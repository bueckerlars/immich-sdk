"""Timeline API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class TimelineClient:
    """Client for Immich Timeline endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the timeline client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_time_buckets(self, dto: dict[str, object]) -> list[dict[str, object]]:
        """Get time buckets for timeline.

        :param dto: Dict with time bucket options.
        :returns: List of time bucket dicts.
        """
        resp = self._base.post("/api/timeline/bucket", json=dto)
        return resp.json()
