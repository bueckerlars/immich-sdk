"""Partners API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.partner import (
    PartnerCreateDto,
    PartnerResponseDto,
    PartnerUpdateDto,
)


class PartnersClient:
    """Client for Immich Partners endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the partners client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_partners(self) -> list[PartnerResponseDto]:
        """Retrieve list of partners.

        :returns: List of partner DTOs.
        """
        resp = self._base.get("/api/partners")
        return [PartnerResponseDto.model_validate(p) for p in resp.json()]

    def create_partner(self, dto: PartnerCreateDto) -> PartnerResponseDto:
        """Create a new partner.

        :param dto: Partner create DTO.
        :returns: Created partner DTO.
        """
        resp = self._base.post(
            "/api/partners",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return PartnerResponseDto.model_validate(resp.json())

    def remove_partner(self, id: str) -> None:
        """Remove a partner.

        :param id: Partner ID.
        """
        self._base.delete(f"/api/partners/{id}")

    def update_partner(self, id: str, dto: PartnerUpdateDto) -> PartnerResponseDto:
        """Update a partner.

        :param id: Partner ID.
        :param dto: Partner update DTO.
        :returns: Updated partner DTO.
        """
        resp = self._base.put(
            f"/api/partners/{id}",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return PartnerResponseDto.model_validate(resp.json())
