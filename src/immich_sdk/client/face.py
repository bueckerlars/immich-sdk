"""Faces API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class FacesClient:
    """Client for Immich Faces endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the faces client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_faces(self, id: UUID | str) -> list[dict[str, object]]:
        """Retrieve all faces belonging to an asset.

        :param id: Asset ID (UUID or string).
        :returns: List of face dicts.
        """
        resp = self._base.get("/api/faces", params={"id": str(id)})
        return resp.json()

    def create_face(self, dto: dict[str, object]) -> None:
        """Create a new face that has not been discovered by facial recognition.

        :param dto: Dict with face data.
        """
        self._base.post("/api/faces", json=dto)

    def delete_face(self, id: UUID | str, dto: dict[str, object]) -> None:
        """Delete a face identified by the id.

        :param id: Face ID (UUID or string).
        :param dto: Dict with face/person data.
        """
        self._base.delete(f"/api/faces/{id}", json=dto)

    def reassign_faces_by_id(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Re-assign the face provided in the body to the person identified by the id in the path.

        :param id: Person ID (UUID or string).
        :param dto: Dict with face IDs to reassign.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/faces/{id}", json=dto)
        return resp.json()
