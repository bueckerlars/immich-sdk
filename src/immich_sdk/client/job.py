"""Jobs API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient
from immich_sdk.models.job import JobCreateDto
from immich_sdk.models.queue import (
    QueuesResponseLegacyDto,
    QueueCommandDto,
    QueueResponseLegacyDto,
)


class JobsClient:
    """Client for Immich Jobs endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the jobs client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def create_job(self, dto: JobCreateDto) -> None:
        """Run a specific job. Most jobs are queued automatically.

        :param dto: Job create DTO (manual job name).
        """
        self._base.post(
            "/api/jobs", json=dto.model_dump(by_alias=True, exclude_none=True)
        )

    def get_queues_legacy(self) -> QueuesResponseLegacyDto:
        """Retrieve the counts of the current queue and current status. (Deprecated)

        :returns: Legacy queues response.
        """
        resp = self._base.get("/api/jobs")
        return QueuesResponseLegacyDto.model_validate(resp.json())

    def run_queue_command_legacy(
        self, name: str, dto: QueueCommandDto
    ) -> QueueResponseLegacyDto:
        """Queue all assets for a specific job type. (Deprecated)

        :param name: Job type name.
        :param dto: Queue command DTO.
        :returns: Legacy queue response for that queue.
        """
        resp = self._base.put(
            f"/api/jobs/{name}",
            json=dto.model_dump(by_alias=True, exclude_none=True),
        )
        return QueueResponseLegacyDto.model_validate(resp.json())
