"""Download API client."""

from __future__ import annotations

from immich_sdk.models import AssetIdsDto
from immich_sdk.client._base import BaseClient


class DownloadClient:
    """Client for Immich Download endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the download client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_download_info(
        self,
        dto: dict[str, object],
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> dict[str, object]:
        """Retrieve information about how to request a download for the specified assets or album.

        :param dto: Dict with asset IDs or album ID.
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: Raw response dict from the API.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.post(
            "/api/download/info",
            json=dto,
            params=params or None,
        )
        return resp.json()

    def download_archive(
        self,
        dto: AssetIdsDto,
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> bytes:
        """Download a ZIP archive containing the specified assets.

        :param dto: :class:`AssetIdsDto` with asset IDs.
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: Raw ZIP file bytes.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.post(
            "/api/download/archive",
            json=dto.model_dump(mode="json", exclude_none=True),
            params=params or None,
        )
        return resp.content
