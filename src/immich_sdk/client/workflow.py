"""Workflow API client."""

from __future__ import annotations

from uuid import UUID

from immich_sdk.client._base import BaseClient


class WorkflowClient:
    """Client for Immich Workflow endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the workflow client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_workflows(self) -> list[dict[str, object]]:
        """Retrieve all workflows.

        :returns: List of workflow dicts.
        """
        resp = self._base.get("/api/workflows")
        return resp.json()

    def create_workflow(self, dto: dict[str, object]) -> dict[str, object]:
        """Create a new workflow.

        :param dto: Dict with workflow data.
        :returns: Raw response dict from the API.
        """
        resp = self._base.post("/api/workflows", json=dto)
        return resp.json()

    def get_workflow(self, id: UUID | str) -> dict[str, object]:
        """Retrieve a workflow by ID.

        :param id: Workflow ID (UUID or string).
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/workflows/{id}")
        return resp.json()

    def update_workflow(
        self, id: UUID | str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Update a workflow.

        :param id: Workflow ID (UUID or string).
        :param dto: Dict with fields to update.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/workflows/{id}", json=dto)
        return resp.json()

    def delete_workflow(self, id: UUID | str) -> None:
        """Delete a workflow.

        :param id: Workflow ID (UUID or string).
        """
        self._base.delete(f"/api/workflows/{id}")
