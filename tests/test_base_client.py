"""Tests for BaseClient."""

from unittest.mock import patch

import httpx
import pytest

from immich_sdk.client._base import BaseClient
from immich_sdk.exception import ImmichHTTPError, ImmichValidationError


def test_get_sends_api_key_header() -> None:
    """BaseClient.get sends x-api-key header."""
    with patch("immich_sdk.client._base.httpx.Client") as mock_client_class:
        mock_response = httpx.Response(200, json={"ok": True})
        mock_response.request = httpx.Request("GET", "https://example.com/api/albums")
        mock_client_class.return_value.__enter__.return_value.request.return_value = (
            mock_response
        )

        base = BaseClient(
            base_url="https://example.com", api_key="test-key", enable_logging=False
        )
        base.get("/api/albums")

        call_kwargs = (
            mock_client_class.return_value.__enter__.return_value.request.call_args[1]
        )
        assert call_kwargs["headers"]["x-api-key"] == "test-key"


def test_get_raises_immich_http_error_on_404() -> None:
    """BaseClient.get raises ImmichHTTPError on 404."""
    with patch("immich_sdk.client._base.httpx.Client") as mock_client_class:
        mock_response = httpx.Response(
            404,
            json={"message": "Not found"},
            request=httpx.Request("GET", "https://example.com/api/albums"),
        )
        mock_client_class.return_value.__enter__.return_value.request.return_value = (
            mock_response
        )

        base = BaseClient(
            base_url="https://example.com", api_key="test-key", enable_logging=False
        )

        with pytest.raises(ImmichHTTPError) as exc_info:
            base.get("/api/albums")
        assert exc_info.value.status_code == 404
        assert "Not found" in str(exc_info.value)


def test_get_raises_immich_validation_error_on_422() -> None:
    """BaseClient.get raises ImmichValidationError on 422."""
    with patch("immich_sdk.client._base.httpx.Client") as mock_client_class:
        mock_response = httpx.Response(
            422,
            json={"message": "Validation failed", "details": []},
            request=httpx.Request("GET", "https://example.com/api/albums"),
        )
        mock_client_class.return_value.__enter__.return_value.request.return_value = (
            mock_response
        )

        base = BaseClient(
            base_url="https://example.com", api_key="test-key", enable_logging=False
        )

        with pytest.raises(ImmichValidationError) as exc_info:
            base.get("/api/albums")
        assert exc_info.value.status_code == 422
