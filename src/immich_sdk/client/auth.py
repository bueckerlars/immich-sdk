"""Authentication API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.auth import (
    AuthStatusResponseDto,
    ChangePasswordDto,
    LoginCredentialDto,
    LoginResponseDto,
    LogoutResponseDto,
    ValidateAccessTokenResponseDto,
)
from immich_sdk.models.user import UserResponseDto


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

    def logout(self) -> LogoutResponseDto:
        """Logout the current user and invalidate the session token.

        :returns: Logout response.
        """
        resp = self._base.post("/api/auth/logout")
        return LogoutResponseDto.model_validate(resp.json())

    def change_password(self, dto: ChangePasswordDto) -> UserResponseDto:
        """Change the password of the current user.

        :param dto: Change password DTO.
        :returns: Updated user response (non-admin, matches /api/auth/ endpoint).
        """
        resp = self._base.post(
            "/api/auth/change-password",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return UserResponseDto.model_validate(resp.json())

    def validate_access_token(self) -> ValidateAccessTokenResponseDto:
        """Validate the current authorization method is still valid.

        :returns: Validate token response.
        """
        resp = self._base.post("/api/auth/validateToken")
        return ValidateAccessTokenResponseDto.model_validate(resp.json())
