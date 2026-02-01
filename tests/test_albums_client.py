"""Tests for AlbumsClient."""

from unittest.mock import MagicMock


from immich_sdk.client.album import AlbumsClient
from immich_sdk.client._base import BaseClient
from immich_sdk.models import AlbumResponseDto, CreateAlbumDto


def test_get_all_albums_returns_parsed_list() -> None:
    """AlbumsClient.get_all_albums returns list of AlbumResponseDto."""
    mock_base = MagicMock(spec=BaseClient)
    mock_base.get.return_value.json.return_value = [
        {
            "id": "album-1",
            "albumName": "Test Album",
            "description": "",
            "albumThumbnailAssetId": None,
            "albumUsers": [],
            "assetCount": 0,
            "assets": [],
            "createdAt": "2024-01-01T00:00:00.000Z",
            "updatedAt": "2024-01-01T00:00:00.000Z",
            "ownerId": "user-1",
            "owner": {"id": "user-1", "email": "u@x.com", "name": "User"},
            "shared": False,
            "hasSharedLink": False,
            "isActivityEnabled": False,
            "contributorCounts": [],
        },
    ]

    client = AlbumsClient(mock_base)
    result = client.get_all_albums()

    assert len(result) == 1
    assert isinstance(result[0], AlbumResponseDto)
    assert result[0].id == "album-1"
    assert result[0].albumName == "Test Album"
    mock_base.get.assert_called_once_with("/api/albums", params=None)


def test_create_album_sends_dto_and_returns_album() -> None:
    """AlbumsClient.create_album sends CreateAlbumDto and returns AlbumResponseDto."""
    mock_base = MagicMock(spec=BaseClient)
    mock_base.post.return_value.json.return_value = {
        "id": "album-new",
        "albumName": "New Album",
        "description": "Desc",
        "albumThumbnailAssetId": None,
        "albumUsers": [],
        "assetCount": 0,
        "assets": [],
        "createdAt": "2024-01-01T00:00:00.000Z",
        "updatedAt": "2024-01-01T00:00:00.000Z",
        "ownerId": "user-1",
        "owner": None,
        "shared": False,
        "hasSharedLink": False,
        "isActivityEnabled": False,
        "contributorCounts": [],
    }

    client = AlbumsClient(mock_base)
    dto = CreateAlbumDto(albumName="New Album", description="Desc")
    result = client.create_album(dto)

    assert isinstance(result, AlbumResponseDto)
    assert result.albumName == "New Album"
    mock_base.post.assert_called_once()
    call_json = mock_base.post.call_args[1]["json"]
    assert call_json["albumName"] == "New Album"
    assert call_json["description"] == "Desc"
