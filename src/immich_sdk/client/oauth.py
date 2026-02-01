"""OAuth API client."""

from __future__ import annotations

from typing import Any

from immich_sdk.client._base import BaseClient
from immich_sdk.models.oauth import (
    OAuthAuthorizeResponseDto,
    OAuthCallbackDto,
    OAuthConfigDto,
    OAuthMobileRedirectDto,
)


class OAuthClient:
    """Client for Immich OAuth endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the OAuth client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def start_oauth(self, dto: OAuthConfigDto) -> OAuthAuthorizeResponseDto:
        """Start OAuth flow.

        :param dto: OAuth config (redirect URI, state, code challenge).
        :returns: Authorize response with URL to redirect user.
        """
        resp = self._base.post(
            "/api/oauth/authorize",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return OAuthAuthorizeResponseDto.model_validate(resp.json())

    def finish_oauth(self, dto: OAuthCallbackDto) -> dict[str, Any]:
        """Finish OAuth flow (callback). Returns token/session; type varies by server.

        :param dto: OAuth callback DTO (url, state, codeVerifier).
        :returns: Response (e.g. login response); structure is server-specific.
        """
        resp = self._base.post(
            "/api/oauth/callback",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return resp.json()

    def link_oauth_account(self, dto: OAuthCallbackDto) -> None:
        """Link OAuth account.

        :param dto: OAuth callback DTO (url, state, codeVerifier).
        """
        self._base.post(
            "/api/oauth/link",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )

    def redirect_oauth_to_mobile(
        self, dto: OAuthMobileRedirectDto
    ) -> OAuthMobileRedirectDto:
        """Redirect OAuth to mobile.

        :param dto: Redirect DTO (url).
        :returns: Redirect response.
        """
        resp = self._base.post(
            "/api/oauth/mobile-redirect",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return OAuthMobileRedirectDto.model_validate(resp.json())

    def unlink_oauth_account(self) -> None:
        """Unlink OAuth account."""
        self._base.delete("/api/oauth/unlink")
