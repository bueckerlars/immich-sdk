"""Partners API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class PartnersClient:
    """Client for Immich Partners endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the partners client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_partners(self) -> list[dict[str, object]]:
        """Retrieve list of partners.

        :returns: List of partner dicts.
        """
        resp = self._base.get("/api/partners")
        return resp.json()

    def create_partner(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new partner.

        :param dto: Dict with partner data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/partners", json=dto)
        return resp.json()

    def remove_partner(self, id: str) -> None:
        """Remove a partner.

        :param id: Partner ID.
        """
        self._base.delete(f"/api/partners/{id}")

    def update_partner(self, id: str, dto: dict[str, object]) -> dict[str, object]:
        """Update a partner.

        :param id: Partner ID.
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/partners/{id}", json=dto)
        return resp.json()
