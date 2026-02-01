"""Maintenance (admin) API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class MaintenanceClient:
    """Client for Immich Maintenance (admin) endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the maintenance client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def set_maintenance_mode(self, dto: dict[str, object]) -> None:
        """Put Immich into or take it out of maintenance mode.

        :param dto: Dict with maintenance mode flag.
        """
        self._base.post("/api/admin/maintenance", json=dto)

    def detect_prior_install(self) -> dict[str, object]:
        """Collect integrity checks and other heuristics about local data.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/admin/maintenance/detect-install")
        return resp.json()

    def maintenance_login(self, dto: dict[str, object]) -> dict[str, object]:
        """Login with maintenance token or cookie.

        :param dto: Dict with token or cookie.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/admin/maintenance/login", json=dto)
        return resp.json()

    def get_maintenance_status(self) -> dict[str, object]:
        """Fetch information about the currently running maintenance action.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/admin/maintenance/status")
        return resp.json()
