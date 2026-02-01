"""Authentication (admin) API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class AuthAdminClient:
    """Client for Immich Authentication (admin) endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the auth admin client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def unlink_all_oauth_accounts_admin(self) -> None:
        """Unlink all OAuth accounts associated with user accounts in the system."""
        self._base.post("/api/admin/auth/unlink-all")
