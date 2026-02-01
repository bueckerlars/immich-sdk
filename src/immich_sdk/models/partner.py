"""Partner-related DTOs."""

from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.user import UserAvatarColor


class PartnerDirection(str, Enum):
    """Partner direction."""

    SHARED_BY = "shared-by"
    SHARED_WITH = "shared-with"


class PartnerCreateDto(BaseModel):
    """DTO for creating a partner."""

    sharedWithId: UUID = Field(..., description="User ID to share with")


class PartnerUpdateDto(BaseModel):
    """DTO for updating a partner."""

    inTimeline: bool = Field(..., description="Show partner assets in timeline")


class PartnerResponseDto(BaseModel):
    """Partner response DTO."""

    id: str = Field(..., description="User ID")
    email: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    avatarColor: UserAvatarColor | str = Field(..., description="Avatar color")
    profileImagePath: str = Field(..., description="Profile image path")
    profileChangedAt: str = Field(..., description="Profile change date")
    inTimeline: bool | None = Field(None, description="Show in timeline")
