"""Exceptions for the Immich API SDK."""


class ImmichAPIException(Exception):
    """Base exception for all Immich API exceptions."""


class ImmichHTTPError(ImmichAPIException):
    """Raised when the API returns a non-2xx HTTP status.

    :ivar status_code: HTTP status code (e.g. 404, 500).
    :ivar message: Optional error message from the response body.
    :ivar response_body: Raw response body (string or bytes).
    """

    def __init__(
        self,
        status_code: int,
        message: str | None = None,
        response_body: str | bytes | None = None,
    ) -> None:
        """Initialize the error.

        :param status_code: HTTP status code (e.g. 404, 500).
        :param message: Optional error message from the response body.
        :param response_body: Raw response body (string or bytes).
        """
        self.status_code = status_code
        self.message = message
        self.response_body = response_body
        parts = [f"HTTP {status_code}"]
        if message:
            parts.append(message)
        super().__init__(": ".join(parts))


class ImmichValidationError(ImmichAPIException):
    """Raised when the API returns 422 Unprocessable Entity (validation error).

    :ivar status_code: 422.
    :ivar message: Optional validation error message.
    :ivar details: Optional list of field-level validation errors.
    """

    def __init__(
        self,
        status_code: int = 422,
        message: str | None = None,
        details: list[dict[str, object]] | None = None,
    ) -> None:
        """Initialize the validation error.

        :param status_code: HTTP status code (default 422).
        :param message: Optional validation error message.
        :param details: Optional list of field-level validation errors.
        """
        self.status_code = status_code
        self.message = message
        self.details = details or []
        super().__init__(message or "Validation error")
