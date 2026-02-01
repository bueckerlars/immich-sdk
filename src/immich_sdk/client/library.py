"""Libraries API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class LibrariesClient:
    """Client for Immich Libraries endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the libraries client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_all_libraries(self) -> list[dict[str, object]]:
        """Retrieve a list of external libraries.

        :returns: List of library dicts.
        """
        resp = self._base.get("/api/libraries")
        return resp.json()

    def create_library(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new external library.

        :param dto: Dict with library settings.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/libraries", json=dto)
        return resp.json()

    def get_library(self, id: UUID | str) -> dict[str, object]:
        """Retrieve an external library by its ID.

        :param id: Library ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/libraries/{id}")
        return resp.json()

    def update_library(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update an existing external library.

        :param id: Library ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/libraries/{id}", json=dto)
        return resp.json()

    def delete_library(self, id: UUID | str) -> None:
        """Delete an external library by its ID.

        :param id: Library ID (UUID or string).
        """
        self._base.delete(f"/api/libraries/{id}")

    def scan_library(self, id: UUID | str) -> None:
        """Queue a scan for the external library to find and import new assets.

        :param id: Library ID (UUID or string).
        """
        self._base.post(f"/api/libraries/{id}/scan")

    def get_library_statistics(self, id: UUID | str) -> dict[str, object]:
        """Retrieve statistics for a specific external library.

        :param id: Library ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/libraries/{id}/statistics")
        return resp.json()

    def validate_library(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Validate the settings of an external library.

        :param id: Library ID (UUID or string).
        :param dto: Dict with library settings to validate.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(f"/api/libraries/{id}/validate", json=dto)
        return resp.json()
