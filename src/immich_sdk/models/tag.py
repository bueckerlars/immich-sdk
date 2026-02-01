"""Tag-related DTOs."""

from uuid import UUID

from pydantic import BaseModel, Field


class TagMergeDto(BaseModel):
    """DTO for merging multiple tags into one (target tag is path param)."""

    ids: list[UUID] = Field(..., description="Source tag IDs to merge into target")


class TagCreateDto(BaseModel):
    """DTO for creating a tag."""

    name: str = Field(..., description="Tag name")
    color: str | None = Field(None, description="Tag color (hex)")
    parentId: UUID | None = Field(None, description="Parent tag ID")


class TagUpdateDto(BaseModel):
    """DTO for updating a tag."""

    color: str | None = Field(None, description="Tag color (hex)")


class TagResponseDto(BaseModel):
    """Tag response DTO."""

    id: str = Field(..., description="Tag ID")
    name: str = Field(..., description="Tag name")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    value: str = Field(..., description="Tag value (full path)")
    color: str | None = Field(None, description="Tag color (hex)")
    parentId: str | None = Field(None, description="Parent tag ID")
