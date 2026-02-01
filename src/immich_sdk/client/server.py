"""Server API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class ServerClient:
    """Client for Immich Server endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the server client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_server_version(self) -> dict[str, object]:
        """Get server version.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/server/version")
        return resp.json()

    def get_server_features(self) -> dict[str, object]:
        """Get server features.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/server/features")
        return resp.json()

    def get_server_config(self) -> dict[str, object]:
        """Get server config.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/server/config")
        return resp.json()

    def get_server_statistics(self) -> dict[str, object]:
        """Get server statistics.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/server/statistics")
        return resp.json()
