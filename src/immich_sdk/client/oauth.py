"""OAuth API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class OAuthClient:
    """Client for Immich OAuth endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the OAuth client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def start_oauth(self, dto: dict[str, object]) -> dict[str, object]:
        """Start OAuth flow.

        :param dto: Dict with OAuth provider and redirect info.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/oauth/authorize", json=dto)
        return resp.json()

    def finish_oauth(self, dto: dict[str, object]) -> dict[str, object]:
        """Finish OAuth flow.

        :param dto: Dict with OAuth callback data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/oauth/callback", json=dto)
        return resp.json()

    def link_oauth_account(self, dto: dict[str, object]) -> None:
        """Link OAuth account.

        :param dto: Dict with OAuth link data.
        """
        self._base.post("/api/oauth/link", json=dto)

    def redirect_oauth_to_mobile(self, dto: dict[str, object]) -> dict[str, object]:
        """Redirect OAuth to mobile.

        :param dto: Dict with redirect data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/oauth/mobile-redirect", json=dto)
        return resp.json()

    def unlink_oauth_account(self) -> None:
        """Unlink OAuth account."""
        self._base.delete("/api/oauth/unlink")
