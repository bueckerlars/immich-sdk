"""Plugins API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class PluginsClient:
    """Client for Immich Plugins endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the plugins client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_plugins(self) -> list[dict[str, object]]:
        """Retrieve all plugins.

        :returns: List of plugin dicts.
        """
        resp = self._base.get("/api/plugins")
        return resp.json()

    def get_plugin_triggers(self) -> list[dict[str, object]]:
        """Retrieve plugin triggers.

        :returns: List of trigger dicts.
        """
        resp = self._base.get("/api/plugins/triggers")
        return resp.json()

    def get_plugin(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a plugin by ID.

        :param id: Plugin ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/plugins/{id}")
        return resp.json()
