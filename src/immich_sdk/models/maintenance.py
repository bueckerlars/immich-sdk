"""Maintenance (admin) DTOs."""

from enum import Enum

from pydantic import BaseModel, Field


class MaintenanceAction(str, Enum):
    """Maintenance action."""

    START = "start"
    END = "end"
    SELECT_DATABASE_RESTORE = "select_database_restore"
    RESTORE_DATABASE = "restore_database"


class StorageFolder(str, Enum):
    """Storage folder."""

    ENCODED_VIDEO = "encoded-video"
    LIBRARY = "library"
    UPLOAD = "upload"
    PROFILE = "profile"
    THUMBS = "thumbs"
    BACKUPS = "backups"


class SetMaintenanceModeDto(BaseModel):
    """DTO for setting maintenance mode."""

    action: MaintenanceAction = Field(..., description="Maintenance action")
    restoreBackupFilename: str | None = Field(
        None, description="Restore backup filename"
    )


class MaintenanceStatusResponseDto(BaseModel):
    """Maintenance status response."""

    action: MaintenanceAction = Field(..., description="Maintenance action")
    active: bool = Field(..., description="Whether maintenance is active")
    error: str | None = Field(None, description="Error message")
    progress: float | None = Field(None, description="Progress (0-1)")
    task: str | None = Field(None, description="Current task description")


class MaintenanceAuthDto(BaseModel):
    """Maintenance auth (username)."""

    username: str = Field(..., description="Maintenance username")


class MaintenanceDetectInstallStorageFolderDto(BaseModel):
    """Storage folder info in detect-install response."""

    folder: StorageFolder | str = Field(..., description="Storage folder")
    files: float = Field(..., description="Number of files")
    readable: bool = Field(..., description="Whether the folder is readable")
    writable: bool = Field(..., description="Whether the folder is writable")


class MaintenanceDetectInstallResponseDto(BaseModel):
    """Response from detect-install."""

    storage: list[MaintenanceDetectInstallStorageFolderDto] = Field(
        ..., description="Storage folders"
    )


class MaintenanceLoginDto(BaseModel):
    """Maintenance login (token)."""

    token: str | None = Field(None, description="Maintenance token")
