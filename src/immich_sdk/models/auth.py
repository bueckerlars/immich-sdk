"""Authentication-related DTOs."""

from pydantic import BaseModel, Field


class LoginCredentialDto(BaseModel):
    """DTO for login credentials."""

    email: str = Field(..., description="User email")
    password: str = Field(..., description="User password")


class LoginResponseDto(BaseModel):
    """DTO for login response."""

    accessToken: str = Field(..., description="Access token")
    userId: str = Field(..., description="User ID")
    userEmail: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    profileImagePath: str = Field(..., description="Profile image path")
    isAdmin: bool = Field(..., description="Is admin user")
    isOnboarded: bool = Field(..., description="Is onboarded")
    shouldChangePassword: bool = Field(..., description="Should change password")


class AuthStatusResponseDto(BaseModel):
    """DTO for auth status response."""

    isElevated: bool = Field(..., description="Is elevated session")
    password: bool = Field(..., description="Has password set")
    pinCode: bool = Field(..., description="Has PIN code set")
    expiresAt: str | None = Field(None, description="Session expiration date")
    pinExpiresAt: str | None = Field(None, description="PIN expiration date")
