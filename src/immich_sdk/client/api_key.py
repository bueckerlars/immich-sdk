"""API keys API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import (
    APIKeyCreateDto,
    APIKeyCreateResponseDto,
    APIKeyResponseDto,
    APIKeyUpdateDto,
)
from immich_sdk.client._base import BaseClient


class APIKeysClient:
    """Client for Immich API keys endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the API keys client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_api_keys(self) -> list[APIKeyResponseDto]:
        """Retrieve all API keys of the current user.

        :returns: List of :class:`APIKeyResponseDto`.
        """
        resp = self._base.get("/api/api-keys")
        data = resp.json()
        return [APIKeyResponseDto.model_validate(item) for item in data]

    def create_api_key(self, dto: APIKeyCreateDto) -> APIKeyCreateResponseDto:
        """Create a new API key limited to the specified permissions.

        :param dto: :class:`APIKeyCreateDto` with name and permissions.
        :returns: :class:`APIKeyCreateResponseDto` (includes secret once).
        """
        resp = self._base.post(
            "/api/api-keys", json=dto.model_dump(mode="json", exclude_none=True)
        )
        return APIKeyCreateResponseDto.model_validate(resp.json())

    def get_my_api_key(self) -> APIKeyResponseDto:
        """Retrieve the API key that is used to access this endpoint.

        :returns: :class:`APIKeyResponseDto`.
        """
        resp = self._base.get("/api/api-keys/me")
        return APIKeyResponseDto.model_validate(resp.json())

    def get_api_key(self, key_id: UUID | str) -> APIKeyResponseDto:
        """Retrieve an API key by its ID. The current user must own this API key.

        :param key_id: API key ID (UUID or string).
        :returns: :class:`APIKeyResponseDto`.
        """
        resp = self._base.get(f"/api/api-keys/{key_id}")
        return APIKeyResponseDto.model_validate(resp.json())

    def update_api_key(
        self, key_id: UUID | str, dto: APIKeyUpdateDto
    ) -> APIKeyResponseDto:
        """Update the name and permissions of an API key by its ID.

        :param key_id: API key ID (UUID or string).
        :param dto: :class:`APIKeyUpdateDto` with new name and/or permissions.
        :returns: Updated :class:`APIKeyResponseDto`.
        """
        resp = self._base.put(
            f"/api/api-keys/{key_id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return APIKeyResponseDto.model_validate(resp.json())

    def delete_api_key(self, key_id: UUID | str) -> None:
        """Delete an API key by its ID. The current user must own this API key.

        :param key_id: API key ID (UUID or string).
        """
        self._base.delete(f"/api/api-keys/{key_id}")
