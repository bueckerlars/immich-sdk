"""Assets API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models import (
    AssetBulkDeleteDto,
    AssetBulkUpdateDto,
    AssetBulkUploadCheckDto,
    AssetBulkUploadCheckResponseDto,
    AssetCopyDto,
    AssetJobsDto,
    AssetMediaResponseDto,
    AssetMetadataBulkDeleteDto,
    AssetMetadataBulkResponseDto,
    AssetMetadataBulkUpsertDto,
    AssetMetadataResponseDto,
    AssetMetadataUpsertDto,
    AssetOcrResponseDto,
    AssetResponseDto,
    AssetStatsResponseDto,
    CheckExistingAssetsDto,
    CheckExistingAssetsResponseDto,
    UpdateAssetDto,
)


class AssetsClient:
    """Client for Immich Assets endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the assets client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_asset_info(
        self,
        asset_id: UUID | str,
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> AssetResponseDto:
        """Retrieve detailed information about a specific asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: :class:`AssetResponseDto`.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.get(
            f"/api/assets/{asset_id}",
            params=params or None,
        )
        return AssetResponseDto.model_validate(resp.json())

    def update_asset(
        self, asset_id: UUID | str, dto: UpdateAssetDto
    ) -> AssetResponseDto:
        """Update information of a specific asset.

        :param asset_id: Asset ID (UUID or string).
        :param dto: :class:`UpdateAssetDto` with fields to update.
        :returns: Updated :class:`AssetResponseDto`.
        """
        resp = self._base.put(
            f"/api/assets/{asset_id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return AssetResponseDto.model_validate(resp.json())

    def delete_assets(self, dto: AssetBulkDeleteDto) -> None:
        """Delete multiple assets.

        :param dto: :class:`AssetBulkDeleteDto` with asset IDs to delete.
        """
        self._base.delete(
            "/api/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )

    def update_assets(self, dto: AssetBulkUpdateDto) -> None:
        """Update multiple assets.

        :param dto: :class:`AssetBulkUpdateDto` with asset IDs and fields.
        """
        self._base.put(
            "/api/assets",
            json=dto.model_dump(mode="json", exclude_none=True),
        )

    def upload_asset(
        self,
        files: dict[str, tuple[str, bytes]],
        data: dict[str, str] | None = None,
        *,
        key: str | None = None,
        slug: str | None = None,
        x_immich_checksum: str | None = None,
    ) -> AssetMediaResponseDto:
        """Upload a new asset to the server.

        :param files: Dict mapping field names to (filename, bytes) tuples.
        :param data: Optional form data (e.g. deviceId).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :param x_immich_checksum: Optional SHA1 checksum header.
        :returns: :class:`AssetMediaResponseDto`.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        headers: dict[str, str] = {}
        if x_immich_checksum is not None:
            headers["x-immich-checksum"] = x_immich_checksum
        resp = self._base.post(
            "/api/assets",
            files=files,
            data=data,
            params=params or None,
            headers=headers or None,
        )
        return AssetMediaResponseDto.model_validate(resp.json())

    def check_bulk_upload(
        self, dto: AssetBulkUploadCheckDto
    ) -> AssetBulkUploadCheckResponseDto:
        """Determine which assets have already been uploaded based on their SHA1 checksums.

        :param dto: :class:`AssetBulkUploadCheckDto` with checksums to check.
        :returns: :class:`AssetBulkUploadCheckResponseDto`.
        """
        resp = self._base.post(
            "/api/assets/bulk-upload-check",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return AssetBulkUploadCheckResponseDto.model_validate(resp.json())

    def copy_asset(self, dto: AssetCopyDto) -> None:
        """Copy asset information (albums, tags, etc.) from one asset to another.

        :param dto: :class:`AssetCopyDto` with source and target asset IDs.
        """
        self._base.put(
            "/api/assets/copy",
            json=dto.model_dump(mode="json", exclude_none=True),
        )

    def check_existing_assets(
        self, dto: CheckExistingAssetsDto
    ) -> CheckExistingAssetsResponseDto:
        """Check if multiple assets exist on the server (for background backup).

        :param dto: :class:`CheckExistingAssetsDto` with device IDs and asset IDs.
        :returns: :class:`CheckExistingAssetsResponseDto`.
        """
        resp = self._base.post(
            "/api/assets/exist",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return CheckExistingAssetsResponseDto.model_validate(resp.json())

    def run_asset_jobs(self, dto: AssetJobsDto) -> None:
        """Run a specific job on a set of assets.

        :param dto: :class:`AssetJobsDto` with job name and asset IDs.
        """
        self._base.post(
            "/api/assets/jobs",
            json=dto.model_dump(mode="json", exclude_none=True),
        )

    def get_asset_statistics(
        self,
        *,
        is_favorite: bool | None = None,
        is_trashed: bool | None = None,
        visibility: str | None = None,
    ) -> AssetStatsResponseDto:
        """Retrieve various statistics about the assets owned by the authenticated user.

        :param is_favorite: Optional filter for favorite assets.
        :param is_trashed: Optional filter for trashed assets.
        :param visibility: Optional visibility filter.
        :returns: :class:`AssetStatsResponseDto`.
        """
        params: dict[str, str | bool] = {}
        if is_favorite is not None:
            params["isFavorite"] = is_favorite
        if is_trashed is not None:
            params["isTrashed"] = is_trashed
        if visibility is not None:
            params["visibility"] = visibility
        resp = self._base.get("/api/assets/statistics", params=params or None)
        return AssetStatsResponseDto.model_validate(resp.json())

    def download_asset(
        self,
        asset_id: UUID | str,
        *,
        key: str | None = None,
        slug: str | None = None,
        edited: bool = False,
    ) -> bytes:
        """Download the original file of the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :param edited: If True, return edited version if available.
        :returns: Raw file bytes.
        """
        params: dict[str, str | bool] = {"edited": edited}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.get(f"/api/assets/{asset_id}/original", params=params)
        return resp.content

    def view_asset(
        self,
        asset_id: UUID | str,
        *,
        key: str | None = None,
        slug: str | None = None,
        size: str | None = None,
        edited: bool = False,
    ) -> bytes:
        """Retrieve the thumbnail image for the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :param size: Optional thumbnail size.
        :param edited: If True, return edited version if available.
        :returns: Raw image bytes.
        """
        params: dict[str, str | bool] = {"edited": edited}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        if size is not None:
            params["size"] = size
        resp = self._base.get(f"/api/assets/{asset_id}/thumbnail", params=params)
        return resp.content

    def play_asset_video(
        self,
        asset_id: UUID | str,
        *,
        key: str | None = None,
        slug: str | None = None,
    ) -> bytes:
        """Stream the video file for the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Optional shared link key.
        :param slug: Optional shared link slug.
        :returns: Raw video bytes.
        """
        params: dict[str, str] = {}
        if key is not None:
            params["key"] = key
        if slug is not None:
            params["slug"] = slug
        resp = self._base.get(
            f"/api/assets/{asset_id}/video/playback", params=params or None
        )
        return resp.content

    def get_asset_metadata(
        self, asset_id: UUID | str
    ) -> list[AssetMetadataResponseDto]:
        """Retrieve all metadata key-value pairs associated with the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :returns: List of metadata DTOs.
        """
        resp = self._base.get(f"/api/assets/{asset_id}/metadata")
        return [AssetMetadataResponseDto.model_validate(m) for m in resp.json()]

    def update_asset_metadata(
        self, asset_id: UUID | str, dto: AssetMetadataUpsertDto
    ) -> list[AssetMetadataResponseDto]:
        """Update or add metadata key-value pairs for the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param dto: Metadata upsert DTO.
        :returns: Updated list of metadata DTOs.
        """
        resp = self._base.put(
            f"/api/assets/{asset_id}/metadata",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return [AssetMetadataResponseDto.model_validate(m) for m in resp.json()]

    def delete_asset_metadata(self, asset_id: UUID | str, key: str) -> None:
        """Delete a specific metadata key-value pair associated with the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Metadata key to delete.
        """
        self._base.delete(f"/api/assets/{asset_id}/metadata/{key}")

    def get_asset_metadata_by_key(
        self, asset_id: UUID | str, key: str
    ) -> AssetMetadataResponseDto:
        """Retrieve the value of a specific metadata key associated with the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :param key: Metadata key.
        :returns: Metadata response DTO.
        """
        resp = self._base.get(f"/api/assets/{asset_id}/metadata/{key}")
        return AssetMetadataResponseDto.model_validate(resp.json())

    def get_asset_ocr(self, asset_id: UUID | str) -> list[AssetOcrResponseDto]:
        """Retrieve all OCR data associated with the specified asset.

        :param asset_id: Asset ID (UUID or string).
        :returns: List of OCR result DTOs.
        """
        resp = self._base.get(f"/api/assets/{asset_id}/ocr")
        return [AssetOcrResponseDto.model_validate(o) for o in resp.json()]

    def update_bulk_asset_metadata(
        self, dto: AssetMetadataBulkUpsertDto
    ) -> list[AssetMetadataBulkResponseDto]:
        """Upsert metadata key-value pairs for multiple assets.

        :param dto: Bulk metadata upsert DTO.
        :returns: Updated list of bulk metadata response DTOs.
        """
        resp = self._base.put(
            "/api/assets/metadata",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return [AssetMetadataBulkResponseDto.model_validate(m) for m in resp.json()]

    def delete_bulk_asset_metadata(self, dto: AssetMetadataBulkDeleteDto) -> None:
        """Delete metadata key-value pairs for multiple assets.

        :param dto: Bulk metadata delete DTO.
        """
        self._base.delete(
            "/api/assets/metadata",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
