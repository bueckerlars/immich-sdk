"""Queue API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class QueueClient:
    """Client for Immich Queue endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the queue client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def get_queues(self) -> dict[str, object]:
        """Retrieve all queues status.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/queue")
        return resp.json()

    def get_queue(self, name: str) -> dict[str, object]:
        """Retrieve a specific queue by name.

        :param name: Queue name.
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/queue/{name}")
        return resp.json()

    def update_queue(self, name: str, dto: dict[str, object]) -> dict[str, object]:
        """Update a queue (e.g. pause/resume).

        :param name: Queue name.
        :param dto: Dict with queue options.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/queue/{name}", json=dto)
        return resp.json()

    def empty_queue(self, name: str) -> None:
        """Empty a queue.

        :param name: Queue name.
        """
        self._base.post(f"/api/queue/{name}/empty")

    def get_queue_jobs(
        self, name: str, params: dict[str, object] | None = None
    ) -> dict[str, object]:
        """Get jobs in a queue.

        :param name: Queue name.
        :param params: Optional query parameters.
        :returns: Raw response dict from the API.
        """
        resp = self._base.get(f"/api/queue/{name}/jobs", params=params or None)
        return resp.json()
