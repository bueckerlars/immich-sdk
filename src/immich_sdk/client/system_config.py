"""System config API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.system_config import (
    StorageTemplateOptionsDto,
    SystemConfigDto,
    SystemConfigUpdateDto,
)


class SystemConfigClient:
    """Client for Immich System config endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the system config client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_system_config(self) -> SystemConfigDto:
        """Get system config.

        :returns: System config DTO.
        """
        resp = self._base.get("/api/system-config")
        return SystemConfigDto.model_validate(resp.json())

    def update_system_config(self, dto: SystemConfigUpdateDto) -> SystemConfigDto:
        """Update system config.

        :param dto: Config fields to update.
        :returns: Updated system config DTO.
        """
        resp = self._base.put(
            "/api/system-config",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return SystemConfigDto.model_validate(resp.json())

    def get_storage_template_options(self) -> StorageTemplateOptionsDto:
        """Get storage template options.

        :returns: Storage template options DTO.
        """
        resp = self._base.get("/api/system-config/storage-template-options")
        return StorageTemplateOptionsDto.model_validate(resp.json())
