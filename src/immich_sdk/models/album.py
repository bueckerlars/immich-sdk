"""Album-related DTOs."""

from __future__ import annotations

from typing import TypeAlias
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.asset import AssetResponseDto
from immich_sdk.models.common import AlbumUserRole, AssetOrder, BulkIdErrorReason
from immich_sdk.models.user import UserResponseDto


class AlbumUserResponseDto(BaseModel):
    """Album user in response (role + user)."""

    role: AlbumUserRole = Field(..., description="Album user role")
    user: UserResponseDto = Field(..., description="User")


class ContributorCountResponseDto(BaseModel):
    """Contributor count in album."""

    assetCount: int = Field(..., description="Number of assets contributed")
    userId: str = Field(..., description="User ID")


class AlbumUserCreateDto(BaseModel):
    """DTO for adding a user to an album. Uses :class:`AlbumUserRole` for role."""

    userId: UUID = Field(..., description="User ID")
    role: AlbumUserRole = Field(..., description="Album user role")


class AlbumUserAddDto(BaseModel):
    """DTO for adding a user to an album (with optional role). Uses :class:`AlbumUserRole`."""

    userId: UUID = Field(..., description="User ID")
    role: AlbumUserRole = Field(AlbumUserRole.EDITOR, description="Album user role")


class AddUsersDto(BaseModel):
    """DTO for sharing an album with users. Uses :class:`AlbumUserAddDto` for each user."""

    albumUsers: list[AlbumUserAddDto] = Field(
        ..., min_length=1, description="Album users to add"
    )


class UpdateAlbumUserDto(BaseModel):
    """DTO for updating a user's role in an album. Uses :class:`AlbumUserRole`."""

    role: AlbumUserRole = Field(..., description="Album user role")


class AlbumsAddAssetsDto(BaseModel):
    """DTO for adding assets to multiple albums."""

    albumIds: list[UUID] = Field(..., description="Album IDs")
    assetIds: list[UUID] = Field(..., description="Asset IDs")


class AlbumsAddAssetsResponseDto(BaseModel):
    """Response for adding assets to multiple albums."""

    success: bool = Field(..., description="Operation success")
    error: BulkIdErrorReason | None = Field(None, description="Error reason if failed")


class AlbumStatisticsResponseDto(BaseModel):
    """Album statistics response DTO."""

    owned: int = Field(..., description="Number of owned albums")
    shared: int = Field(..., description="Number of shared albums")
    notShared: int = Field(..., description="Number of non-shared albums")


class CreateAlbumDto(BaseModel):
    """DTO for creating an album. Optional :class:`AlbumUserCreateDto` for shared users."""

    albumName: str = Field(..., description="Album name")
    description: str | None = Field(None, description="Album description")
    albumUsers: list[AlbumUserCreateDto] | None = Field(None, description="Album users")
    assetIds: list[UUID] | None = Field(None, description="Initial asset IDs")


class UpdateAlbumDto(BaseModel):
    """DTO for updating an album. Uses :class:`AssetOrder` for sort order."""

    albumName: str | None = Field(None, description="Album name")
    description: str | None = Field(None, description="Album description")
    albumThumbnailAssetId: UUID | None = Field(
        None, description="Album thumbnail asset ID"
    )
    isActivityEnabled: bool | None = Field(None, description="Enable activity feed")
    order: AssetOrder | None = Field(None, description="Asset sort order")


_AlbumUserList: TypeAlias = list[AlbumUserResponseDto]
_AssetList: TypeAlias = list[AssetResponseDto]
_ContributorCountList: TypeAlias = list[ContributorCountResponseDto]


class AlbumResponseDto(BaseModel):
    """Album response DTO."""

    id: str = Field(..., description="Album ID")
    albumName: str = Field(..., description="Album name")
    description: str = Field(..., description="Album description")
    albumThumbnailAssetId: str | None = Field(None, description="Thumbnail asset ID")
    albumUsers: _AlbumUserList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list, description="Album users"
    )
    assetCount: int = Field(..., description="Number of assets")
    assets: _AssetList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list, description="Assets"
    )
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    ownerId: str = Field(..., description="Owner user ID")
    owner: UserResponseDto | None = Field(None, description="Owner")
    shared: bool = Field(..., description="Is shared album")
    hasSharedLink: bool = Field(..., description="Has shared link")
    isActivityEnabled: bool = Field(..., description="Activity feed enabled")
    startDate: str | None = Field(None, description="Start date (earliest asset)")
    endDate: str | None = Field(None, description="End date (latest asset)")
    lastModifiedAssetTimestamp: str | None = Field(
        None, description="Last modified asset timestamp"
    )
    order: str | None = Field(None, description="Asset sort order")
    contributorCounts: _ContributorCountList = (
        Field(  # pyright: ignore[reportUnknownVariableType]
            default_factory=list, description="Contributor counts"
        )
    )
