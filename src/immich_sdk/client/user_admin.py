"""Users (admin) API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class UserAdminClient:
    """Client for Immich Users (admin) endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the user admin client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def search_users_admin(
        self,
        *,
        id: UUID | str | None = None,
        with_deleted: bool | None = None,
    ) -> list[dict[str, object]]:
        """Search for users (admin).

        :param id: Optional user ID filter.
        :param with_deleted: If True, include deleted users.
        :returns: List of user dicts.
        """
        params: dict[str, str | bool] = {}
        if id is not None:
            params["id"] = str(id)
        if with_deleted is not None:
            params["withDeleted"] = with_deleted
        resp = self._base.get("/api/admin/users", params=params or None)
        return resp.json()

    def create_user_admin(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new user (admin).

        :param dto: Dict with user data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/admin/users", json=dto)
        return resp.json()

    def get_user_admin(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a specific user by their ID (admin).

        :param id: User ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/admin/users/{id}")
        return resp.json()

    def update_user_admin(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update an existing user (admin).

        :param id: User ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/admin/users/{id}", json=dto)
        return resp.json()

    def delete_user_admin(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Delete a user (admin).

        :param id: User ID (UUID or string).
        :param dto: Dict with delete options.
        :returns: Raw response dict from the API.
        """
        resp = self._base.delete(f"/api/admin/users/{id}", json=dto)
        return resp.json()

    def restore_user_admin(self, id: UUID | str) -> dict[str, object]:
        """Restore a previously deleted user (admin).

        :param id: User ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(f"/api/admin/users/{id}/restore")
        return resp.json()

    def get_user_preferences_admin(self, id: UUID | str) -> dict[str, object]:
        """Retrieve the preferences of a specific user (admin).

        :param id: User ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/admin/users/{id}/preferences")
        return resp.json()

    def update_user_preferences_admin(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update the preferences of a specific user (admin).

        :param id: User ID (UUID or string).
        :param dto: Dict with preference fields.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/admin/users/{id}/preferences", json=dto)
        return resp.json()

    def get_user_sessions_admin(self, id: UUID | str) -> list[dict[str, object]]:
        """Retrieve all sessions for a specific user (admin).

        :param id: User ID (UUID or string).
        :returns: List of session dicts.
        """
        resp = self._base.get(f"/api/admin/users/{id}/sessions")
        return resp.json()

    def get_user_statistics_admin(
        self,
        id: UUID | str,
        *,
        is_favorite: bool | None = None,
        is_trashed: bool | None = None,
        visibility: str | None = None,
    ) -> dict[str, object]:
        """Retrieve asset statistics for a specific user (admin).

        :param id: User ID (UUID or string).
        :param is_favorite: Optional filter for favorite assets.
        :param is_trashed: Optional filter for trashed assets.
        :param visibility: Optional visibility filter.
        :returns: Raw response dict from the API.
        """
        params: dict[str, str | bool] = {}
        if is_favorite is not None:
            params["isFavorite"] = is_favorite
        if is_trashed is not None:
            params["isTrashed"] = is_trashed
        if visibility is not None:
            params["visibility"] = visibility
        resp = self._base.get(
            f"/api/admin/users/{id}/statistics", params=params or None
        )
        return resp.json()
