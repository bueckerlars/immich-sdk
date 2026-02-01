"""Tags API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class TagsClient:
    """Client for Immich Tags endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the tags client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_tags(self) -> list[dict[str, object]]:
        """Retrieve all tags.

        :returns: List of tag dicts.
        """
        resp = self._base.get("/api/tags")
        return resp.json()

    def create_tag(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new tag.

        :param dto: Dict with tag data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/tags", json=dto)
        return resp.json()

    def get_tag(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a tag by ID.

        :param id: Tag ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/tags/{id}")
        return resp.json()

    def update_tag(self, id: UUID | str, dto: dict[str, object]) -> dict[str, object]:
        """Update a tag.

        :param id: Tag ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.patch(f"/api/tags/{id}", json=dto)
        return resp.json()

    def delete_tag(self, id: UUID | str) -> None:
        """Delete a tag.

        :param id: Tag ID (UUID or string).
        """
        self._base.delete(f"/api/tags/{id}")

    def get_tag_assets(self, id: UUID | str) -> list[dict[str, object]]:
        """Retrieve assets for a tag.

        :param id: Tag ID (UUID or string).
        :returns: List of asset dicts.
        """
        resp = self._base.get(f"/api/tags/{id}/assets")
        return resp.json()

    def merge_tags(self, id: UUID | str, dto: dict[str, object]) -> dict[str, object]:
        """Merge multiple tags into one.

        :param id: Target tag ID (UUID or string).
        :param dto: Dict with source tag IDs.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(f"/api/tags/{id}/merge", json=dto)
        return resp.json()
