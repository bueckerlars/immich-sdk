"""Tags API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    AssetResponseDto,
    TagCreateDto,
    TagMergeDto,
    TagResponseDto,
    TagUpdateDto,
)


class TagsClient:
    """Client for Immich Tags endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the tags client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_tags(self) -> list[TagResponseDto]:
        """Retrieve all tags.

        :returns: List of :class:`TagResponseDto`.
        """
        resp = self._base.get("/api/tags")
        data = resp.json()
        return [TagResponseDto.model_validate(item) for item in data]

    def create_tag(self, dto: TagCreateDto) -> TagResponseDto:
        """Create a new tag.

        :param dto: :class:`TagCreateDto` with tag data.
        :returns: :class:`TagResponseDto`.
        """
        resp = self._base.post(
            "/api/tags",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return TagResponseDto.model_validate(resp.json())

    def get_tag(self, id: UUID | str) -> TagResponseDto:
        """Retrieve a tag by ID.

        :param id: Tag ID (UUID or string).
        :returns: :class:`TagResponseDto`.
        """
        resp = self._base.get(f"/api/tags/{id}")
        return TagResponseDto.model_validate(resp.json())

    def update_tag(self, id: UUID | str, dto: TagUpdateDto) -> TagResponseDto:
        """Update a tag.

        :param id: Tag ID (UUID or string).
        :param dto: :class:`TagUpdateDto` with fields to update.
        :returns: :class:`TagResponseDto`.
        """
        resp = self._base.patch(
            f"/api/tags/{id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return TagResponseDto.model_validate(resp.json())

    def delete_tag(self, id: UUID | str) -> None:
        """Delete a tag.

        :param id: Tag ID (UUID or string).
        """
        self._base.delete(f"/api/tags/{id}")

    def get_tag_assets(self, id: UUID | str) -> list[AssetResponseDto]:
        """Retrieve assets for a tag.

        :param id: Tag ID (UUID or string).
        :returns: List of :class:`AssetResponseDto`.
        """
        resp = self._base.get(f"/api/tags/{id}/assets")
        data = resp.json()
        return [AssetResponseDto.model_validate(item) for item in data]

    def merge_tags(self, id: UUID | str, dto: TagMergeDto) -> TagResponseDto:
        """Merge multiple tags into one.

        :param id: Target tag ID (UUID or string).
        :param dto: :class:`TagMergeDto` with source tag IDs.
        :returns: :class:`TagResponseDto` (the target tag after merge).
        """
        resp = self._base.post(
            f"/api/tags/{id}/merge",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return TagResponseDto.model_validate(resp.json())
