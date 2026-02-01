"""Trash API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models import AssetResponseDto, BulkIdsDto


class TrashClient:
    """Client for Immich Trash endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the trash client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_trash(self) -> list[AssetResponseDto]:
        """Retrieve trashed assets.

        :returns: List of :class:`AssetResponseDto`.
        """
        resp = self._base.get("/api/trash")
        data = resp.json()
        return [AssetResponseDto.model_validate(item) for item in data]

    def restore_assets(self, dto: BulkIdsDto) -> None:
        """Restore assets from trash.

        :param dto: :class:`BulkIdsDto` with asset IDs.
        """
        self._base.post(
            "/api/trash/restore", json=dto.model_dump(mode="json", exclude_none=True)
        )

    def empty_trash(self) -> None:
        """Empty the trash."""
        self._base.post("/api/trash/empty")
