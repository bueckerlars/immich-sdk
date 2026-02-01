"""Duplicate-related DTOs."""

from pydantic import BaseModel, Field

from immich_sdk.models.asset import AssetResponseDto


class DuplicateResponseDto(BaseModel):
    """Duplicate group response."""

    duplicateId: str = Field(..., description="Duplicate group ID")
    assets: list[AssetResponseDto] = Field(..., description="Duplicate assets")
