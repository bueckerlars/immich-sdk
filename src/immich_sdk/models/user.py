"""User-related DTOs."""

from pydantic import BaseModel, Field


class UserResponseDto(BaseModel):
    """User response DTO."""

    id: str = Field(..., description="User ID")
    email: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    avatarColor: str = Field(..., description="Avatar color")
    profileImagePath: str = Field(..., description="Profile image path")
    profileChangedAt: str = Field(..., description="Profile change date")
