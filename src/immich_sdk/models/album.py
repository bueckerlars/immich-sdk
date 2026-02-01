"""Album-related DTOs."""

from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.common import AlbumUserRole, AssetOrder


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


class AlbumResponseDto(BaseModel):
    """Album response DTO."""

    id: str = Field(..., description="Album ID")
    albumName: str = Field(..., description="Album name")
    description: str = Field(..., description="Album description")
    albumThumbnailAssetId: str | None = Field(None, description="Thumbnail asset ID")
    albumUsers: list[dict[str, object]] = Field(
        default_factory=lambda: [], description="Album users"
    )
    assetCount: int = Field(..., description="Number of assets")
    assets: list[dict[str, object]] = Field(
        default_factory=lambda: [], description="Assets"
    )
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    ownerId: str = Field(..., description="Owner user ID")
    owner: dict[str, object] | None = Field(None, description="Owner")
    shared: bool = Field(..., description="Is shared album")
    hasSharedLink: bool = Field(..., description="Has shared link")
    isActivityEnabled: bool = Field(..., description="Activity feed enabled")
    startDate: str | None = Field(None, description="Start date (earliest asset)")
    endDate: str | None = Field(None, description="End date (latest asset)")
    lastModifiedAssetTimestamp: str | None = Field(
        None, description="Last modified asset timestamp"
    )
    order: str | None = Field(None, description="Asset sort order")
    contributorCounts: list[dict[str, object]] = Field(
        default_factory=lambda: [], description="Contributor counts"
    )
