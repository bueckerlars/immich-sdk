"""Map API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class MapClient:
    """Client for Immich Map endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the map client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_map_markers(
        self,
        *,
        file_created_after: str | None = None,
        file_created_before: str | None = None,
        is_archived: bool | None = None,
        is_favorite: bool | None = None,
        with_partners: bool | None = None,
        with_shared_albums: bool | None = None,
    ) -> list[dict[str, object]]:
        """Retrieve latitude/longitude coordinates for every asset with location data.

        :param file_created_after: Optional filter: assets created after this date.
        :param file_created_before: Optional filter: assets created before this date.
        :param is_archived: Optional filter for archived assets.
        :param is_favorite: Optional filter for favorite assets.
        :param with_partners: Optional: include partner assets.
        :param with_shared_albums: Optional: include shared album assets.
        :returns: List of marker dicts.
        """
        params: dict[str, str | bool] = {}
        if file_created_after is not None:
            params["fileCreatedAfter"] = file_created_after
        if file_created_before is not None:
            params["fileCreatedBefore"] = file_created_before
        if is_archived is not None:
            params["isArchived"] = is_archived
        if is_favorite is not None:
            params["isFavorite"] = is_favorite
        if with_partners is not None:
            params["withPartners"] = with_partners
        if with_shared_albums is not None:
            params["withSharedAlbums"] = with_shared_albums
        resp = self._base.get("/api/map/markers", params=params or None)
        return resp.json()

    def reverse_geocode(self, lat: float, lon: float) -> list[dict[str, object]]:
        """Retrieve location information for given latitude and longitude coordinates.

        :param lat: Latitude.
        :param lon: Longitude.
        :returns: List of location dicts.
        """
        resp = self._base.get(
            "/api/map/reverse-geocode", params={"lat": lat, "lon": lon}
        )
        return resp.json()
