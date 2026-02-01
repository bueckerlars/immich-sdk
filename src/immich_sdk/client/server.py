"""Server API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    ServerConfigDto,
    ServerFeaturesDto,
    ServerStatsResponseDto,
    ServerVersionResponseDto,
)


class ServerClient:
    """Client for Immich Server endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the server client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_server_version(self) -> ServerVersionResponseDto:
        """Get server version.

        :returns: :class:`ServerVersionResponseDto`.
        """
        resp = self._base.get("/api/server/version")
        return ServerVersionResponseDto.model_validate(resp.json())

    def get_server_features(self) -> ServerFeaturesDto:
        """Get server features.

        :returns: :class:`ServerFeaturesDto`.
        """
        resp = self._base.get("/api/server/features")
        return ServerFeaturesDto.model_validate(resp.json())

    def get_server_config(self) -> ServerConfigDto:
        """Get server config.

        :returns: :class:`ServerConfigDto`.
        """
        resp = self._base.get("/api/server/config")
        return ServerConfigDto.model_validate(resp.json())

    def get_server_statistics(self) -> ServerStatsResponseDto:
        """Get server statistics.

        :returns: :class:`ServerStatsResponseDto`.
        """
        resp = self._base.get("/api/server/statistics")
        return ServerStatsResponseDto.model_validate(resp.json())
