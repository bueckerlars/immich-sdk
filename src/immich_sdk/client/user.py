"""User API client (non-admin)."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.models import UserResponseDto
from immich_sdk.client._base import BaseClient


class UserClient:
    """Client for Immich User endpoints (non-admin). Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the user client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_user(self, id: UUID | str) -> UserResponseDto:
        """Retrieve a specific user by their ID.

        :param id: User ID (UUID or string; use 'me' for current user).
        :returns: :class:`UserResponseDto`.
        """
        resp = self._base.get(f"/api/user/{id}")
        return UserResponseDto.model_validate(resp.json())

    def get_my_user(self) -> UserResponseDto:
        """Retrieve the current user.

        :returns: :class:`UserResponseDto`.
        """
        return self.get_user("me")

    def update_user(self, id: UUID | str, dto: dict[str, object]) -> UserResponseDto:
        """Update a user.

        :param id: User ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Updated :class:`UserResponseDto`.
        """
        resp = self._base.put(f"/api/user/{id}", json=dto)
        return UserResponseDto.model_validate(resp.json())

    def get_user_preferences(self, id: UUID | str) -> dict[str, object]:
        """Retrieve preferences for a user.

        :param id: User ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/user/{id}/preferences")
        return resp.json()

    def update_user_preferences(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update preferences for a user.

        :param id: User ID (UUID or string).
        :param dto: Dict with preference fields.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/user/{id}/preferences", json=dto)
        return resp.json()

    def get_profile_image(self, id: UUID | str) -> bytes:
        """Retrieve profile image for a user.

        :param id: User ID (UUID or string).
        :returns: Raw image bytes.
        """
        resp = self._base.get(f"/api/user/{id}/profile-image")
        return resp.content

    def create_profile_image(
        self, id: UUID | str, file: bytes, filename: str = "profile.jpg"
    ) -> dict[str, object]:
        """Create/upload profile image for a user.

        :param id: User ID (UUID or string).
        :param file: Image file bytes.
        :param filename: Filename for the upload (default: profile.jpg).
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(
            f"/api/user/{id}/profile-image",
            files={"file": (filename, file)},
        )
        return resp.json()

    def delete_profile_image(self, id: UUID | str) -> None:
        """Delete profile image for a user.

        :param id: User ID (UUID or string).
        """
        self._base.delete(f"/api/user/{id}/profile-image")
