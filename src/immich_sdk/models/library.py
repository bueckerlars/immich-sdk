"""Library-related DTOs."""

from __future__ import annotations

from typing import TypeAlias
from uuid import UUID

from pydantic import BaseModel, Field


class CreateLibraryDto(BaseModel):
    """DTO for creating a library."""

    ownerId: UUID = Field(..., description="Owner user ID")
    name: str | None = Field(None, description="Library name")
    importPaths: list[str] | None = Field(None, description="Import paths (max 128)")
    exclusionPatterns: list[str] | None = Field(
        None, description="Exclusion patterns (max 128)"
    )


class UpdateLibraryDto(BaseModel):
    """DTO for updating a library."""

    name: str | None = Field(None, description="Library name")
    importPaths: list[str] | None = Field(None, description="Import paths (max 128)")
    exclusionPatterns: list[str] | None = Field(
        None, description="Exclusion patterns (max 128)"
    )


class LibraryResponseDto(BaseModel):
    """Library response DTO."""

    id: str = Field(..., description="Library ID")
    name: str = Field(..., description="Library name")
    ownerId: str = Field(..., description="Owner user ID")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    assetCount: int = Field(..., description="Number of assets")
    importPaths: list[str] = Field(..., description="Import paths")
    exclusionPatterns: list[str] = Field(..., description="Exclusion patterns")
    refreshedAt: str | None = Field(None, description="Last refresh date")


class LibraryStatsResponseDto(BaseModel):
    """Library statistics response."""

    photos: int = Field(0, description="Number of photos")
    videos: int = Field(0, description="Number of videos")
    total: int = Field(0, description="Total number of assets")
    usage: int = Field(0, description="Storage usage in bytes")


class ValidateLibraryImportPathResponseDto(BaseModel):
    """Validation result for a single library import path."""

    importPath: str = Field(..., description="Import path")
    isValid: bool = Field(..., description="Is valid")
    message: str | None = Field(None, description="Validation message")


_ImportPathResultList: TypeAlias = list[ValidateLibraryImportPathResponseDto]


class ValidateLibraryDto(BaseModel):
    """DTO for validating library settings."""

    importPaths: list[str] | None = Field(
        None, description="Import paths to validate (max 128)"
    )
    exclusionPatterns: list[str] | None = Field(
        None, description="Exclusion patterns (max 128)"
    )


class ValidateLibraryResponseDto(BaseModel):
    """Response for library validation."""

    importPaths: _ImportPathResultList = (
        Field(  # pyright: ignore[reportUnknownVariableType]
            default_factory=list,
            description="Validation results for import paths",
        )
    )
