"""Memories API client."""

from __future__ import annotations

from typing import Any, cast
from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.common import BulkIdsDto
from immich_sdk.models.memory import (
    MemoryCreateDto,
    MemoryResponseDto,
    MemoryStatisticsResponseDto,
    MemoryUpdateDto,
)


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
    ) -> list[MemoryResponseDto]:
        """Retrieve a list of memories.

        :param for_date: Optional date filter.
        :param is_saved: Optional filter for saved memories.
        :param is_trashed: Optional filter for trashed memories.
        :param order: Optional sort order.
        :param size: Optional page size.
        :param type_filter: Optional type filter.
        :returns: List of memory DTOs.
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
        data = resp.json()
        items: list[dict[str, Any]] = cast(
            list[dict[str, Any]], data if isinstance(data, list) else [data]
        )
        return [MemoryResponseDto.model_validate(m) for m in items]

    def create_memory(self, dto: MemoryCreateDto) -> MemoryResponseDto:
        """Create a new memory.

        :param dto: Memory create DTO.
        :returns: Created memory DTO.
        """
        resp = self._base.post(
            "/api/memories",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return MemoryResponseDto.model_validate(resp.json())

    def get_memory(self, id: UUID | str) -> MemoryResponseDto:
        """Retrieve a specific memory by its ID.

        :param id: Memory ID (UUID or string).
        :returns: Memory DTO.
        """
        resp = self._base.get(f"/api/memories/{id}")
        return MemoryResponseDto.model_validate(resp.json())

    def update_memory(self, id: UUID | str, dto: MemoryUpdateDto) -> MemoryResponseDto:
        """Update an existing memory by its ID.

        :param id: Memory ID (UUID or string).
        :param dto: Memory update DTO.
        :returns: Updated memory DTO.
        """
        resp = self._base.put(
            f"/api/memories/{id}",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return MemoryResponseDto.model_validate(resp.json())

    def delete_memory(self, id: UUID | str) -> None:
        """Delete a specific memory by its ID.

        :param id: Memory ID (UUID or string).
        """
        self._base.delete(f"/api/memories/{id}")

    def add_memory_assets(
        self, id: UUID | str, dto: BulkIdsDto
    ) -> list[MemoryResponseDto]:
        """Add a list of asset IDs to a specific memory.

        :param id: Memory ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: Updated memory (or list of memories); API may return list.
        """
        resp = self._base.put(
            f"/api/memories/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        data = resp.json()
        if isinstance(data, list):
            items: list[dict[str, Any]] = cast(list[dict[str, Any]], data)
            return [MemoryResponseDto.model_validate(m) for m in items]
        return [MemoryResponseDto.model_validate(data)]

    def remove_memory_assets(
        self, id: UUID | str, dto: BulkIdsDto
    ) -> list[MemoryResponseDto]:
        """Remove a list of asset IDs from a specific memory.

        :param id: Memory ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: Updated memory (or list); API may return list.
        """
        resp = self._base.delete(
            f"/api/memories/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        data = resp.json()
        if isinstance(data, list):
            items_rm: list[dict[str, Any]] = cast(list[dict[str, Any]], data)
            return [MemoryResponseDto.model_validate(m) for m in items_rm]
        return [MemoryResponseDto.model_validate(data)]

    def memories_statistics(
        self,
        *,
        for_date: str | None = None,
        is_saved: bool | None = None,
        is_trashed: bool | None = None,
        order: str | None = None,
        size: int | None = None,
        type_filter: str | None = None,
    ) -> MemoryStatisticsResponseDto:
        """Retrieve statistics about memories.

        :param for_date: Optional date filter.
        :param is_saved: Optional filter for saved memories.
        :param is_trashed: Optional filter for trashed memories.
        :param order: Optional sort order.
        :param size: Optional page size.
        :param type_filter: Optional type filter.
        :returns: Memory statistics DTO.
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
        return MemoryStatisticsResponseDto.model_validate(resp.json())
