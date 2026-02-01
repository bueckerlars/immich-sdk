"""Map-related DTOs."""

from pydantic import BaseModel, Field


class MapMarkerResponseDto(BaseModel):
    """Map marker (asset location) response."""

    id: str = Field(..., description="Asset ID")
    lat: float = Field(..., description="Latitude")
    lon: float = Field(..., description="Longitude")
    city: str | None = Field(None, description="City name")
    state: str | None = Field(None, description="State/Province name")
    country: str | None = Field(None, description="Country name")


class MapReverseGeocodeResponseDto(BaseModel):
    """Reverse geocode result (location info for lat/lon)."""

    city: str | None = Field(None, description="City name")
    state: str | None = Field(None, description="State/Province name")
    country: str | None = Field(None, description="Country name")
