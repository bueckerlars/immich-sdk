"""Common DTOs and enums used across the Immich API."""

from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class AlbumUserRole(str, Enum):
    """Album user role."""

    EDITOR = "editor"
    VIEWER = "viewer"


class AssetOrder(str, Enum):
    """Asset sort order."""

    ASC = "asc"
    DESC = "desc"


class BulkIdErrorReason(str, Enum):
    """Error reason for bulk operations."""

    DUPLICATE = "duplicate"
    NO_PERMISSION = "no_permission"
    NOT_FOUND = "not_found"
    UNKNOWN = "unknown"


class BulkIdsDto(BaseModel):
    """DTO for bulk operations with a list of IDs."""

    ids: list[UUID] = Field(..., description="IDs to process")


class BulkIdResponseDto(BaseModel):
    """Response item for bulk operations. Uses :class:`BulkIdErrorReason` for error."""

    id: str = Field(..., description="ID")
    success: bool = Field(..., description="Whether operation succeeded")
    error: BulkIdErrorReason | None = Field(None, description="Error reason if failed")


class AssetIdsDto(BaseModel):
    """DTO for a list of asset IDs."""

    assetIds: list[UUID] = Field(..., description="Asset IDs")
