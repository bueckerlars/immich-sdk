"""Albums API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import (
    AddUsersDto,
    AlbumResponseDto,
    AlbumStatisticsResponseDto,
    AlbumsAddAssetsDto,
    BulkIdResponseDto,
    BulkIdsDto,
    CreateAlbumDto,
    UpdateAlbumDto,
    UpdateAlbumUserDto,
)
from immich_sdk.client._base import BaseClient


class AlbumsClient:
    """Client for Immich Albums endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the albums client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_all_albums(
        self,
        *,
        asset_id: UUID | None = None,
        shared: bool | None = None,
    ) -> list[AlbumResponseDto]:
        """Retrieve a list of albums available to the authenticated user.

        :param asset_id: Optional asset ID to filter albums containing this asset.
        :param shared: Optional filter for shared albums only.
        :returns: List of :class:`AlbumResponseDto`.
        """
        params: dict[str, str | bool] = {}
        if asset_id is not None:
            params["assetId"] = str(asset_id)
        if shared is not None:
            params["shared"] = shared
        resp = self._base.get("/api/albums", params=params or None)
        data = resp.json()
        return [AlbumResponseDto.model_validate(item) for item in data]

    def create_album(self, dto: CreateAlbumDto) -> AlbumResponseDto:
        """Create a new album.

        :param dto: :class:`CreateAlbumDto` with album name and optional metadata.
        :returns: The created :class:`AlbumResponseDto`.
        """
        resp = self._base.post(
            "/api/albums", json=dto.model_dump(mode="json", exclude_none=True)
        )
        return AlbumResponseDto.model_validate(resp.json())

    def get_album_info(
        self,
        album_id: UUID | str,
        *,
        key: str | None = None,
        slug: str | None = None,
        without_assets: bool | None = None,
    ) -> AlbumResponseDto:
        """Retrieve information about a specific album by its ID.

        :param album_id: Album ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :param without_assets: If True, omit assets in the response.
        :returns: The :class:`AlbumResponseDto`.
        """
        params: dict[str, str | bool] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        if without_assets is not None:
            params["withoutAssets"] = without_assets
        resp = self._base.get(
            f"/api/albums/{album_id}",
            params=params or None,
        )
        return AlbumResponseDto.model_validate(resp.json())

    def update_album_info(
        self, album_id: UUID | str, dto: UpdateAlbumDto
    ) -> AlbumResponseDto:
        """Update the information of a specific album by its ID.

        :param album_id: Album ID (UUID or string).
        :param dto: :class:`UpdateAlbumDto` with fields to update.
        :returns: The updated :class:`AlbumResponseDto`.
        """
        resp = self._base.patch(
            f"/api/albums/{album_id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return AlbumResponseDto.model_validate(resp.json())

    def delete_album(self, album_id: UUID | str) -> None:
        """Delete a specific album by its ID.

        :param album_id: Album ID (UUID or string).
        """
        self._base.delete(f"/api/albums/{album_id}")

    def get_album_statistics(self) -> AlbumStatisticsResponseDto:
        """Return statistics about the albums available to the authenticated user.

        :returns: :class:`AlbumStatisticsResponseDto`.
        """
        resp = self._base.get("/api/albums/statistics")
        return AlbumStatisticsResponseDto.model_validate(resp.json())

    def add_assets_to_albums(self, dto: AlbumsAddAssetsDto) -> dict[str, object]:
        """Send a list of asset IDs and album IDs to add each asset to each album.

        :param dto: :class:`AlbumsAddAssetsDto` with album and asset IDs.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(
            "/api/albums/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return resp.json()

    def add_assets_to_album(
        self,
        album_id: UUID | str,
        dto: BulkIdsDto,
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> list[BulkIdResponseDto]:
        """Add multiple assets to a specific album by its ID.

        :param album_id: Album ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: List of :class:`BulkIdResponseDto`.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.put(
            f"/api/albums/{album_id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
            params=params or None,
        )
        data = resp.json()
        return [BulkIdResponseDto.model_validate(item) for item in data]

    def remove_asset_from_album(
        self, album_id: UUID | str, dto: BulkIdsDto
    ) -> list[BulkIdResponseDto]:
        """Remove multiple assets from a specific album by its ID.

        :param album_id: Album ID (UUID or string).
        :param dto: :class:`BulkIdsDto` with asset IDs.
        :returns: List of :class:`BulkIdResponseDto`.
        """
        resp = self._base.delete(
            f"/api/albums/{album_id}/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        data = resp.json()
        return [BulkIdResponseDto.model_validate(item) for item in data]

    def add_users_to_album(
        self, album_id: UUID | str, dto: AddUsersDto
    ) -> AlbumResponseDto:
        """Share an album with multiple users.

        :param album_id: Album ID (UUID or string).
        :param dto: :class:`AddUsersDto` with users to add.
        :returns: Updated :class:`AlbumResponseDto`.
        """
        resp = self._base.put(
            f"/api/albums/{album_id}/users",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return AlbumResponseDto.model_validate(resp.json())

    def remove_user_from_album(self, album_id: UUID | str, user_id: UUID | str) -> None:
        """Remove a user from an album. Use an ID of 'me' to leave a shared album.

        :param album_id: Album ID (UUID or string).
        :param user_id: User ID (UUID or string; use 'me' to leave).
        """
        self._base.delete(f"/api/albums/{album_id}/user/{user_id}")

    def update_album_user(
        self,
        album_id: UUID | str,
        user_id: UUID | str,
        dto: UpdateAlbumUserDto,
    ) -> None:
        """Change the role for a specific user in a specific album.

        :param album_id: Album ID (UUID or string).
        :param user_id: User ID (UUID or string).
        :param dto: :class:`UpdateAlbumUserDto` with new role.
        """
        self._base.put(
            f"/api/albums/{album_id}/user/{user_id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
