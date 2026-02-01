"""View API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.view import ViewSettingsDto


class ViewClient:
    """Client for Immich View endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the view client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_view_settings(self) -> ViewSettingsDto:
        """Get view settings.

        :returns: View settings DTO.
        """
        resp = self._base.get("/api/view/settings")
        return ViewSettingsDto.model_validate(resp.json())

    def update_view_settings(self, dto: ViewSettingsDto) -> ViewSettingsDto:
        """Update view settings.

        :param dto: View settings DTO.
        :returns: Updated view settings.
        """
        payload = dto.model_dump(by_alias=True, exclude_none=True)
        resp = self._base.put("/api/view/settings", json=payload)
        return ViewSettingsDto.model_validate(resp.json())
