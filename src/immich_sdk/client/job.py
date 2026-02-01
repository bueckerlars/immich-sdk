"""Jobs API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class JobsClient:
    """Client for Immich Jobs endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the jobs client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def create_job(self, dto: dict[str, object]) -> None:
        """Run a specific job. Most jobs are queued automatically.

        :param dto: Dict with job type and options.
        """
        self._base.post("/api/jobs", json=dto)

    def get_queues_legacy(self) -> dict[str, object]:
        """Retrieve the counts of the current queue and current status. (Deprecated)

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/jobs")
        return resp.json()

    def run_queue_command_legacy(
        self, name: str, dto: dict[str, object]
    ) -> dict[str, object]:
        """Queue all assets for a specific job type. (Deprecated)

        :param name: Job type name.
        :param dto: Dict with job options.
        :returns: Raw response dict from the API.
        """
        resp = self._base.put(f"/api/jobs/{name}", json=dto)
        return resp.json()
