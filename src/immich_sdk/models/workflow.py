"""Workflow-related DTOs."""

from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class PluginTriggerType(str, Enum):
    """Workflow trigger type (plugin)."""

    ASSET_CREATE = "AssetCreate"
    PERSON_RECOGNIZED = "PersonRecognized"


class WorkflowActionItemDto(BaseModel):
    """Workflow action item (create/update)."""

    pluginActionId: UUID = Field(..., description="Plugin action ID")
    actionConfig: dict[str, Any] | None = Field(
        None, description="Action configuration"
    )


class WorkflowFilterItemDto(BaseModel):
    """Workflow filter item (create/update)."""

    pluginFilterId: UUID = Field(..., description="Plugin filter ID")
    filterConfig: dict[str, Any] | None = Field(
        None, description="Filter configuration"
    )


class WorkflowActionResponseDto(BaseModel):
    """Workflow action response."""

    id: str = Field(..., description="Action ID")
    workflowId: str = Field(..., description="Workflow ID")
    pluginActionId: str = Field(..., description="Plugin action ID")
    order: float = Field(..., description="Action order")
    actionConfig: dict[str, Any] | None = Field(
        None, description="Action configuration"
    )


class WorkflowFilterResponseDto(BaseModel):
    """Workflow filter response."""

    id: str = Field(..., description="Filter ID")
    workflowId: str = Field(..., description="Workflow ID")
    pluginFilterId: str = Field(..., description="Plugin filter ID")
    order: float = Field(..., description="Filter order")
    filterConfig: dict[str, Any] | None = Field(
        None, description="Filter configuration"
    )


class WorkflowCreateDto(BaseModel):
    """DTO for creating a workflow."""

    name: str = Field(..., description="Workflow name")
    triggerType: str = Field(..., description="Workflow trigger type")
    actions: list[WorkflowActionItemDto] = Field(..., description="Workflow actions")
    filters: list[WorkflowFilterItemDto] = Field(..., description="Workflow filters")
    description: str | None = Field(None, description="Workflow description")
    enabled: bool | None = Field(None, description="Workflow enabled")


class WorkflowUpdateDto(BaseModel):
    """DTO for updating a workflow."""

    name: str | None = Field(None, description="Workflow name")
    triggerType: str | None = Field(None, description="Workflow trigger type")
    actions: list[WorkflowActionItemDto] | None = Field(
        None, description="Workflow actions"
    )
    filters: list[WorkflowFilterItemDto] | None = Field(
        None, description="Workflow filters"
    )
    description: str | None = Field(None, description="Workflow description")
    enabled: bool | None = Field(None, description="Workflow enabled")


class WorkflowResponseDto(BaseModel):
    """Workflow response DTO."""

    id: str = Field(..., description="Workflow ID")
    name: str | None = Field(None, description="Workflow name")
    description: str = Field(..., description="Workflow description")
    enabled: bool = Field(..., description="Workflow enabled")
    triggerType: str = Field(..., description="Workflow trigger type")
    ownerId: str = Field(..., description="Owner user ID")
    createdAt: str = Field(..., description="Creation date")
    actions: list[WorkflowActionResponseDto] = Field(
        ..., description="Workflow actions"
    )
    filters: list[WorkflowFilterResponseDto] = Field(
        ..., description="Workflow filters"
    )
