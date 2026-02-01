"""Search-related DTOs."""

from uuid import UUID

from pydantic import BaseModel, Field

from immich_sdk.models.album import AlbumResponseDto
from immich_sdk.models.asset import (
    AssetResponseDto,
    AssetTypeEnum,
    AssetVisibility,
)
from immich_sdk.models.common import AssetOrder


class SearchFacetCountResponseDto(BaseModel):
    """Facet count in search."""

    count: int = Field(..., description="Number of assets with this facet value")
    value: str = Field(..., description="Facet value")


class SearchFacetResponseDto(BaseModel):
    """Facet in search result."""

    fieldName: str = Field(..., description="Facet field name")
    counts: list[SearchFacetCountResponseDto] = Field(..., description="Facet counts")


class SearchAlbumResponseDto(BaseModel):
    """Album search result page."""

    count: int = Field(..., description="Number of albums in this page")
    facets: list[SearchFacetResponseDto] = Field(..., description="Facets")
    items: list[AlbumResponseDto] = Field(..., description="Albums")
    total: int = Field(..., description="Total number of matching albums")


class SearchAssetResponseDto(BaseModel):
    """Asset search result page."""

    count: int = Field(..., description="Number of assets in this page")
    facets: list[SearchFacetResponseDto] = Field(..., description="Facets")
    items: list[AssetResponseDto] = Field(..., description="Assets")
    nextPage: str | None = Field(None, description="Next page token")
    total: int = Field(..., description="Total number of matching assets")


class SearchResponseDto(BaseModel):
    """Combined search response (albums + assets)."""

    albums: SearchAlbumResponseDto = Field(..., description="Album results")
    assets: SearchAssetResponseDto = Field(..., description="Asset results")


class SearchExploreItem(BaseModel):
    """Single explore item."""

    data: AssetResponseDto = Field(..., description="Asset data")
    value: str = Field(..., description="Explore value")


class SearchExploreResponseDto(BaseModel):
    """Explore search response."""

    fieldName: str = Field(..., description="Explore field name")
    items: list[SearchExploreItem] = Field(..., description="Items")


class SearchStatisticsResponseDto(BaseModel):
    """Search statistics."""

    total: int = Field(..., description="Total number of matching assets")


class TimeBucketsResponseDto(BaseModel):
    """Time bucket for timeline."""

    count: int = Field(..., description="Number of assets in this time bucket")
    timeBucket: str = Field(
        ...,
        description="Time bucket identifier (e.g. YYYY-MM-DD)",
    )


class PlacesResponseDto(BaseModel):
    """Place search result (e.g. city)."""

    name: str = Field(..., description="Place name")
    latitude: float = Field(..., description="Latitude coordinate")
    longitude: float = Field(..., description="Longitude coordinate")
    admin1name: str | None = Field(
        None, description="Administrative level 1 (state/province)"
    )
    admin2name: str | None = Field(
        None, description="Administrative level 2 (county/district)"
    )


class SmartSearchDto(BaseModel):
    """Smart search request (ML-based asset search)."""

    query: str | None = Field(None, description="Natural language search query")
    queryAssetId: UUID | None = Field(
        None, description="Asset ID to use as search reference"
    )
    albumIds: list[UUID] | None = Field(None, description="Filter by album IDs")
    city: str | None = Field(None, description="Filter by city name")
    country: str | None = Field(None, description="Filter by country name")
    createdAfter: str | None = Field(
        None, description="Filter by creation date (after)"
    )
    createdBefore: str | None = Field(
        None, description="Filter by creation date (before)"
    )
    deviceId: str | None = Field(None, description="Device ID to filter by")
    isEncoded: bool | None = Field(None, description="Filter by encoded status")
    isFavorite: bool | None = Field(None, description="Filter by favorite")
    isMotion: bool | None = Field(None, description="Filter by motion photo")
    isNotInAlbum: bool | None = Field(
        None, description="Filter assets not in any album"
    )
    isOffline: bool | None = Field(None, description="Filter by offline")
    language: str | None = Field(None, description="Search language code")
    lensModel: str | None = Field(None, description="Filter by lens model")
    libraryId: UUID | None = Field(None, description="Library ID to filter by")
    make: str | None = Field(None, description="Filter by camera make")
    model: str | None = Field(None, description="Filter by camera model")
    ocr: str | None = Field(None, description="Filter by OCR text content")
    page: int | None = Field(None, ge=1, description="Page number")
    personIds: list[UUID] | None = Field(None, description="Filter by person IDs")
    rating: float | None = Field(None, ge=-1, le=5, description="Filter by rating")
    size: int | None = Field(None, ge=1, le=1000, description="Number of results")
    state: str | None = Field(None, description="Filter by state/province name")
    tagIds: list[UUID] | None = Field(None, description="Filter by tag IDs")
    takenAfter: str | None = Field(None, description="Filter by taken date (after)")
    takenBefore: str | None = Field(None, description="Filter by taken date (before)")
    type: AssetTypeEnum | None = Field(None, description="Asset type filter")
    updatedAfter: str | None = Field(None, description="Filter by update date (after)")
    updatedBefore: str | None = Field(
        None, description="Filter by update date (before)"
    )
    visibility: AssetVisibility | None = Field(None, description="Filter by visibility")
    withDeleted: bool | None = Field(None, description="Include deleted assets")
    withExif: bool | None = Field(None, description="Include EXIF data in response")


class MetadataSearchDto(BaseModel):
    """Search/filter options for assets."""

    albumIds: list[UUID] | None = Field(None, description="Filter by album IDs")
    checksum: str | None = Field(None, description="Filter by file checksum")
    city: str | None = Field(None, description="Filter by city name")
    country: str | None = Field(None, description="Filter by country name")
    createdAfter: str | None = Field(
        None, description="Filter by creation date (after)"
    )
    createdBefore: str | None = Field(
        None, description="Filter by creation date (before)"
    )
    description: str | None = Field(None, description="Filter by description")
    deviceAssetId: str | None = Field(None, description="Filter by device asset ID")
    deviceId: str | None = Field(None, description="Device ID to filter by")
    id: UUID | None = Field(None, description="Filter by asset ID")
    isFavorite: bool | None = Field(None, description="Filter by favorite")
    isNotInAlbum: bool | None = Field(
        None, description="Filter assets not in any album"
    )
    isOffline: bool | None = Field(None, description="Filter by offline")
    libraryId: UUID | None = Field(None, description="Library ID to filter by")
    order: AssetOrder | None = Field(None, description="Sort order (default desc)")
    page: int | None = Field(None, ge=1, description="Page number")
    personIds: list[UUID] | None = Field(None, description="Filter by person IDs")
    size: int | None = Field(None, ge=1, le=1000, description="Number of results")
    tagIds: list[UUID] | None = Field(None, description="Filter by tag IDs")
    type: AssetTypeEnum | None = Field(None, description="Asset type filter")
