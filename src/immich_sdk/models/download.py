"""Download-related DTOs."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, Field


class DownloadArchiveInfo(BaseModel):
    """Archive info in download response."""

    assetIds: list[str] = Field(..., description="Asset IDs in this archive")
    size: int = Field(..., description="Archive size in bytes")


class DownloadInfoDto(BaseModel):
    """Request DTO for download info."""

    assetIds: list[UUID | str] | None = Field(None, description="Asset IDs to download")
    albumId: UUID | str | None = Field(None, description="Album ID to download")
    userId: UUID | str | None = Field(
        None, description="User ID to download assets from"
    )
    archiveSize: int | None = Field(None, description="Archive size limit in bytes")


class DownloadResponseDto(BaseModel):
    """Response DTO for download info."""

    archives: list[DownloadArchiveInfo] = Field(..., description="Archive information")
    totalSize: int = Field(..., description="Total size in bytes")
