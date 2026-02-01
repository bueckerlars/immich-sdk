"""Face-related DTOs."""

from __future__ import annotations

from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.person import PersonResponseDto


class FaceDto(BaseModel):
    """DTO containing a face ID (e.g. for reassignment)."""

    id: UUID | str = Field(..., description="Face ID")


class SourceType(str, Enum):
    """Face detection source type."""

    MACHINE_LEARNING = "machine-learning"
    EXIF = "exif"
    MANUAL = "manual"


class AssetFaceCreateDto(BaseModel):
    """DTO for creating a face (manual face creation)."""

    assetId: UUID | str = Field(..., description="Asset ID")
    personId: UUID | str = Field(..., description="Person ID")
    height: int = Field(..., description="Face bounding box height")
    imageHeight: int = Field(..., description="Image height in pixels")
    imageWidth: int = Field(..., description="Image width in pixels")
    width: int = Field(..., description="Face bounding box width")
    x: int = Field(..., description="Face bounding box X coordinate")
    y: int = Field(..., description="Face bounding box Y coordinate")


class AssetFaceDeleteDto(BaseModel):
    """DTO for face deletion (optional force)."""

    force: bool = Field(
        False, description="Force delete even if person has other faces"
    )


class AssetFaceWithoutPersonResponseDto(BaseModel):
    """Face response without person (e.g. for asset faces list)."""

    id: str = Field(..., description="Face ID")
    boundingBoxX1: int = Field(..., description="Bounding box X1 coordinate")
    boundingBoxX2: int = Field(..., description="Bounding box X2 coordinate")
    boundingBoxY1: int = Field(..., description="Bounding box Y1 coordinate")
    boundingBoxY2: int = Field(..., description="Bounding box Y2 coordinate")
    imageHeight: int = Field(..., description="Image height in pixels")
    imageWidth: int = Field(..., description="Image width in pixels")
    sourceType: SourceType = Field(..., description="Face detection source type")


class AssetFaceResponseDto(BaseModel):
    """Face response with optional person."""

    id: str = Field(..., description="Face ID")
    boundingBoxX1: int = Field(..., description="Bounding box X1 coordinate")
    boundingBoxX2: int = Field(..., description="Bounding box X2 coordinate")
    boundingBoxY1: int = Field(..., description="Bounding box Y1 coordinate")
    boundingBoxY2: int = Field(..., description="Bounding box Y2 coordinate")
    imageHeight: int = Field(..., description="Image height in pixels")
    imageWidth: int = Field(..., description="Image width in pixels")
    person: PersonResponseDto | None = Field(
        None, description="Person associated with face"
    )
    sourceType: SourceType | None = Field(
        None, description="Face detection source type"
    )


class AssetFaceUpdateItem(BaseModel):
    """Single face reassignment item."""

    assetId: UUID | str = Field(..., description="Asset ID")
    personId: UUID | str = Field(..., description="Person ID")


class AssetFaceUpdateDto(BaseModel):
    """DTO for bulk face reassignment."""

    data: list[AssetFaceUpdateItem] = Field(..., description="Face update items")
