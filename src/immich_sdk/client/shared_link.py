"""Shared links API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    BulkIdResponseDto,
    BulkIdsDto,
    SharedLinkCreateDto,
    SharedLinkEditDto,
    SharedLinkResponseDto,
)


class SharedLinksClient:
    """Client for Immich Shared links endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the shared links client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def create_shared_link(self, dto: SharedLinkCreateDto) -> SharedLinkResponseDto:
        """Create a new shared link.

        :param dto: Dict with shared link options.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(
            "/api/shared-link",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return SharedLinkResponseDto.model_validate(resp.json())

    def get_shared_links(self) -> list[SharedLinkResponseDto]:
        """Retrieve all shared links.

        :returns: List of shared link dicts.
        """
        resp = self._base.get("/api/shared-link")
        data = resp.json()
        return [SharedLinkResponseDto.model_validate(item) for item in data]

    def get_my_shared_link(
        self, key: str | None = None, slug: str | None = None
    ) -> SharedLinkResponseDto:
        """Retrieve the shared link for the current user (by key/slug).

        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: Raw response dict from the API.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.get("/api/shared-link/me", params=params or None)
        return SharedLinkResponseDto.model_validate(resp.json())

    def get_shared_link(
        self, id: UUID | str, key: str | None = None, slug: str | None = None
    ) -> SharedLinkResponseDto:
        """Retrieve a shared link by ID.

        :param id: Shared link ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: Raw response dict from the API.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.get(f"/api/shared-link/{id}", params=params or None)
        return SharedLinkResponseDto.model_validate(resp.json())

    def update_shared_link(
        self, id: UUID | str, dto: SharedLinkEditDto
    ) -> SharedLinkResponseDto:
        """Update a shared link.

        :param id: Shared link ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.patch(
            f"/api/shared-link/{id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return SharedLinkResponseDto.model_validate(resp.json())

    def remove_shared_link(self, id: UUID | str) -> None:
        """Remove a shared link.

        :param id: Shared link ID (UUID or string).
        """
        self._base.delete(f"/api/shared-link/{id}")

    def add_assets_to_shared_link(
        self,
        id: UUID | str,
        dto: BulkIdsDto,
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> list[BulkIdResponseDto]:
        """Add assets to a shared link.

        :param id: Shared link ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: List of :class:`BulkIdResponseDto`.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.put(
            f"/api/shared-link/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
            params=params or None,
        )
        data = resp.json()
        return [BulkIdResponseDto.model_validate(item) for item in data]

    def remove_assets_from_shared_link(
        self, id: UUID | str, dto: BulkIdsDto
    ) -> list[BulkIdResponseDto]:
        """Remove assets from a shared link.

        :param id: Shared link ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: List of :class:`BulkIdResponseDto`.
        """
        resp = self._base.delete(
            f"/api/shared-link/{id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        data = resp.json()
        return [BulkIdResponseDto.model_validate(item) for item in data]
