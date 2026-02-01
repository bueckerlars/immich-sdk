"""System metadata DTOs."""

from pydantic import BaseModel, ConfigDict, Field


class SystemMetadataResponseDto(BaseModel):
    """System metadata response (structure may vary; root GET /system-metadata)."""

    model_config = ConfigDict(extra="allow")


class AdminOnboardingUpdateDto(BaseModel):
    """Admin onboarding status (GET /system-metadata/admin-onboarding)."""

    isOnboarded: bool = Field(..., description="Is admin onboarded")


class ReverseGeocodingStateResponseDto(BaseModel):
    """Reverse geocoding import state (GET /system-metadata/reverse-geocoding-state)."""

    lastImportFileName: str | None = Field(None, description="Last import file name")
    lastUpdate: str | None = Field(None, description="Last update timestamp")


class VersionCheckStateResponseDto(BaseModel):
    """Version check state (GET /system-metadata/version-check-state)."""

    checkedAt: str | None = Field(None, description="Last check timestamp")
    releaseVersion: str | None = Field(None, description="Release version")
