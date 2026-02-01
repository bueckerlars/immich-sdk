"""Memory-related DTOs."""

from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.asset import AssetResponseDto


class MemoryType(str, Enum):
    """Memory type."""

    ON_THIS_DAY = "on_this_day"


class MemorySearchOrder(str, Enum):
    """Memory search order."""

    ASC = "asc"
    DESC = "desc"
    RANDOM = "random"


class OnThisDayDto(BaseModel):
    """On this day memory data."""

    year: int = Field(..., ge=1, description="Year for on this day memory")


class MemoryCreateDto(BaseModel):
    """DTO for creating a memory."""

    type: MemoryType = Field(..., description="Memory type")
    memoryAt: str = Field(..., description="Memory date")
    data: OnThisDayDto = Field(
        ..., description="Memory data (e.g. year for on_this_day)"
    )
    assetIds: list[UUID] | None = Field(None, description="Asset IDs to associate")
    isSaved: bool | None = Field(None, description="Is memory saved")
    seenAt: str | None = Field(None, description="Date when memory was seen")


class MemoryUpdateDto(BaseModel):
    """DTO for updating a memory."""

    isSaved: bool | None = Field(None, description="Is memory saved")
    memoryAt: str | None = Field(None, description="Memory date")
    seenAt: str | None = Field(None, description="Date when memory was seen")


class MemoryResponseDto(BaseModel):
    """Memory response DTO."""

    id: str = Field(..., description="Memory ID")
    type: MemoryType = Field(..., description="Memory type")
    memoryAt: str = Field(..., description="Memory date")
    ownerId: str = Field(..., description="Owner user ID")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    isSaved: bool = Field(..., description="Is memory saved")
    assets: list[AssetResponseDto] = Field(..., description="Assets")
    data: OnThisDayDto | dict[str, Any] | None = Field(None, description="Memory data")
    deletedAt: str | None = Field(None, description="Deletion date")
    hideAt: str | None = Field(None, description="Date when memory should be hidden")
    seenAt: str | None = Field(None, description="Date when memory was seen")
    showAt: str | None = Field(None, description="Date when memory should be shown")


class MemoryStatisticsResponseDto(BaseModel):
    """Memory statistics response."""

    total: int = Field(..., description="Total number of memories")
