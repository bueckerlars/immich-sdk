"""Libraries API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    CreateLibraryDto,
    LibraryResponseDto,
    LibraryStatsResponseDto,
    UpdateLibraryDto,
    ValidateLibraryDto,
    ValidateLibraryResponseDto,
)


class LibrariesClient:
    """Client for Immich Libraries endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the libraries client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_all_libraries(self) -> list[LibraryResponseDto]:
        """Retrieve a list of external libraries.

        :returns: List of :class:`LibraryResponseDto`.
        """
        resp = self._base.get("/api/libraries")
        data = resp.json()
        return [LibraryResponseDto.model_validate(item) for item in data]

    def create_library(self, dto: CreateLibraryDto) -> LibraryResponseDto:
        """Create a new external library.

        :param dto: :class:`CreateLibraryDto` with library settings.
        :returns: :class:`LibraryResponseDto`.
        """
        resp = self._base.post(
            "/api/libraries",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return LibraryResponseDto.model_validate(resp.json())

    def get_library(self, id: UUID | str) -> LibraryResponseDto:
        """Retrieve an external library by its ID.

        :param id: Library ID (UUID or string).
        :returns: :class:`LibraryResponseDto`.
        """
        resp = self._base.get(f"/api/libraries/{id}")
        return LibraryResponseDto.model_validate(resp.json())

    def update_library(
        self, id: UUID | str, dto: UpdateLibraryDto
    ) -> LibraryResponseDto:
        """Update an existing external library.

        :param id: Library ID (UUID or string).
        :param dto: :class:`UpdateLibraryDto` with fields to update.
        :returns: :class:`LibraryResponseDto`.
        """
        resp = self._base.put(
            f"/api/libraries/{id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return LibraryResponseDto.model_validate(resp.json())

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

    def get_library_statistics(self, id: UUID | str) -> LibraryStatsResponseDto:
        """Retrieve statistics for a specific external library.

        :param id: Library ID (UUID or string).
        :returns: :class:`LibraryStatsResponseDto`.
        """
        resp = self._base.get(f"/api/libraries/{id}/statistics")
        return LibraryStatsResponseDto.model_validate(resp.json())

    def validate_library(
        self, id: UUID | str, dto: ValidateLibraryDto
    ) -> ValidateLibraryResponseDto:
        """Validate the settings of an external library.

        :param id: Library ID (UUID or string).
        :param dto: :class:`ValidateLibraryDto` with library settings to validate.
        :returns: :class:`ValidateLibraryResponseDto`.
        """
        resp = self._base.post(
            f"/api/libraries/{id}/validate",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return ValidateLibraryResponseDto.model_validate(resp.json())
