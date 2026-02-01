"""System config API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class SystemConfigClient:
    """Client for Immich System config endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the system config client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_system_config(self) -> dict[str, object]:
        """Get system config.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/system-config")
        return resp.json()

    def update_system_config(self, dto: dict[str, object]) -> dict[str, object]:
        """Update system config.

        :param dto: Dict with config fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put("/api/system-config", json=dto)
        return resp.json()

    def get_storage_template_options(self) -> dict[str, object]:
        """Get storage template options.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/system-config/storage-template-options")
        return resp.json()
