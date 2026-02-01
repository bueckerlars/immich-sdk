"""Queue-related DTOs."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class QueueCommand(str, Enum):
    """Queue command to execute."""

    START = "start"
    PAUSE = "pause"
    RESUME = "resume"
    EMPTY = "empty"
    CLEAR_FAILED = "clear-failed"


class QueueName(str, Enum):
    """Queue name."""

    THUMBNAIL_GENERATION = "thumbnailGeneration"
    METADATA_EXTRACTION = "metadataExtraction"
    VIDEO_CONVERSION = "videoConversion"
    FACE_DETECTION = "faceDetection"
    FACIAL_RECOGNITION = "facialRecognition"
    SMART_SEARCH = "smartSearch"
    DUPLICATE_DETECTION = "duplicateDetection"
    BACKGROUND_TASK = "backgroundTask"
    STORAGE_TEMPLATE_MIGRATION = "storageTemplateMigration"
    MIGRATION = "migration"
    SEARCH = "search"
    SIDECAR = "sidecar"
    LIBRARY = "library"
    NOTIFICATIONS = "notifications"
    BACKUP_DATABASE = "backupDatabase"
    OCR = "ocr"
    WORKFLOW = "workflow"
    EDITOR = "editor"


class QueueJobStatus(str, Enum):
    """Queue job status."""

    ACTIVE = "active"
    FAILED = "failed"
    COMPLETED = "completed"
    DELAYED = "delayed"
    WAITING = "waiting"
    PAUSED = "paused"


class JobName(str, Enum):
    """Job name (queue job type)."""

    ASSET_DELETE = "AssetDelete"
    ASSET_DELETE_CHECK = "AssetDeleteCheck"
    ASSET_DETECT_FACES_QUEUE_ALL = "AssetDetectFacesQueueAll"
    ASSET_DETECT_FACES = "AssetDetectFaces"
    ASSET_DETECT_DUPLICATES_QUEUE_ALL = "AssetDetectDuplicatesQueueAll"
    ASSET_DETECT_DUPLICATES = "AssetDetectDuplicates"
    ASSET_EDIT_THUMBNAIL_GENERATION = "AssetEditThumbnailGeneration"
    ASSET_ENCODE_VIDEO_QUEUE_ALL = "AssetEncodeVideoQueueAll"
    ASSET_ENCODE_VIDEO = "AssetEncodeVideo"
    ASSET_EMPTY_TRASH = "AssetEmptyTrash"
    ASSET_EXTRACT_METADATA_QUEUE_ALL = "AssetExtractMetadataQueueAll"
    ASSET_EXTRACT_METADATA = "AssetExtractMetadata"
    ASSET_FILE_MIGRATION = "AssetFileMigration"
    ASSET_GENERATE_THUMBNAILS_QUEUE_ALL = "AssetGenerateThumbnailsQueueAll"
    ASSET_GENERATE_THUMBNAILS = "AssetGenerateThumbnails"
    AUDIT_LOG_CLEANUP = "AuditLogCleanup"
    AUDIT_TABLE_CLEANUP = "AuditTableCleanup"
    DATABASE_BACKUP = "DatabaseBackup"
    FACIAL_RECOGNITION_QUEUE_ALL = "FacialRecognitionQueueAll"
    FACIAL_RECOGNITION = "FacialRecognition"
    FILE_DELETE = "FileDelete"
    FILE_MIGRATION_QUEUE_ALL = "FileMigrationQueueAll"
    LIBRARY_DELETE_CHECK = "LibraryDeleteCheck"
    LIBRARY_DELETE = "LibraryDelete"
    LIBRARY_REMOVE_ASSET = "LibraryRemoveAsset"
    LIBRARY_SCAN_ASSETS_QUEUE_ALL = "LibraryScanAssetsQueueAll"
    LIBRARY_SYNC_ASSETS = "LibrarySyncAssets"
    LIBRARY_SYNC_FILES_QUEUE_ALL = "LibrarySyncFilesQueueAll"
    LIBRARY_SYNC_FILES = "LibrarySyncFiles"
    LIBRARY_SCAN_QUEUE_ALL = "LibraryScanQueueAll"
    MEMORY_CLEANUP = "MemoryCleanup"
    MEMORY_GENERATE = "MemoryGenerate"
    NOTIFICATIONS_CLEANUP = "NotificationsCleanup"
    NOTIFY_USER_SIGNUP = "NotifyUserSignup"
    NOTIFY_ALBUM_INVITE = "NotifyAlbumInvite"
    NOTIFY_ALBUM_UPDATE = "NotifyAlbumUpdate"
    USER_DELETE = "UserDelete"
    USER_DELETE_CHECK = "UserDeleteCheck"
    USER_SYNC_USAGE = "UserSyncUsage"
    PERSON_CLEANUP = "PersonCleanup"
    PERSON_FILE_MIGRATION = "PersonFileMigration"
    PERSON_GENERATE_THUMBNAIL = "PersonGenerateThumbnail"
    SESSION_CLEANUP = "SessionCleanup"
    SEND_MAIL = "SendMail"
    SIDECAR_QUEUE_ALL = "SidecarQueueAll"
    SIDECAR_CHECK = "SidecarCheck"
    SIDECAR_WRITE = "SidecarWrite"
    SMART_SEARCH_QUEUE_ALL = "SmartSearchQueueAll"
    SMART_SEARCH = "SmartSearch"
    STORAGE_TEMPLATE_MIGRATION = "StorageTemplateMigration"
    STORAGE_TEMPLATE_MIGRATION_SINGLE = "StorageTemplateMigrationSingle"
    TAG_CLEANUP = "TagCleanup"
    VERSION_CHECK = "VersionCheck"
    OCR_QUEUE_ALL = "OcrQueueAll"
    OCR = "Ocr"
    WORKFLOW_RUN = "WorkflowRun"


class QueueStatisticsDto(BaseModel):
    """Queue job counts."""

    active: int = Field(..., description="Number of active jobs")
    completed: int = Field(..., description="Number of completed jobs")
    delayed: int = Field(..., description="Number of delayed jobs")
    failed: int = Field(..., description="Number of failed jobs")
    paused: int = Field(..., description="Number of paused jobs")
    waiting: int = Field(..., description="Number of waiting jobs")


class QueueResponseDto(BaseModel):
    """Single queue status (new API)."""

    name: QueueName | str = Field(..., description="Queue name")
    isPaused: bool = Field(..., description="Whether the queue is paused")
    statistics: QueueStatisticsDto = Field(..., description="Job counts")


class QueueStatusLegacyDto(BaseModel):
    """Legacy queue status."""

    isActive: bool = Field(..., description="Whether the queue has running jobs")
    isPaused: bool = Field(..., description="Whether the queue is paused")


class QueueResponseLegacyDto(BaseModel):
    """Legacy single queue response."""

    jobCounts: QueueStatisticsDto = Field(..., description="Job counts")
    queueStatus: QueueStatusLegacyDto = Field(..., description="Queue status")


class QueueCommandDto(BaseModel):
    """Queue command request."""

    command: QueueCommand = Field(..., description="Queue command to execute")
    force: bool | None = Field(None, description="Force the command execution")


class QueueDeleteDto(BaseModel):
    """Request to empty/delete queue jobs."""

    failed: bool | None = Field(None, description="If true, also remove failed jobs")


class QueueJobResponseDto(BaseModel):
    """Single job in a queue."""

    id: str | None = Field(None, description="Job ID")
    name: JobName | str = Field(..., description="Job name")
    data: dict[str, Any] = Field(..., description="Job data payload")
    timestamp: int = Field(..., description="Job creation timestamp")


class QueueUpdateDto(BaseModel):
    """Update queue (e.g. pause/resume)."""

    isPaused: bool | None = Field(None, description="Whether to pause the queue")


class QueuesResponseLegacyDto(BaseModel):
    """Legacy response: all queues by name."""

    backgroundTask: QueueResponseLegacyDto
    backupDatabase: QueueResponseLegacyDto
    duplicateDetection: QueueResponseLegacyDto
    editor: QueueResponseLegacyDto
    faceDetection: QueueResponseLegacyDto
    facialRecognition: QueueResponseLegacyDto
    library: QueueResponseLegacyDto
    metadataExtraction: QueueResponseLegacyDto
    migration: QueueResponseLegacyDto
    notifications: QueueResponseLegacyDto
    ocr: QueueResponseLegacyDto
    search: QueueResponseLegacyDto
    sidecar: QueueResponseLegacyDto
    smartSearch: QueueResponseLegacyDto
    storageTemplateMigration: QueueResponseLegacyDto
    thumbnailGeneration: QueueResponseLegacyDto
    videoConversion: QueueResponseLegacyDto
    workflow: QueueResponseLegacyDto
