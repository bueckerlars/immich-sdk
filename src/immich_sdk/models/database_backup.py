"""Database backup (admin) DTOs."""

from pydantic import BaseModel, Field


class DatabaseBackupDto(BaseModel):
    """Single database backup entry."""

    filename: str = Field(..., description="Backup filename")
    filesize: float = Field(..., description="File size")


class DatabaseBackupListResponseDto(BaseModel):
    """List of database backups."""

    backups: list[DatabaseBackupDto] = Field(..., description="List of backups")


class DatabaseBackupDeleteDto(BaseModel):
    """Request to delete database backups."""

    backups: list[str] = Field(..., description="Backup filenames to delete")
