"""Pydantic models for the Immich API."""

from immich_sdk.models.activity import (
    ActivityCreateDto,
    ActivityResponseDto,
    ActivityStatisticsResponseDto,
)
from immich_sdk.models.album import (
    AddUsersDto,
    AlbumResponseDto,
    AlbumStatisticsResponseDto,
    AlbumUserAddDto,
    AlbumUserCreateDto,
    AlbumsAddAssetsDto,
    CreateAlbumDto,
    UpdateAlbumDto,
    UpdateAlbumUserDto,
)
from immich_sdk.models.api_key import (
    APIKeyCreateDto,
    APIKeyCreateResponseDto,
    APIKeyResponseDto,
    APIKeyUpdateDto,
)
from immich_sdk.models.auth import (
    AuthStatusResponseDto,
    LoginCredentialDto,
    LoginResponseDto,
)
from immich_sdk.models.common import (
    AlbumUserRole,
    AssetIdsDto,
    AssetOrder,
    BulkIdErrorReason,
    BulkIdResponseDto,
    BulkIdsDto,
)
from immich_sdk.models.user import UserResponseDto

__all__ = [
    "ActivityCreateDto",
    "ActivityResponseDto",
    "ActivityStatisticsResponseDto",
    "AddUsersDto",
    "AlbumResponseDto",
    "AlbumStatisticsResponseDto",
    "AlbumUserAddDto",
    "AlbumUserCreateDto",
    "AlbumsAddAssetsDto",
    "UpdateAlbumUserDto",
    "AlbumUserRole",
    "APIKeyCreateDto",
    "APIKeyCreateResponseDto",
    "APIKeyResponseDto",
    "APIKeyUpdateDto",
    "AssetIdsDto",
    "AssetOrder",
    "AuthStatusResponseDto",
    "BulkIdErrorReason",
    "BulkIdResponseDto",
    "BulkIdsDto",
    "CreateAlbumDto",
    "LoginCredentialDto",
    "LoginResponseDto",
    "UpdateAlbumDto",
    "UserResponseDto",
]
