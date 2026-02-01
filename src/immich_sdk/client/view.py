"""View API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class ViewClient:
    """Client for Immich View endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the view client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_view_settings(self) -> dict[str, object]:
        """Get view settings.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/view/settings")
        return resp.json()

    def update_view_settings(self, dto: dict[str, object]) -> dict[str, object]:
        """Update view settings.

        :param dto: Dict with view settings.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put("/api/view/settings", json=dto)
        return resp.json()
