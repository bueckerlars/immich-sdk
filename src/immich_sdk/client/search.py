"""Search API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class SearchClient:
    """Client for Immich Search endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the search client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def search_assets(self, dto: dict[str, object]) -> dict[str, object]:
        """Search assets with filters.

        :param dto: Dict with search filters.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/search/assets", json=dto)
        return resp.json()

    def search_places(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Search places (cities, etc.).

        :param dto: Dict with search filters.
        :returns: List of place dicts.
        """
        resp = self._base.post("/api/search/places", json=dto)
        return resp.json()

    def search_people(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Search people.

        :param dto: Dict with search filters.
        :returns: List of person dicts.
        """
        resp = self._base.post("/api/search/people", json=dto)
        return resp.json()

    def search_smart(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Smart search.

        :param dto: Dict with search query.
        :returns: List of result dicts.
        """
        resp = self._base.post("/api/search/smart", json=dto)
        return resp.json()

    def search_metadata(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Search metadata.

        :param dto: Dict with search filters.
        :returns: List of metadata dicts.
        """
        resp = self._base.post("/api/search/metadata", json=dto)
        return resp.json()

    def get_explore_data(self) -> list[dict[str, object]]:
        """Get explore data.

        :returns: List of explore dicts.
        """
        resp = self._base.get("/api/search/explore")
        return resp.json()

    def get_time_buckets(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Get time buckets for timeline.

        :param dto: Dict with time bucket options.
        :returns: List of time bucket dicts.
        """
        resp = self._base.post("/api/search/time-bucket", json=dto)
        return resp.json()
