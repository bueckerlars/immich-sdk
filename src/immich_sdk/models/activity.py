"""Activity-related DTOs."""

from uuid import UUID

from pydantic import BaseModel, Field


class ReactionType(str):
    """Activity type: like or comment."""

    pass


class ActivityCreateDto(BaseModel):
    """DTO for creating an activity (like or comment)."""

    albumId: UUID = Field(..., description="Album ID")
    type: str = Field(..., description="Activity type (like or comment)")
    assetId: UUID | None = Field(
        None, description="Asset ID (if activity is for an asset)"
    )
    comment: str | None = Field(
        None, description="Comment text (required if type is comment)"
    )


class ActivityResponseDto(BaseModel):
    """Activity response DTO."""

    id: str = Field(..., description="Activity ID")
    assetId: str | None = Field(
        None, description="Asset ID (if activity is for an asset)"
    )
    comment: str | None = Field(
        None, description="Comment text (for comment activities)"
    )
    createdAt: str = Field(..., description="Creation date")
    type: str = Field(..., description="Activity type")
    user: dict[str, object] = Field(..., description="User who created the activity")


class ActivityStatisticsResponseDto(BaseModel):
    """Activity statistics response DTO."""

    likes: int = Field(..., description="Number of likes")
    comments: int = Field(..., description="Number of comments")
