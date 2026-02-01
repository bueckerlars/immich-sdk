"""Sync API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.sync import (
    SyncChecksumsRequestDto,
    SyncChecksumsResponseDto,
    SyncStatusResponseDto,
)


class SyncClient:
    """Client for Immich Sync endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the sync client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_sync_status(self) -> SyncStatusResponseDto:
        """Get sync status.

        :returns: Sync status response.
        """
        resp = self._base.get("/api/sync/status")
        return SyncStatusResponseDto.model_validate(resp.json())

    def get_upload_checksums(
        self, dto: SyncChecksumsRequestDto
    ) -> SyncChecksumsResponseDto:
        """Get upload checksums for duplicate detection.

        :param dto: Request DTO (e.g. asset IDs or checksums).
        :returns: Checksums response.
        """
        resp = self._base.post(
            "/api/sync/checksums",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return SyncChecksumsResponseDto.model_validate(resp.json())
