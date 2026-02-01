"""Tests for SearchClient."""

from unittest.mock import MagicMock

from immich_sdk.client._base import BaseClient
from immich_sdk.client.search import SearchClient
from immich_sdk.models import MetadataSearchDto, SearchResponseDto


def _minimal_asset(id: str, type: str = "IMAGE") -> dict:
    """Minimal asset dict satisfying AssetResponseDto required fields."""
    return {
        "id": id,
        "type": type,
        "visibility": "timeline",
        "checksum": "csum",
        "createdAt": "2024-01-01T00:00:00.000Z",
        "deviceAssetId": "dev-1",
        "deviceId": "device-1",
        "duration": "0:00:00.000",
        "fileCreatedAt": "2024-01-01T00:00:00.000Z",
        "fileModifiedAt": "2024-01-01T00:00:00.000Z",
        "hasMetadata": True,
        "height": 100,
        "localDateTime": "2024-01-01T00:00:00.000Z",
        "originalFileName": "x.jpg",
        "originalPath": "/x.jpg",
        "ownerId": "user-1",
        "thumbhash": None,
        "updatedAt": "2024-01-01T00:00:00.000Z",
        "width": 100,
        "isArchived": False,
        "isEdited": False,
        "isFavorite": False,
        "isOffline": False,
        "isTrashed": False,
    }


def test_search_assets_returns_search_response_dto() -> None:
    """SearchClient.search_assets sends MetadataSearchDto and returns SearchResponseDto."""
    mock_base = MagicMock(spec=BaseClient)
    mock_base.post.return_value.json.return_value = {
        "albums": {
            "count": 0,
            "facets": [],
            "items": [],
            "total": 0,
        },
        "assets": {
            "count": 2,
            "facets": [],
            "items": [_minimal_asset("asset-1"), _minimal_asset("asset-2")],
            "nextPage": None,
            "total": 2,
        },
    }

    client = SearchClient(mock_base)
    dto = MetadataSearchDto(isFavorite=True)
    result = client.search_assets(dto)

    assert isinstance(result, SearchResponseDto)
    assert result.assets.total == 2
    assert len(result.assets.items) == 2
    assert result.assets.items[0].id == "asset-1"
    assert result.assets.items[1].id == "asset-2"
    mock_base.post.assert_called_once_with(
        "/api/search/assets",
        json={"isFavorite": True},
    )


def test_search_assets_empty() -> None:
    """SearchClient.search_assets returns empty assets when no match."""
    mock_base = MagicMock(spec=BaseClient)
    mock_base.post.return_value.json.return_value = {
        "albums": {"count": 0, "facets": [], "items": [], "total": 0},
        "assets": {"count": 0, "facets": [], "items": [], "nextPage": None, "total": 0},
    }

    client = SearchClient(mock_base)
    result = client.search_assets(MetadataSearchDto())

    assert isinstance(result, SearchResponseDto)
    assert result.assets.total == 0
    assert len(result.assets.items) == 0
