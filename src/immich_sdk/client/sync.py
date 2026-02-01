"""Sync API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class SyncClient:
    """Client for Immich Sync endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the sync client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_sync_status(self) -> dict[str, object]:
        """Get sync status.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/sync/status")
        return resp.json()

    def get_upload_checksums(self, dto: dict[str, object]) -> dict[str, object]:
        """Get upload checksums for duplicate detection.

        :param dto: Dict with asset IDs or checksums.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/sync/checksums", json=dto)
        return resp.json()
