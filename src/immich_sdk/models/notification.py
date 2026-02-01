"""Notification-related DTOs."""

from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class NotificationLevel(str, Enum):
    """Notification level."""

    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class NotificationType(str, Enum):
    """Notification type."""

    JOB_FAILED = "JobFailed"
    BACKUP_FAILED = "BackupFailed"
    SYSTEM_MESSAGE = "SystemMessage"
    ALBUM_INVITE = "AlbumInvite"
    ALBUM_UPDATE = "AlbumUpdate"
    CUSTOM = "Custom"


class NotificationCreateDto(BaseModel):
    """DTO for creating a notification (admin)."""

    title: str = Field(..., description="Notification title")
    userId: UUID = Field(..., description="User ID to send notification to")
    description: str | None = Field(None, description="Notification description")
    level: NotificationLevel | None = Field(None, description="Notification level")
    type: NotificationType | None = Field(None, description="Notification type")
    readAt: str | None = Field(None, description="Date when notification was read")
    data: dict[str, Any] | None = Field(
        None, description="Additional notification data"
    )


class NotificationUpdateDto(BaseModel):
    """DTO for updating a notification."""

    readAt: str | None = Field(None, description="Date when notification was read")


class NotificationUpdateAllDto(BaseModel):
    """DTO for updating multiple notifications."""

    ids: list[UUID] = Field(..., description="Notification IDs to update")
    readAt: str | None = Field(None, description="Date when notifications were read")


class NotificationDeleteAllDto(BaseModel):
    """DTO for deleting multiple notifications."""

    ids: list[UUID] = Field(..., description="Notification IDs to delete")


class NotificationDto(BaseModel):
    """Notification response DTO."""

    id: str = Field(..., description="Notification ID")
    createdAt: str = Field(..., description="Creation date")
    title: str = Field(..., description="Notification title")
    type: NotificationType = Field(..., description="Notification type")
    level: NotificationLevel = Field(..., description="Notification level")
    description: str | None = Field(None, description="Notification description")
    readAt: str | None = Field(None, description="Date when notification was read")
    data: dict[str, Any] | None = Field(
        None, description="Additional notification data"
    )
