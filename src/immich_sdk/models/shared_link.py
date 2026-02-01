"""Shared link-related DTOs."""

from __future__ import annotations

from enum import Enum
from typing import TypeAlias
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.album import AlbumResponseDto
from immich_sdk.models.asset import AssetResponseDto

_AssetList: TypeAlias = list[AssetResponseDto]


class SharedLinkType(str, Enum):
    """Shared link type."""

    ALBUM = "ALBUM"
    INDIVIDUAL = "INDIVIDUAL"


class SharedLinkCreateDto(BaseModel):
    """DTO for creating a shared link."""

    type: SharedLinkType = Field(..., description="Shared link type")
    albumId: UUID | None = Field(None, description="Album ID (for album sharing)")
    assetIds: list[UUID] | None = Field(
        None, description="Asset IDs (for individual assets)"
    )
    allowDownload: bool = Field(True, description="Allow downloads")
    allowUpload: bool | None = Field(None, description="Allow uploads")
    description: str | None = Field(None, description="Link description")
    expiresAt: str | None = Field(None, description="Expiration date")
    password: str | None = Field(None, description="Link password")
    showMetadata: bool = Field(True, description="Show metadata")
    slug: str | None = Field(None, description="Custom URL slug")


class SharedLinkEditDto(BaseModel):
    """DTO for editing a shared link."""

    allowDownload: bool | None = Field(None, description="Allow downloads")
    allowUpload: bool | None = Field(None, description="Allow uploads")
    changeExpiryTime: bool | None = Field(
        None,
        description="Whether to change the expiry time",
    )
    description: str | None = Field(None, description="Link description")
    expiresAt: str | None = Field(None, description="Expiration date")
    password: str | None = Field(None, description="Link password")
    showMetadata: bool | None = Field(None, description="Show metadata")
    slug: str | None = Field(None, description="Custom URL slug")


class SharedLinkResponseDto(BaseModel):
    """Shared link response DTO."""

    id: str = Field(..., description="Shared link ID")
    type: SharedLinkType = Field(..., description="Shared link type")
    allowDownload: bool = Field(..., description="Allow downloads")
    allowUpload: bool = Field(..., description="Allow uploads")
    createdAt: str = Field(..., description="Creation date")
    key: str = Field(..., description="Encryption key (base64url)")
    showMetadata: bool = Field(..., description="Show metadata")
    album: AlbumResponseDto | None = Field(
        None, description="Album (when type is ALBUM)"
    )
    assets: _AssetList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list, description="Assets"
    )
    description: str | None = Field(None, description="Link description")
    expiresAt: str | None = Field(None, description="Expiration date")
    password: str | None = Field(None, description="Has password")
    slug: str | None = Field(None, description="Custom URL slug")
    token: str | None = Field(None, description="Access token")
