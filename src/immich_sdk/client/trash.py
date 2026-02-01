"""Trash API client."""

from __future__ import annotations

from immich_sdk.models import BulkIdsDto
from immich_sdk.client._base import BaseClient


class TrashClient:
    """Client for Immich Trash endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the trash client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_trash(self) -> list[dict[str, object]]:
        """Retrieve trashed assets.

        :returns: List of trashed asset dicts.
        """
        resp = self._base.get("/api/trash")
        return resp.json()

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
