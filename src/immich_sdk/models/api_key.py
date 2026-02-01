"""API key-related DTOs."""

from pydantic import BaseModel, Field


class APIKeyCreateDto(BaseModel):
    """DTO for creating an API key."""

    name: str | None = Field(None, description="API key name")
    permissions: list[str] = Field(..., min_length=1, description="List of permissions")


class APIKeyUpdateDto(BaseModel):
    """DTO for updating an API key."""

    name: str | None = Field(None, description="API key name")
    permissions: list[str] | None = Field(
        None, min_length=1, description="List of permissions"
    )


class APIKeyResponseDto(BaseModel):
    """API key response DTO."""

    id: str = Field(..., description="API key ID")
    name: str = Field(..., description="API key name")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    permissions: list[str] = Field(..., description="List of permissions")


class APIKeyCreateResponseDto(BaseModel):
    """Response after creating an API key (includes secret once). Contains :class:`APIKeyResponseDto`."""

    apiKey: APIKeyResponseDto = Field(..., description="API key metadata")
    secret: str = Field(..., description="API key secret (only shown once)")
