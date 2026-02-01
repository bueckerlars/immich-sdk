"""Notifications API client."""

from __future__ import annotations

from typing import Any
from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.notification import (
    NotificationCreateDto,
    NotificationDto,
    NotificationUpdateDto,
    NotificationUpdateAllDto,
)


class NotificationsClient:
    """Client for Immich Notifications endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the notifications client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_notifications(self) -> list[NotificationDto]:
        """Retrieve notifications for the current user.

        :returns: List of notification DTOs.
        """
        resp = self._base.get("/api/notifications")
        return [NotificationDto.model_validate(n) for n in resp.json()]

    def get_notification(self, id: UUID | str) -> NotificationDto:
        """Retrieve a notification by ID.

        :param id: Notification ID (UUID or string).
        :returns: Notification DTO.
        """
        resp = self._base.get(f"/api/notifications/{id}")
        return NotificationDto.model_validate(resp.json())

    def update_notification(
        self, id: UUID | str, dto: NotificationUpdateDto
    ) -> NotificationDto:
        """Update a notification.

        :param id: Notification ID (UUID or string).
        :param dto: Notification update DTO.
        :returns: Updated notification DTO.
        """
        resp = self._base.patch(
            f"/api/notifications/{id}",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationDto.model_validate(resp.json())

    def delete_notification(self, id: UUID | str) -> None:
        """Delete a notification.

        :param id: Notification ID (UUID or string).
        """
        self._base.delete(f"/api/notifications/{id}")

    def update_all_notifications(self, dto: NotificationUpdateAllDto) -> None:
        """Update all notifications.

        :param dto: Update all DTO (e.g. ids, readAt).
        """
        self._base.put(
            "/api/notifications",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )

    def delete_all_notifications(self) -> None:
        """Delete all notifications."""
        self._base.delete("/api/notifications")

    def create_notification_admin(self, dto: NotificationCreateDto) -> NotificationDto:
        """Create a new notification for a specific user (admin).

        :param dto: Notification create DTO.
        :returns: Created notification DTO.
        """
        resp = self._base.post(
            "/api/admin/notifications",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationDto.model_validate(resp.json())

    def get_notification_template_admin(
        self, name: str, dto: dict[str, Any]
    ) -> dict[str, Any]:
        """Retrieve a preview of the provided email template (admin).

        :param name: Template name.
        :param dto: Template variables (structure is template-specific).
        :returns: Template preview response.
        """
        resp = self._base.post(f"/api/admin/notifications/templates/{name}", json=dto)
        return resp.json()

    def send_test_email_admin(self, dto: dict[str, Any]) -> dict[str, Any]:
        """Send a test email using the provided SMTP configuration (admin).

        :param dto: SMTP config (structure is server-specific).
        :returns: Test result response.
        """
        resp = self._base.post("/api/admin/notifications/test-email", json=dto)
        return resp.json()
