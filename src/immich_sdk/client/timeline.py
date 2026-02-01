"""Timeline API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.search import TimeBucketsResponseDto
from immich_sdk.models.timeline import TimelineBucketRequestDto


class TimelineClient:
    """Client for Immich Timeline endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the timeline client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_time_buckets(
        self, dto: TimelineBucketRequestDto
    ) -> list[TimeBucketsResponseDto]:
        """Get time buckets for timeline.

        :param dto: Time bucket request options.
        :returns: List of time bucket DTOs.
        """
        resp = self._base.post(
            "/api/timeline/bucket",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return [TimeBucketsResponseDto.model_validate(b) for b in resp.json()]
