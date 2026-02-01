"""Asset-related DTOs."""

from enum import Enum
from typing import Any, TypeAlias
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.user import UserResponseDto

_PeopleList: TypeAlias = list[dict[str, object]]
_TagsList: TypeAlias = list[dict[str, object]]
_UnassignedFacesList: TypeAlias = list[dict[str, object]]


class AssetJobName(str, Enum):
    """Asset job name."""

    REFRESH_FACES = "refresh-faces"
    REFRESH_METADATA = "refresh-metadata"
    REGENERATE_THUMBNAIL = "regenerate-thumbnail"
    TRANSCODE_VIDEO = "transcode-video"


class AssetMediaStatus(str, Enum):
    """Upload status."""

    CREATED = "created"
    REPLACED = "replaced"
    DUPLICATE = "duplicate"


class AssetTypeEnum(str, Enum):
    """Asset type."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    OTHER = "OTHER"


class AssetVisibility(str, Enum):
    """Asset visibility."""

    ARCHIVE = "archive"
    TIMELINE = "timeline"
    HIDDEN = "hidden"
    LOCKED = "locked"


class ExifResponseDto(BaseModel):
    """EXIF metadata response."""

    city: str | None = Field(None, description="City name")
    country: str | None = Field(None, description="Country name")
    dateTimeOriginal: str | None = Field(None, description="Original date/time")
    description: str | None = Field(None, description="Image description")
    exifImageHeight: float | None = Field(None, description="Image height in pixels")
    exifImageWidth: float | None = Field(None, description="Image width in pixels")
    exposureTime: str | None = Field(None, description="Exposure time")
    fNumber: float | None = Field(None, description="F-number (aperture)")
    fileSizeInByte: int | None = Field(None, description="File size in bytes")
    focalLength: float | None = Field(None, description="Focal length in mm")
    iso: float | None = Field(None, description="ISO sensitivity")
    latitude: float | None = Field(None, description="GPS latitude")
    lensModel: str | None = Field(None, description="Lens model")
    longitude: float | None = Field(None, description="GPS longitude")
    make: str | None = Field(None, description="Camera make")
    model: str | None = Field(None, description="Camera model")
    modifyDate: str | None = Field(None, description="Modification date/time")
    orientation: str | None = Field(None, description="Image orientation")
    projectionType: str | None = Field(None, description="Projection type")
    rating: float | None = Field(None, description="Rating")
    state: str | None = Field(None, description="State/province name")
    timeZone: str | None = Field(None, description="Time zone")


class AssetStackResponseDto(BaseModel):
    """Stack info in asset response."""

    assetCount: int = Field(..., description="Number of assets in stack")
    id: str = Field(..., description="Stack ID")
    primaryAssetId: str = Field(..., description="Primary asset ID")


class AssetResponseDto(BaseModel):
    """Asset response DTO."""

    checksum: str = Field(..., description="Base64 encoded SHA1 hash")
    createdAt: str = Field(..., description="Creation date")
    deviceAssetId: str = Field(..., description="Device asset ID")
    deviceId: str = Field(..., description="Device ID")
    duplicateId: str | None = Field(None, description="Duplicate group ID")
    duration: str = Field(..., description="Video duration (for videos)")
    exifInfo: ExifResponseDto | None = Field(None, description="EXIF metadata")
    fileCreatedAt: str = Field(..., description="File creation timestamp")
    fileModifiedAt: str = Field(..., description="File modification timestamp")
    hasMetadata: bool = Field(..., description="Whether asset has metadata")
    height: float | None = Field(None, description="Asset height")
    id: str = Field(..., description="Asset ID")
    isArchived: bool = Field(..., description="Is archived")
    isEdited: bool = Field(..., description="Is edited")
    isFavorite: bool = Field(..., description="Is favorite")
    isOffline: bool = Field(..., description="Is offline")
    isTrashed: bool = Field(..., description="Is trashed")
    libraryId: str | None = Field(None, description="Library ID (deprecated)")
    livePhotoVideoId: str | None = Field(None, description="Live photo video ID")
    localDateTime: str = Field(..., description="Local date/time")
    originalFileName: str = Field(..., description="Original file name")
    originalMimeType: str | None = Field(None, description="Original MIME type")
    originalPath: str = Field(..., description="Original file path")
    owner: UserResponseDto | None = Field(None, description="Owner")
    ownerId: str = Field(..., description="Owner user ID")
    people: _PeopleList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list,
        description="People in asset (PersonWithFacesResponseDto when person models exist)",
    )
    resized: bool | None = Field(None, description="Is resized (deprecated)")
    stack: AssetStackResponseDto | None = Field(None, description="Stack info")
    tags: _TagsList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list,
        description="Tags (TagResponseDto when tag models exist)",
    )
    thumbhash: str | None = Field(None, description="Thumbhash for thumbnail")
    type: AssetTypeEnum = Field(..., description="Asset type")
    unassignedFaces: _UnassignedFacesList = (
        Field(  # pyright: ignore[reportUnknownVariableType]
            default_factory=list,
            description="Unassigned faces",
        )
    )
    updatedAt: str = Field(..., description="Last update date")
    visibility: AssetVisibility = Field(..., description="Asset visibility")
    width: float | None = Field(None, description="Asset width")


class AssetStatsResponseDto(BaseModel):
    """Asset statistics response."""

    images: int = Field(..., description="Number of images")
    total: int = Field(..., description="Total number of assets")
    videos: int = Field(..., description="Number of videos")


class UpdateAssetDto(BaseModel):
    """DTO for updating an asset."""

    dateTimeOriginal: str | None = Field(None, description="Original date and time")
    description: str | None = Field(None, description="Asset description")
    isFavorite: bool | None = Field(None, description="Mark as favorite")
    latitude: float | None = Field(None, description="Latitude coordinate")
    livePhotoVideoId: UUID | str | None = Field(None, description="Live photo video ID")
    longitude: float | None = Field(None, description="Longitude coordinate")
    rating: int | None = Field(None, ge=-1, le=5, description="Rating")
    visibility: AssetVisibility | None = Field(None, description="Asset visibility")


class AssetBulkDeleteDto(BaseModel):
    """DTO for bulk deleting assets."""

    ids: list[UUID] = Field(..., description="IDs to process")
    force: bool | None = Field(None, description="Force delete even if in use")


class AssetBulkUpdateDto(BaseModel):
    """DTO for bulk updating assets."""

    ids: list[UUID] = Field(..., description="Asset IDs to update")
    dateTimeOriginal: str | None = Field(None, description="Original date and time")
    dateTimeRelative: float | None = Field(
        None, description="Relative time offset in seconds"
    )
    description: str | None = Field(None, description="Asset description")
    duplicateId: str | None = Field(None, description="Duplicate asset ID")
    isFavorite: bool | None = Field(None, description="Mark as favorite")
    latitude: float | None = Field(None, description="Latitude coordinate")
    longitude: float | None = Field(None, description="Longitude coordinate")
    rating: int | None = Field(None, ge=-1, le=5, description="Rating")
    timeZone: str | None = Field(None, description="Time zone (IANA timezone)")
    visibility: AssetVisibility | None = Field(None, description="Asset visibility")


class AssetBulkUploadCheckItem(BaseModel):
    """Single item for bulk upload check."""

    checksum: str = Field(..., description="Base64 or hex encoded SHA1 hash")
    id: str = Field(..., description="Asset ID")


class AssetBulkUploadCheckResult(BaseModel):
    """Result of a single bulk upload check."""

    action: str = Field(..., description="Upload action (accept or reject)")
    id: str = Field(..., description="Asset ID")
    assetId: str | None = Field(None, description="Existing asset ID if duplicate")
    isTrashed: bool | None = Field(
        None, description="Whether existing asset is trashed"
    )
    reason: str | None = Field(
        None, description="Rejection reason (duplicate or unsupported-format)"
    )


class AssetBulkUploadCheckDto(BaseModel):
    """DTO for bulk upload check."""

    assets: list[AssetBulkUploadCheckItem] = Field(..., description="Assets to check")


class AssetBulkUploadCheckResponseDto(BaseModel):
    """Response for bulk upload check."""

    results: list[AssetBulkUploadCheckResult] = Field(
        ..., description="Upload check results"
    )


class AssetCopyDto(BaseModel):
    """DTO for copying asset metadata."""

    sourceId: UUID = Field(..., description="Source asset ID")
    targetId: UUID = Field(..., description="Target asset ID")
    albums: bool = Field(True, description="Copy album associations")
    favorite: bool = Field(True, description="Copy favorite status")
    sharedLinks: bool = Field(True, description="Copy shared links")
    sidecar: bool = Field(True, description="Copy sidecar file")
    stack: bool = Field(True, description="Copy stack association")


class CheckExistingAssetsDto(BaseModel):
    """DTO for checking existing assets."""

    deviceAssetIds: list[str] = Field(
        ..., min_length=1, description="Device asset IDs to check"
    )
    deviceId: str = Field(..., description="Device ID")


class CheckExistingAssetsResponseDto(BaseModel):
    """Response for check existing assets."""

    existingIds: list[str] = Field(..., description="Existing asset IDs")


class AssetJobsDto(BaseModel):
    """DTO for running asset jobs."""

    assetIds: list[UUID] = Field(..., description="Asset IDs")
    name: AssetJobName = Field(..., description="Job name")


class AssetMediaResponseDto(BaseModel):
    """Response for asset upload/replace."""

    id: str = Field(..., description="Asset media ID")
    status: AssetMediaStatus = Field(..., description="Upload status")


class AssetMetadataResponseDto(BaseModel):
    """Single asset metadata key-value response."""

    key: str = Field(..., description="Metadata key")
    updatedAt: str = Field(..., description="Last update date")
    value: dict[str, Any] = Field(..., description="Metadata value (object)")


class AssetMetadataUpsertItemDto(BaseModel):
    """Single metadata item to upsert (single asset)."""

    key: str = Field(..., description="Metadata key")
    value: dict[str, Any] = Field(..., description="Metadata value (object)")


class AssetMetadataUpsertDto(BaseModel):
    """Request to upsert metadata for a single asset."""

    items: list[AssetMetadataUpsertItemDto] = Field(
        ..., description="Metadata items to upsert"
    )


class AssetMetadataBulkDeleteItemDto(BaseModel):
    """Single item for bulk metadata delete."""

    assetId: UUID | str = Field(..., description="Asset ID")
    key: str = Field(..., description="Metadata key")


class AssetMetadataBulkDeleteDto(BaseModel):
    """Request to delete metadata for multiple assets."""

    items: list[AssetMetadataBulkDeleteItemDto] = Field(
        ..., description="Metadata items to delete"
    )


class AssetMetadataBulkUpsertItemDto(BaseModel):
    """Single item for bulk metadata upsert."""

    assetId: UUID | str = Field(..., description="Asset ID")
    key: str = Field(..., description="Metadata key")
    value: dict[str, Any] = Field(..., description="Metadata value (object)")


class AssetMetadataBulkUpsertDto(BaseModel):
    """Request to upsert metadata for multiple assets."""

    items: list[AssetMetadataBulkUpsertItemDto] = Field(
        ..., description="Metadata items to upsert"
    )


class AssetMetadataBulkResponseDto(BaseModel):
    """Single item in bulk metadata response."""

    assetId: str = Field(..., description="Asset ID")
    key: str = Field(..., description="Metadata key")
    updatedAt: str = Field(..., description="Last update date")
    value: dict[str, Any] = Field(..., description="Metadata value (object)")


class AssetOcrResponseDto(BaseModel):
    """OCR result for an asset."""

    assetId: str = Field(..., description="Asset ID")
    id: str = Field(..., description="OCR entry ID")
    text: str = Field(..., description="Recognized text")
    boxScore: float = Field(..., description="Confidence score for text detection box")
    textScore: float = Field(..., description="Confidence score for text recognition")
    x1: float = Field(..., description="Normalized x coordinate of box corner 1 (0-1)")
    x2: float = Field(..., description="Normalized x coordinate of box corner 2 (0-1)")
    x3: float = Field(..., description="Normalized x coordinate of box corner 3 (0-1)")
    x4: float = Field(..., description="Normalized x coordinate of box corner 4 (0-1)")
    y1: float = Field(..., description="Normalized y coordinate of box corner 1 (0-1)")
    y2: float = Field(..., description="Normalized y coordinate of box corner 2 (0-1)")
    y3: float = Field(..., description="Normalized y coordinate of box corner 3 (0-1)")
    y4: float = Field(..., description="Normalized y coordinate of box corner 4 (0-1)")
