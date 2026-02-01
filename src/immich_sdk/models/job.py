"""Job-related DTOs."""

from enum import Enum

from pydantic import BaseModel, Field


class ManualJobName(str, Enum):
    """Manual job name (for create job endpoint)."""

    PERSON_CLEANUP = "person-cleanup"
    TAG_CLEANUP = "tag-cleanup"
    USER_CLEANUP = "user-cleanup"
    MEMORY_CLEANUP = "memory-cleanup"
    MEMORY_CREATE = "memory-create"
    BACKUP_DATABASE = "backup-database"


class JobCreateDto(BaseModel):
    """DTO for creating a manual job."""

    name: ManualJobName = Field(..., description="Job name")
