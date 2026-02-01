"""User admin and session DTOs."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from immich_sdk.models.user import UserAvatarColor


class UserLicense(BaseModel):
    """User license info."""

    activatedAt: str = Field(..., description="Activation date")
    activationKey: str = Field(..., description="Activation key")
    licenseKey: str = Field(..., description="License key")


class UserStatus(str, Enum):
    """User status."""

    ACTIVE = "active"
    REMOVING = "removing"
    DELETED = "deleted"


class UserAdminCreateDto(BaseModel):
    """DTO for creating a user (admin)."""

    email: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    password: str = Field(..., description="User password")
    avatarColor: UserAvatarColor | str | None = Field(None, description="Avatar color")
    isAdmin: bool | None = Field(None, description="Grant admin privileges")
    notify: bool | None = Field(None, description="Send notification email")
    quotaSizeInBytes: int | None = Field(None, description="Storage quota in bytes")
    shouldChangePassword: bool | None = Field(
        None, description="Require password change on next login"
    )
    storageLabel: str | None = Field(None, description="Storage label")


class UserAdminUpdateDto(BaseModel):
    """DTO for updating a user (admin)."""

    email: str | None = Field(None, description="User email")
    name: str | None = Field(None, description="User name")
    password: str | None = Field(None, description="User password")
    avatarColor: UserAvatarColor | str | None = Field(None, description="Avatar color")
    isAdmin: bool | None = Field(None, description="Grant admin privileges")
    pinCode: str | None = Field(None, description="PIN code")
    quotaSizeInBytes: int | None = Field(None, description="Storage quota in bytes")
    shouldChangePassword: bool | None = Field(
        None, description="Require password change on next login"
    )
    storageLabel: str | None = Field(None, description="Storage label")


class UserAdminDeleteDto(BaseModel):
    """DTO for user deletion (admin)."""

    force: bool | None = Field(None, description="Force delete even if user has assets")


class UserAdminResponseDto(BaseModel):
    """User response (admin)."""

    id: str = Field(..., description="User ID")
    email: str = Field(..., description="User email")
    name: str = Field(..., description="User name")
    avatarColor: UserAvatarColor | str = Field(..., description="Avatar color")
    profileImagePath: str = Field(..., description="Profile image path")
    profileChangedAt: str = Field(..., description="Profile change date")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    deletedAt: str | None = Field(None, description="Deletion date")
    isAdmin: bool = Field(..., description="Is admin user")
    oauthId: str = Field(..., description="OAuth ID")
    quotaSizeInBytes: int | None = Field(None, description="Storage quota in bytes")
    quotaUsageInBytes: int | None = Field(None, description="Storage usage in bytes")
    shouldChangePassword: bool = Field(
        ..., description="Require password change on next login"
    )
    status: UserStatus | str = Field(..., description="User status")
    storageLabel: str | None = Field(None, description="Storage label")
    license: UserLicense | None = Field(None, description="User license")


class SessionResponseDto(BaseModel):
    """Session response."""

    id: str = Field(..., description="Session ID")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    current: bool = Field(..., description="Is current session")
    deviceOS: str = Field(..., description="Device OS")
    deviceType: str = Field(..., description="Device type")
    appVersion: str | None = Field(None, description="App version")
    expiresAt: str | None = Field(None, description="Expiration date")
    isPendingSyncReset: bool = Field(..., description="Is pending sync reset")


class UserPreferencesResponseDto(BaseModel):
    """User preferences response (nested structure varies)."""

    model_config = ConfigDict(extra="allow")


class UserPreferencesUpdateDto(BaseModel):
    """User preferences update (nested structure varies)."""

    model_config = ConfigDict(extra="allow")


class UserStatisticsResponseDto(BaseModel):
    """User asset statistics (admin)."""

    model_config = ConfigDict(extra="allow")
