"""Person-related DTOs."""

from uuid import UUID

from pydantic import BaseModel, Field


class PersonCreateDto(BaseModel):
    """DTO for creating a person."""

    name: str = Field(..., description="Person name")
    birthDate: str | None = Field(None, description="Person date of birth")
    color: str | None = Field(None, description="Person color (hex)")
    isFavorite: bool | None = Field(None, description="Mark as favorite")
    isHidden: bool | None = Field(None, description="Person visibility (hidden)")


class PersonUpdateDto(BaseModel):
    """DTO for updating a person."""

    birthDate: str | None = Field(None, description="Person date of birth")
    color: str | None = Field(None, description="Person color (hex)")
    featureFaceAssetId: UUID | None = Field(
        None, description="Asset ID for feature face thumbnail"
    )
    isFavorite: bool | None = Field(None, description="Mark as favorite")
    isHidden: bool | None = Field(None, description="Is hidden")
    name: str | None = Field(None, description="Person name")


class PersonResponseDto(BaseModel):
    """Person response DTO."""

    id: str = Field(..., description="Person ID")
    name: str = Field(..., description="Person name")
    thumbnailPath: str = Field(..., description="Thumbnail path")
    isHidden: bool = Field(..., description="Is hidden")
    birthDate: str | None = Field(None, description="Person date of birth")
    color: str | None = Field(None, description="Person color (hex)")
    isFavorite: bool | None = Field(None, description="Is favorite")
    updatedAt: str | None = Field(None, description="Last update date")


class PersonStatisticsResponseDto(BaseModel):
    """Person statistics response."""

    assets: int = Field(..., description="Number of assets")


class MergePersonDto(BaseModel):
    """DTO for merging persons."""

    ids: list[UUID] = Field(..., description="Person IDs to merge")
