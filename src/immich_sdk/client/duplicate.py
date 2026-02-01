"""Duplicates API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import BulkIdsDto
from immich_sdk.client._base import BaseClient


class DuplicatesClient:
    """Client for Immich Duplicates endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the duplicates client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_asset_duplicates(self) -> list[dict[str, object]]:
        """Retrieve a list of duplicate assets available to the authenticated user.

        :returns: List of duplicate asset dicts.
        """
        resp = self._base.get("/api/duplicates")
        return resp.json()

    def delete_duplicates(self, dto: BulkIdsDto) -> None:
        """Delete multiple duplicate assets specified by their IDs.

        :param dto: :class:`BulkIdsDto` with asset IDs.
        """
        self._base.delete(
            "/api/duplicates", json=dto.model_dump(mode="json", exclude_none=True)
        )

    def delete_duplicate(self, id: UUID | str) -> None:
        """Delete a single duplicate asset specified by its ID.

        :param id: Duplicate/asset ID (UUID or string).
        """
        self._base.delete(f"/api/duplicates/{id}")
