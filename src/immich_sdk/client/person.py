"""People API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class PeopleClient:
    """Client for Immich People endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the people client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_all_people(self) -> list[dict[str, object]]:
        """Retrieve all people.

        :returns: List of person dicts.
        """
        resp = self._base.get("/api/people")
        return resp.json()

    def create_person(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new person.

        :param dto: Dict with person data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/people", json=dto)
        return resp.json()

    def get_person(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a specific person by ID.

        :param id: Person ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/people/{id}")
        return resp.json()

    def update_person(
        self, id: UUID | str, dto: dict[str, object]
    ) -> list[dict[str, object]]:
        """Update a person.

        :param id: Person ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: List of updated face/person dicts.
        """
        resp = self._base.put(f"/api/people/{id}", json=dto)
        return resp.json()

    def delete_person(self, id: UUID | str) -> None:
        """Delete a person.

        :param id: Person ID (UUID or string).
        """
        self._base.delete(f"/api/people/{id}")

    def merge_person(self, id: UUID | str, dto: dict[str, object]) -> dict[str, object]:
        """Merge multiple people into one.

        :param id: Target person ID (UUID or string).
        :param dto: Dict with source person IDs.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(f"/api/people/{id}/merge", json=dto)
        return resp.json()

    def reassign_faces(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Reassign faces to a person.

        :param id: Person ID (UUID or string).
        :param dto: Dict with face IDs to reassign.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/people/{id}/reassign-faces", json=dto)
        return resp.json()

    def get_person_statistics(self, id: UUID | str) -> dict[str, object]:
        """Retrieve statistics for a specific person.

        :param id: Person ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/people/{id}/statistics")
        return resp.json()

    def get_person_thumbnail(self, id: UUID | str) -> bytes:
        """Retrieve thumbnail for a person.

        :param id: Person ID (UUID or string).
        :returns: Raw image bytes.
        """
        resp = self._base.get(f"/api/people/{id}/thumbnail")
        return resp.content
