"""Maintenance (admin) API client."""

from __future__ import annotations

from typing import Any

from immich_sdk.client._base import BaseClient
from immich_sdk.models.maintenance import (
    MaintenanceDetectInstallResponseDto,
    MaintenanceLoginDto,
    MaintenanceStatusResponseDto,
    SetMaintenanceModeDto,
)


class MaintenanceClient:
    """Client for Immich Maintenance (admin) endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the maintenance client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def set_maintenance_mode(self, dto: SetMaintenanceModeDto) -> None:
        """Put Immich into or take it out of maintenance mode.

        :param dto: Set maintenance mode DTO.
        """
        self._base.post(
            "/api/admin/maintenance",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )

    def detect_prior_install(self) -> MaintenanceDetectInstallResponseDto:
        """Collect integrity checks and other heuristics about local data.

        :returns: Detect install response.
        """
        resp = self._base.get("/api/admin/maintenance/detect-install")
        return MaintenanceDetectInstallResponseDto.model_validate(resp.json())

    def maintenance_login(self, dto: MaintenanceLoginDto) -> dict[str, Any]:
        """Login with maintenance token or cookie.

        :param dto: Maintenance login DTO (token).
        :returns: Login response (e.g. session); structure is server-specific.
        """
        resp = self._base.post(
            "/api/admin/maintenance/login",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return resp.json()

    def get_maintenance_status(self) -> MaintenanceStatusResponseDto:
        """Fetch information about the currently running maintenance action.

        :returns: Maintenance status response.
        """
        resp = self._base.get("/api/admin/maintenance/status")
        return MaintenanceStatusResponseDto.model_validate(resp.json())
