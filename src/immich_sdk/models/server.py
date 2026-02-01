"""Server-related DTOs."""

from typing import TypeAlias

from pydantic import BaseModel, Field

_UsageByUserList: TypeAlias = list[dict[str, object]]


class ServerConfigDto(BaseModel):
    """Server config response."""

    externalDomain: str = Field(..., description="External domain URL")
    isInitialized: bool = Field(
        ..., description="Whether the server has been initialized"
    )
    isOnboarded: bool = Field(
        ..., description="Whether the admin has completed onboarding"
    )
    loginPageMessage: str = Field(..., description="Login page message")
    maintenanceMode: bool = Field(..., description="Whether maintenance mode is active")
    mapDarkStyleUrl: str = Field(..., description="Map dark style URL")
    mapLightStyleUrl: str = Field(..., description="Map light style URL")
    oauthButtonText: str = Field(..., description="OAuth button text")
    publicUsers: bool = Field(
        ..., description="Whether public user registration is enabled"
    )
    trashDays: int = Field(
        ...,
        description="Number of days before trashed assets are permanently deleted",
    )
    userDeleteDelay: int = Field(
        ...,
        description="Delay in days before deleted users are permanently removed",
    )


class ServerFeaturesDto(BaseModel):
    """Server features response."""

    configFile: bool = Field(..., description="Whether config file is available")
    duplicateDetection: bool = Field(
        ..., description="Whether duplicate detection is enabled"
    )
    email: bool = Field(..., description="Whether email notifications are enabled")
    facialRecognition: bool = Field(
        ..., description="Whether facial recognition is enabled"
    )
    importFaces: bool = Field(..., description="Whether face import is enabled")
    map: bool = Field(..., description="Whether map feature is enabled")
    oauth: bool = Field(..., description="Whether OAuth is enabled")
    oauthAutoLaunch: bool = Field(
        ..., description="Whether OAuth auto-launch is enabled"
    )
    ocr: bool = Field(..., description="Whether OCR is enabled")
    passwordLogin: bool = Field(..., description="Whether password login is enabled")
    reverseGeocoding: bool = Field(
        ..., description="Whether reverse geocoding is enabled"
    )
    search: bool = Field(..., description="Whether search is enabled")
    sidecar: bool = Field(..., description="Whether sidecar files are supported")
    smartSearch: bool = Field(..., description="Whether smart search is enabled")
    trash: bool = Field(..., description="Whether trash feature is enabled")


class ServerStatsResponseDto(BaseModel):
    """Server statistics response."""

    photos: int = Field(0, description="Total number of photos")
    usage: int = Field(0, description="Total storage usage in bytes")
    usagePhotos: int = Field(0, description="Storage usage for photos in bytes")
    usageVideos: int = Field(0, description="Storage usage for videos in bytes")
    usageByUser: _UsageByUserList = Field(  # pyright: ignore[reportUnknownVariableType]
        default_factory=list, description="Usage per user"
    )


class ServerVersionResponseDto(BaseModel):
    """Server version response."""

    version: str = Field(..., description="Server version")
