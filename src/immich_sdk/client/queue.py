"""Queue API client."""

from __future__ import annotations

from typing import Any, cast

from immich_sdk.client._base import BaseClient
from immich_sdk.models.queue import (
    QueueJobResponseDto,
    QueueResponseDto,
    QueueUpdateDto,
)


class QueueClient:
    """Client for Immich Queue endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the queue client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_queues(self) -> list[QueueResponseDto]:
        """Retrieve all queues status.

        :returns: List of queue DTOs.
        """
        resp = self._base.get("/api/queue")
        data: object = resp.json()
        if isinstance(data, list):
            items: list[dict[str, Any]] = cast(list[dict[str, Any]], data)
            return [QueueResponseDto.model_validate(q) for q in items]
        # Legacy shape: object with queue names as keys, value has jobCounts + queueStatus
        result: list[QueueResponseDto] = []
        data_dict = cast(dict[str, dict[str, Any]], data)
        # QueueStatisticsDto requires all six fields; legacy jobCounts may omit some
        stats_defaults: dict[str, int] = {
            "active": 0,
            "completed": 0,
            "delayed": 0,
            "failed": 0,
            "paused": 0,
            "waiting": 0,
        }
        for name, v in data_dict.items():
            st: dict[str, Any] = v.get("queueStatus") or {}
            jc: dict[str, Any] = v.get("jobCounts") or {}
            statistics = {
                **stats_defaults,
                **{k: v for k, v in jc.items() if k in stats_defaults},
            }
            result.append(
                QueueResponseDto.model_validate(
                    {
                        "name": name,
                        "isPaused": st.get("isPaused", False),
                        "statistics": statistics,
                    }
                )
            )
        return result

    def get_queue(self, name: str) -> QueueResponseDto:
        """Retrieve a specific queue by name.

        :param name: Queue name.
        :returns: Queue DTO.
        """
        resp = self._base.get(f"/api/queue/{name}")
        return QueueResponseDto.model_validate(resp.json())

    def update_queue(self, name: str, dto: QueueUpdateDto) -> QueueResponseDto:
        """Update a queue (e.g. pause/resume).

        :param name: Queue name.
        :param dto: Queue update DTO.
        :returns: Updated queue DTO.
        """
        resp = self._base.put(
            f"/api/queue/{name}",
            json=dto.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return QueueResponseDto.model_validate(resp.json())

    def empty_queue(self, name: str) -> None:
        """Empty a queue.

        :param name: Queue name.
        """
        self._base.post(f"/api/queue/{name}/empty")

    def get_queue_jobs(
        self, name: str, params: dict[str, str | int | bool] | None = None
    ) -> list[QueueJobResponseDto]:
        """Get jobs in a queue.

        :param name: Queue name.
        :param params: Optional query parameters (e.g. status, limit).
        :returns: List of queue job DTOs.
        """
        resp = self._base.get(f"/api/queue/{name}/jobs", params=params or None)
        data = resp.json()
        if isinstance(data, dict) and "jobs" in data:
            jobs_list: list[dict[str, Any]] = cast(list[dict[str, Any]], data["jobs"])
        elif isinstance(data, list):
            jobs_list = cast(list[dict[str, Any]], data)
        else:
            jobs_list = []
        return [QueueJobResponseDto.model_validate(j) for j in jobs_list]
