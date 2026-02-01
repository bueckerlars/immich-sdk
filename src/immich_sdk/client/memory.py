"""Memories API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import BulkIdsDto
from immich_sdk.client._base import BaseClient


class MemoriesClient:
    """Client for Immich Memories endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the memories client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def search_memories(
        self,
        *,
        for_date: str | None = None,
        is_saved: bool | None = None,
        is_trashed: bool | None = None,
        order: str | None = None,
        size: int | None = None,
        type_filter: str | None = None,
    ) -> list[dict[str, object]]:
        """Retrieve a list of memories.

        :param for_date: Optional date filter.
        :param is_saved: Optional filter for saved memories.
        :param is_trashed: Optional filter for trashed memories.
        :param order: Optional sort order.
        :param size: Optional page size.
        :param type_filter: Optional type filter.
        :returns: List of memory dicts.
        """
        params: dict[str, str | int | bool] = {}
        if for_date is not None:
            params["for"] = for_date
        if is_saved is not None:
            params["isSaved"] = is_saved
        if is_trashed is not None:
            params["isTrashed"] = is_trashed
        if order is not None:
            params["order"] = order
        if size is not None:
            params["size"] = size
        if type_filter is not None:
            params["type"] = type_filter
        resp = self._base.get("/api/memories", params=params or None)
        return resp.json()

    def create_memory(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new memory.

        :param dto: Dict with memory data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/memories", json=dto)
        return resp.json()

    def get_memory(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a specific memory by its ID.

        :param id: Memory ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/memories/{id}")
        return resp.json()

    def update_memory(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update an existing memory by its ID.

        :param id: Memory ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/memories/{id}", json=dto)
        return resp.json()

    def delete_memory(self, id: UUID | str) -> None:
        """Delete a specific memory by its ID.

        :param id: Memory ID (UUID or string).
        """
        self._base.delete(f"/api/memories/{id}")

    def add_memory_assets(
        self, id: UUID | str, dto: BulkIdsDto
    ) -> list[dict[str, object]]:
        """Add a list of asset IDs to a specific memory.

        :param id: Memory ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: List of response dicts.
        """
        resp = self._base.put(
            f"/api/memories/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return resp.json()

    def remove_memory_assets(
        self, id: UUID | str, dto: BulkIdsDto
    ) -> list[dict[str, object]]:
        """Remove a list of asset IDs from a specific memory.

        :param id: Memory ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: List of response dicts.
        """
        resp = self._base.delete(
            f"/api/memories/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return resp.json()

    def memories_statistics(
        self,
        *,
        for_date: str | None = None,
        is_saved: bool | None = None,
        is_trashed: bool | None = None,
        order: str | None = None,
        size: int | None = None,
        type_filter: str | None = None,
    ) -> dict[str, object]:
        """Retrieve statistics about memories.

        :param for_date: Optional date filter.
        :param is_saved: Optional filter for saved memories.
        :param is_trashed: Optional filter for trashed memories.
        :param order: Optional sort order.
        :param size: Optional page size.
        :param type_filter: Optional type filter.
        :returns: Raw response dict from the API.
        """
        params: dict[str, str | int | bool] = {}
        if for_date is not None:
            params["for"] = for_date
        if is_saved is not None:
            params["isSaved"] = is_saved
        if is_trashed is not None:
            params["isTrashed"] = is_trashed
        if order is not None:
            params["order"] = order
        if size is not None:
            params["size"] = size
        if type_filter is not None:
            params["type"] = type_filter
        resp = self._base.get("/api/memories/statistics", params=params or None)
        return resp.json()
