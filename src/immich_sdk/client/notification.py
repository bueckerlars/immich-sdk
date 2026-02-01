"""Notifications API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class NotificationsClient:
    """Client for Immich Notifications endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the notifications client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_notifications(self) -> list[dict[str, object]]:
        """Retrieve notifications for the current user.

        :returns: List of notification dicts.
        """
        resp = self._base.get("/api/notifications")
        return resp.json()

    def get_notification(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a notification by ID.

        :param id: Notification ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/notifications/{id}")
        return resp.json()

    def update_notification(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update a notification.

        :param id: Notification ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.patch(f"/api/notifications/{id}", json=dto)
        return resp.json()

    def delete_notification(self, id: UUID | str) -> None:
        """Delete a notification.

        :param id: Notification ID (UUID or string).
        """
        self._base.delete(f"/api/notifications/{id}")

    def update_all_notifications(self, dto: dict[str, object]) -> None:
        """Update all notifications.

        :param dto: Dict with update options.
        """
        self._base.put("/api/notifications", json=dto)

    def delete_all_notifications(self) -> None:
        """Delete all notifications."""
        self._base.delete("/api/notifications")

    def create_notification_admin(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new notification for a specific user (admin).

        :param dto: Dict with notification and user data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/admin/notifications", json=dto)
        return resp.json()

    def get_notification_template_admin(
        self, name: str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Retrieve a preview of the provided email template (admin).

        :param name: Template name.
        :param dto: Dict with template variables.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post(f"/api/admin/notifications/templates/{name}", json=dto)
        return resp.json()

    def send_test_email_admin(self, dto: dict[str, object]) -> dict[str, object]:
        """Send a test email using the provided SMTP configuration (admin).

        :param dto: Dict with SMTP config.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/admin/notifications/test-email", json=dto)
        return resp.json()
