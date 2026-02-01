"""People API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.face import AssetFaceUpdateDto
from immich_sdk.models.person import (
    MergePersonDto,
    PersonCreateDto,
    PersonResponseDto,
    PersonStatisticsResponseDto,
    PersonUpdateDto,
)


class PeopleClient:
    """Client for Immich People endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the people client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_all_people(self) -> list[PersonResponseDto]:
        """Retrieve all people.

        :returns: List of :class:`PersonResponseDto`.
        """
        resp = self._base.get("/api/people")
        data = resp.json()
        return [PersonResponseDto.model_validate(item) for item in data]

    def create_person(self, dto: PersonCreateDto) -> PersonResponseDto:
        """Create a new person.

        :param dto: :class:`PersonCreateDto` with person data.
        :returns: :class:`PersonResponseDto`.
        """
        resp = self._base.post(
            "/api/people",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return PersonResponseDto.model_validate(resp.json())

    def get_person(self, id: UUID | str) -> PersonResponseDto:
        """Retrieve a specific person by ID.

        :param id: Person ID (UUID or string).
        :returns: :class:`PersonResponseDto`.
        """
        resp = self._base.get(f"/api/people/{id}")
        return PersonResponseDto.model_validate(resp.json())

    def update_person(self, id: UUID | str, dto: PersonUpdateDto) -> PersonResponseDto:
        """Update a person.

        :param id: Person ID (UUID or string).
        :param dto: :class:`PersonUpdateDto` with fields to update.
        :returns: Updated person.
        """
        resp = self._base.put(
            f"/api/people/{id}",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return PersonResponseDto.model_validate(resp.json())

    def delete_person(self, id: UUID | str) -> None:
        """Delete a person.

        :param id: Person ID (UUID or string).
        """
        self._base.delete(f"/api/people/{id}")

    def merge_person(self, id: UUID | str, dto: MergePersonDto) -> PersonResponseDto:
        """Merge multiple people into one.

        :param id: Target person ID (UUID or string).
        :param dto: Merge person DTO (source person IDs).
        :returns: Merged person.
        """
        resp = self._base.post(
            f"/api/people/{id}/merge",
            json=dto.model_dump(mode="json", exclude_none=True),
        )
        return PersonResponseDto.model_validate(resp.json())

    def reassign_faces(
        self, id: UUID | str, dto: AssetFaceUpdateDto
    ) -> list[PersonResponseDto]:
        """Reassign faces to a person.

        :param id: Person ID (UUID or string).
        :param dto: Face update DTO (face reassignments).
        :returns: List of updated persons.
        """
        resp = self._base.put(
            f"/api/people/{id}/reassign-faces",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return [PersonResponseDto.model_validate(p) for p in resp.json()]

    def get_person_statistics(self, id: UUID | str) -> PersonStatisticsResponseDto:
        """Retrieve statistics for a specific person.

        :param id: Person ID (UUID or string).
        :returns: :class:`PersonStatisticsResponseDto`.
        """
        resp = self._base.get(f"/api/people/{id}/statistics")
        return PersonStatisticsResponseDto.model_validate(resp.json())

    def get_person_thumbnail(self, id: UUID | str) -> bytes:
        """Retrieve thumbnail for a person.

        :param id: Person ID (UUID or string).
        :returns: Raw image bytes.
        """
        resp = self._base.get(f"/api/people/{id}/thumbnail")
        return resp.content
