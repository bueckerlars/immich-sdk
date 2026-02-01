"""User-related DTOs."""

from enum import Enum

from pydantic import BaseModel, Field


class UserAvatarColor(str, Enum):
    """Avatar color."""

    PRIMARY = "primary"
    PINK = "pink"
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"
    PURPLE = "purple"
    ORANGE = "orange"
    GRAY = "gray"
    AMBER = "amber"


class UserResponseDto(BaseModel):
    """User response DTO."""

    id: str = Field(..., description="User ID")
    email: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    avatarColor: UserAvatarColor | str = Field(
        ..., description="Avatar color"
    )  # str for backward compat
    profileImagePath: str = Field(..., description="Profile image path")
    profileChangedAt: str = Field(..., description="Profile change date")


class UserUpdateMeDto(BaseModel):
    """DTO for updating the current user."""

    avatarColor: UserAvatarColor | str | None = Field(None, description="Avatar color")
    email: str | None = Field(None, description="User email")
    name: str | None = Field(None, description="User name")
    password: str | None = Field(
        None,
        description="User password (deprecated, use change password endpoint)",
    )


class CreateProfileImageResponseDto(BaseModel):
    """Response after creating/uploading a profile image."""

    profileChangedAt: str = Field(
        ..., description="Profile image change date (ISO date-time)"
    )
    profileImagePath: str = Field(..., description="Profile image file path")
    userId: str = Field(..., description="User ID")
