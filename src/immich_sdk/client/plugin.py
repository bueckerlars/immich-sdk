"""Plugins API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.plugin import (
    PluginResponseDto,
    PluginTriggerResponseDto,
)


class PluginsClient:
    """Client for Immich Plugins endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the plugins client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_plugins(self) -> list[PluginResponseDto]:
        """Retrieve all plugins.

        :returns: List of plugin DTOs.
        """
        resp = self._base.get("/api/plugins")
        return [PluginResponseDto.model_validate(p) for p in resp.json()]

    def get_plugin_triggers(self) -> list[PluginTriggerResponseDto]:
        """Retrieve plugin triggers.

        :returns: List of trigger DTOs.
        """
        resp = self._base.get("/api/plugins/triggers")
        return [PluginTriggerResponseDto.model_validate(t) for t in resp.json()]

    def get_plugin(self, id: UUID | str) -> PluginResponseDto:
        """Retrieve a plugin by ID.

        :param id: Plugin ID (UUID or string).
        :returns: Plugin DTO.
        """
        resp = self._base.get(f"/api/plugins/{id}")
        return PluginResponseDto.model_validate(resp.json())
