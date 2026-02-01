"""Sync-related DTOs."""

from pydantic import BaseModel, ConfigDict


class SyncStatusResponseDto(BaseModel):
    """Sync status response (structure may vary)."""

    model_config = ConfigDict(extra="allow")


class SyncChecksumsRequestDto(BaseModel):
    """Request for upload checksums (e.g. asset IDs)."""

    model_config = ConfigDict(extra="allow")


class SyncChecksumsResponseDto(BaseModel):
    """Response from checksums endpoint."""

    model_config = ConfigDict(extra="allow")
