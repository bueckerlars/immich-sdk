"""Workflow API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient
from immich_sdk.models.workflow import (
    WorkflowCreateDto,
    WorkflowResponseDto,
    WorkflowUpdateDto,
)


class WorkflowClient:
    """Client for Immich Workflow endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the workflow client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_workflows(self) -> list[WorkflowResponseDto]:
        """Retrieve all workflows.

        :returns: List of workflow DTOs.
        """
        resp = self._base.get("/api/workflows")
        return [WorkflowResponseDto.model_validate(w) for w in resp.json()]

    def create_workflow(self, dto: WorkflowCreateDto) -> WorkflowResponseDto:
        """Create a new workflow.

        :param dto: Workflow create DTO.
        :returns: Created workflow DTO.
        """
        resp = self._base.post(
            "/api/workflows",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowResponseDto.model_validate(resp.json())

    def get_workflow(self, id: UUID | str) -> WorkflowResponseDto:
        """Retrieve a workflow by ID.

        :param id: Workflow ID (UUID or string).
        :returns: Workflow DTO.
        """
        resp = self._base.get(f"/api/workflows/{id}")
        return WorkflowResponseDto.model_validate(resp.json())

    def update_workflow(
        self, id: UUID | str, dto: WorkflowUpdateDto
    ) -> WorkflowResponseDto:
        """Update a workflow.

        :param id: Workflow ID (UUID or string).
        :param dto: Workflow update DTO.
        :returns: Updated workflow DTO.
        """
        resp = self._base.put(
            f"/api/workflows/{id}",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowResponseDto.model_validate(resp.json())

    def delete_workflow(self, id: UUID | str) -> None:
        """Delete a workflow.

        :param id: Workflow ID (UUID or string).
        """
        self._base.delete(f"/api/workflows/{id}")
