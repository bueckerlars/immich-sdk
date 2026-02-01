"""System metadata API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class SystemMetadataClient:
    """Client for Immich System metadata endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the system metadata client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_system_metadata(self) -> dict[str, object]:
        """Get system metadata.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/system-metadata")
        return resp.json()
