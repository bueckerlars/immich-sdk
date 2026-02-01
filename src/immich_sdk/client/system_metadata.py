"""System metadata API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.system_metadata import (
    AdminOnboardingUpdateDto,
    ReverseGeocodingStateResponseDto,
    SystemMetadataResponseDto,
    VersionCheckStateResponseDto,
)


class SystemMetadataClient:
    """Client for Immich System metadata endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the system metadata client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_system_metadata(self) -> SystemMetadataResponseDto:
        """Get system metadata (combined or root response).

        :returns: System metadata response DTO.
        """
        resp = self._base.get("/api/system-metadata")
        return SystemMetadataResponseDto.model_validate(resp.json())

    def get_admin_onboarding(self) -> AdminOnboardingUpdateDto:
        """Retrieve the current admin onboarding status.

        :returns: Admin onboarding status DTO.
        """
        resp = self._base.get("/api/system-metadata/admin-onboarding")
        return AdminOnboardingUpdateDto.model_validate(resp.json())

    def get_reverse_geocoding_state(
        self,
    ) -> ReverseGeocodingStateResponseDto:
        """Retrieve the current state of the reverse geocoding import.

        :returns: Reverse geocoding state DTO.
        """
        resp = self._base.get("/api/system-metadata/reverse-geocoding-state")
        return ReverseGeocodingStateResponseDto.model_validate(resp.json())

    def get_version_check_state(self) -> VersionCheckStateResponseDto:
        """Retrieve the current state of the version check process.

        :returns: Version check state DTO.
        """
        resp = self._base.get("/api/system-metadata/version-check-state")
        return VersionCheckStateResponseDto.model_validate(resp.json())
