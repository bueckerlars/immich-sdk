"""Faces API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.face import (
    AssetFaceCreateDto,
    AssetFaceDeleteDto,
    AssetFaceResponseDto,
    FaceDto,
)
from immich_sdk.models.person import PersonResponseDto


class FacesClient:
    """Client for Immich Faces endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the faces client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_faces(self, id: UUID | str) -> list[AssetFaceResponseDto]:
        """Retrieve all faces belonging to an asset.

        :param id: Asset ID (UUID or string).
        :returns: List of face DTOs.
        """
        resp = self._base.get("/api/faces", params={"id": str(id)})
        return [AssetFaceResponseDto.model_validate(f) for f in resp.json()]

    def create_face(self, dto: AssetFaceCreateDto) -> None:
        """Create a new face that has not been discovered by facial recognition.

        :param dto: Face create DTO.
        """
        self._base.post("/api/faces", json=dto.model_dump(by_alias=True))

    def delete_face(self, id: UUID | str, dto: AssetFaceDeleteDto) -> None:
        """Delete a face identified by the id.

        :param id: Face ID (UUID or string).
        :param dto: Face delete DTO (e.g. force).
        """
        self._base.delete(f"/api/faces/{id}", json=dto.model_dump(by_alias=True))

    def reassign_faces_by_id(self, id: UUID | str, dto: FaceDto) -> PersonResponseDto:
        """Re-assign the face provided in the body to the person identified by the id in the path.

        :param id: Person ID (UUID or string).
        :param dto: Face DTO (face id to reassign).
        :returns: Updated person.
        """
        resp = self._base.put(f"/api/faces/{id}", json=dto.model_dump(by_alias=True))
        return PersonResponseDto.model_validate(resp.json())
