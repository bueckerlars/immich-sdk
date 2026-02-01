"""Base HTTP client for the Immich API with auth, retry, and logging."""

from __future__ import annotations

import time
from typing import Any, TypeVar, cast

import httpx
from loguru import logger
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from immich_sdk.exception import ImmichHTTPError, ImmichValidationError

T = TypeVar("T")


def _should_retry(exc: BaseException) -> bool:
    """Retry on connection errors and 429/5xx only.

    :param exc: The exception that was raised.
    :returns: True if the request should be retried.
    """

    def _retry_if_status(ex: httpx.HTTPStatusError) -> bool:
        return ex.response.status_code == 429 or ex.response.status_code >= 500

    if isinstance(exc, httpx.HTTPStatusError):
        return _retry_if_status(exc)
    if isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout)):
        return True
    return False


class BaseClient:
    """Low-level HTTP client for Immich API with API key auth, retry, and logging."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        timeout: float = 30.0,
        max_retries: int = 3,
        enable_logging: bool = True,
    ) -> None:
        """Initialize the base client.

        :param base_url: Immich server URL without trailing slash (e.g. https://immich.example.com).
        :param api_key: API key for authentication (x-api-key header).
        :param timeout: Request timeout in seconds.
        :param max_retries: Maximum number of retries for 429/5xx and connection errors.
        :param enable_logging: Whether to log requests and responses (debug/info).
        """
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout
        self._max_retries = max_retries
        self._enable_logging = enable_logging
        self._log = logger.bind(component="immich_sdk")

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        content: bytes | None = None,
        files: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Execute an HTTP request with auth, retry, and error handling.

        :param method: HTTP method (GET, POST, etc.).
        :param path: URL path (e.g. /api/albums).
        :param params: Optional query parameters.
        :param json: Optional JSON body.
        :param content: Optional raw body bytes.
        :param files: Optional multipart files.
        :param data: Optional form data.
        :param headers: Optional additional headers.
        :returns: The HTTP response (after raise_for_status).
        :raises ImmichHTTPError: On non-2xx status (except 422).
        :raises ImmichValidationError: On 422 validation error.
        """
        url = f"{self._base_url}{path}"
        request_headers = {"x-api-key": self._api_key}
        if headers:
            request_headers.update(headers)

        start = time.monotonic()

        @retry(
            retry=retry_if_exception(_should_retry),
            stop=stop_after_attempt(max(self._max_retries, 1)),
            wait=wait_exponential(multiplier=1, min=1, max=10),
            reraise=True,
            before_sleep=lambda rs: (
                self._log.warning(
                    "Retrying after {}: {}",
                    rs.outcome.exception() if rs.outcome else "unknown",
                    path,
                )
                if self._enable_logging
                else None
            ),
        )
        def _do_request() -> httpx.Response:
            with httpx.Client(timeout=self._timeout) as client:
                resp = client.request(
                    method,
                    url,
                    params=params,
                    json=json if json is not None and files is None else None,
                    content=content,
                    files=files,
                    data=data,
                    headers=request_headers,
                )
                resp.raise_for_status()
            return resp

        try:
            resp = _do_request()
        except httpx.HTTPStatusError as e:
            self._raise_for_status(e.response)
            raise  # unreachable

        if self._enable_logging:
            elapsed = time.monotonic() - start
            self._log.debug(
                "{} {} -> {} ({:.2f}s)", method, path, resp.status_code, elapsed
            )
        return resp

    def _raise_for_status(self, resp: httpx.Response) -> None:
        """Parse error response and raise :class:`ImmichHTTPError` or :class:`ImmichValidationError`.

        :param resp: The HTTP response with error status.
        :raises ImmichValidationError: If status code is 422.
        :raises ImmichHTTPError: For any other non-2xx status.
        """
        body: str | bytes | None = resp.content
        message: str | None = None
        details: list[dict[str, object]] | None = None
        try:
            if resp.headers.get("content-type", "").startswith("application/json"):
                raw = resp.json()
                data = cast(dict[str, object], raw) if isinstance(raw, dict) else None
                if data is not None:
                    msg: object = data.get("message") or data.get("error")
                    message = str(msg) if msg is not None else None
                    det: object = data.get("details")
                    details = (
                        cast("list[dict[str, object]] | None", det)
                        if isinstance(det, list)
                        else None
                    )
                body = resp.text
        except Exception:
            pass
        if resp.status_code == 422:
            raise ImmichValidationError(
                status_code=422,
                message=message or resp.text,
                details=details,
            )
        err_msg: str = message or resp.text
        raise ImmichHTTPError(
            status_code=resp.status_code,
            message=err_msg,
            response_body=body,
        )

    def get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Perform a GET request.

        :param path: URL path.
        :param params: Optional query parameters.
        :param headers: Optional additional headers.
        :returns: The HTTP response.
        """
        if self._enable_logging:
            self._log.debug("GET {}", path)
        return self._request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        content: bytes | None = None,
        files: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Perform a POST request.

        :param path: URL path.
        :param params: Optional query parameters.
        :param json: Optional JSON body.
        :param content: Optional raw body bytes.
        :param files: Optional multipart files.
        :param data: Optional form data.
        :param headers: Optional additional headers.
        :returns: The HTTP response.
        """
        if self._enable_logging:
            self._log.debug("POST {}", path)
        return self._request(
            "POST",
            path,
            params=params,
            json=json,
            content=content,
            files=files,
            data=data,
            headers=headers,
        )

    def put(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        content: bytes | None = None,
        files: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Perform a PUT request.

        :param path: URL path.
        :param params: Optional query parameters.
        :param json: Optional JSON body.
        :param content: Optional raw body bytes.
        :param files: Optional multipart files.
        :param data: Optional form data.
        :param headers: Optional additional headers.
        :returns: The HTTP response.
        """
        if self._enable_logging:
            self._log.debug("PUT {}", path)
        return self._request(
            "PUT",
            path,
            params=params,
            json=json,
            content=content,
            files=files,
            data=data,
            headers=headers,
        )

    def patch(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Perform a PATCH request.

        :param path: URL path.
        :param params: Optional query parameters.
        :param json: Optional JSON body.
        :param headers: Optional additional headers.
        :returns: The HTTP response.
        """
        if self._enable_logging:
            self._log.debug("PATCH {}", path)
        return self._request("PATCH", path, params=params, json=json, headers=headers)

    def delete(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Perform a DELETE request.

        :param path: URL path.
        :param params: Optional query parameters.
        :param json: Optional JSON body.
        :param headers: Optional additional headers.
        :returns: The HTTP response.
        """
        if self._enable_logging:
            self._log.debug("DELETE {}", path)
        return self._request("DELETE", path, params=params, json=json, headers=headers)
