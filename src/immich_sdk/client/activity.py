"""Activities API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import (
    ActivityCreateDto,
    ActivityResponseDto,
    ActivityStatisticsResponseDto,
)
from immich_sdk.client._base import BaseClient


class ActivitiesClient:
    """Client for Immich Activities endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the activities client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_activities(
        self,
        album_id: UUID | str,
        *,
        asset_id: UUID | str | None = None,
        level: str | None = None,
        type_filter: str | None = None,
        user_id: UUID | str | None = None,
    ) -> list[ActivityResponseDto]:
        """Return a list of activities for the selected asset or album.

        :param album_id: Album ID (UUID or string).
        :param asset_id: Optional asset ID to filter by.
        :param level: Optional activity level filter.
        :param type_filter: Optional type filter (e.g. like, comment).
        :param user_id: Optional user ID to filter by.
        :returns: List of :class:`ActivityResponseDto`.
        """
        params: dict[str, str] = {"albumId": str(album_id)}
        if asset_id is not None:
            params["assetId"] = str(asset_id)
        if level is not None:
            params["level"] = level
        if type_filter is not None:
            params["type"] = type_filter
        if user_id is not None:
            params["userId"] = str(user_id)
        resp = self._base.get("/api/activities", params=params)
        data = resp.json()
        return [ActivityResponseDto.model_validate(item) for item in data]

    def create_activity(self, dto: ActivityCreateDto) -> ActivityResponseDto:
        """Create a like or a comment for an album, or an asset in an album.

        :param dto: :class:`ActivityCreateDto` with album, type, and optional comment.
        :returns: The created :class:`ActivityResponseDto`.
        """
        resp = self._base.post(
            "/api/activities", json=dto.model_dump(mode="json", exclude_none=True)
        )
        return ActivityResponseDto.model_validate(resp.json())

    def get_activity_statistics(
        self,
        album_id: UUID | str,
        *,
        asset_id: UUID | str | None = None,
    ) -> ActivityStatisticsResponseDto:
        """Return the number of likes and comments for a given album or asset in an album.

        :param album_id: Album ID (UUID or string).
        :param asset_id: Optional asset ID to filter by.
        :returns: :class:`ActivityStatisticsResponseDto`.
        """
        params: dict[str, str] = {"albumId": str(album_id)}
        if asset_id is not None:
            params["assetId"] = str(asset_id)
        resp = self._base.get("/api/activities/statistics", params=params)
        return ActivityStatisticsResponseDto.model_validate(resp.json())

    def delete_activity(self, activity_id: UUID | str) -> None:
        """Remove a like or comment from a given album or asset in an album.

        :param activity_id: Activity ID (UUID or string).
        """
        self._base.delete(f"/api/activities/{activity_id}")
