"""Authentication API client."""

from __future__ import annotations

from immich_sdk.models import (
    AuthStatusResponseDto,
    LoginCredentialDto,
    LoginResponseDto,
)
from immich_sdk.client._base import BaseClient


class AuthClient:
    """Client for Immich Authentication endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the auth client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def login(self, dto: LoginCredentialDto) -> LoginResponseDto:
        """Login with username and password and receive a session token.

        :param dto: :class:`LoginCredentialDto` with email and password.
        :returns: :class:`LoginResponseDto` with session token and user info.
        """
        resp = self._base.post("/api/auth/login", json=dto.model_dump(mode="json"))
        return LoginResponseDto.model_validate(resp.json())

    def get_auth_status(self) -> AuthStatusResponseDto:
        """Get information about the current session.

        :returns: :class:`AuthStatusResponseDto`.
        """
        resp = self._base.get("/api/auth/status")
        return AuthStatusResponseDto.model_validate(resp.json())

    def logout(self) -> dict[str, object]:
        """Logout the current user and invalidate the session token.

        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/auth/logout")
        return resp.json()

    def change_password(self, dto: dict[str, object]) -> dict[str, object]:
        """Change the password of the current user.

        :param dto: Dict with old and new password.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/auth/change-password", json=dto)
        return resp.json()

    def validate_access_token(self) -> dict[str, object]:
        """Validate the current authorization method is still valid.

        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/auth/validateToken")
        return resp.json()
