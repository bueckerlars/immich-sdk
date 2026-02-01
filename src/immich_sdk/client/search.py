"""Search API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    MetadataSearchDto,
    PlacesResponseDto,
    SearchExploreResponseDto,
    SearchResponseDto,
    SmartSearchDto,
    TimeBucketsResponseDto,
)
from immich_sdk.models.person import PersonResponseDto


class SearchClient:
    """Client for Immich Search endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the search client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def search_assets(self, dto: MetadataSearchDto) -> SearchResponseDto:
        """Search assets with filters.

        :param dto: :class:`MetadataSearchDto` with search filters.
        :returns: :class:`SearchResponseDto` (albums + assets).
        """
        resp = self._base.post(
            "/api/search/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return SearchResponseDto.model_validate(resp.json())

    def search_places(self, dto: MetadataSearchDto) -> list[PlacesResponseDto]:
        """Search places (cities, etc.).

        :param dto: :class:`MetadataSearchDto` with search filters.
        :returns: List of place DTOs.
        """
        resp = self._base.post(
            "/api/search/places",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return [PlacesResponseDto.model_validate(p) for p in resp.json()]

    def search_people(self, dto: MetadataSearchDto) -> list[PersonResponseDto]:
        """Search people.

        :param dto: :class:`MetadataSearchDto` with search filters.
        :returns: List of person DTOs.
        """
        resp = self._base.post(
            "/api/search/people",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return [PersonResponseDto.model_validate(p) for p in resp.json()]

    def search_smart(self, dto: SmartSearchDto) -> SearchResponseDto:
        """Smart search (ML-based asset search).

        :param dto: :class:`SmartSearchDto` with query and filters.
        :returns: :class:`SearchResponseDto` (albums + assets).
        """
        resp = self._base.post(
            "/api/search/smart",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return SearchResponseDto.model_validate(resp.json())

    def search_metadata(self, dto: MetadataSearchDto) -> SearchResponseDto:
        """Search assets by metadata (same as search_assets).

        :param dto: :class:`MetadataSearchDto` with search filters.
        :returns: :class:`SearchResponseDto` (albums + assets).
        """
        resp = self._base.post(
            "/api/search/metadata",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return SearchResponseDto.model_validate(resp.json())

    def get_explore_data(self) -> list[SearchExploreResponseDto]:
        """Get explore data.

        :returns: List of :class:`SearchExploreResponseDto`.
        """
        resp = self._base.get("/api/search/explore")
        data = resp.json()
        return [SearchExploreResponseDto.model_validate(item) for item in data]

    def get_time_buckets(self, dto: MetadataSearchDto) -> list[TimeBucketsResponseDto]:
        """Get time buckets for timeline.

        :param dto: :class:`MetadataSearchDto` with time bucket options.
        :returns: List of :class:`TimeBucketsResponseDto`.
        """
        resp = self._base.post(
            "/api/search/time-bucket",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        data = resp.json()
        return [TimeBucketsResponseDto.model_validate(item) for item in data]
