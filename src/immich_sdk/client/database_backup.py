"""Database Backups (admin) API client."""

from __future__ import annotations

from immich_sdk.client._base import BaseClient


class DatabaseBackupClient:
    """Client for Immich Database Backups (admin) endpoints. Uses :class:`BaseClient` for HTTP."""

    def __init__(self, base: BaseClient) -> None:
        """Initialize the database backup client.

        :param base: The shared :class:`BaseClient` instance.
        """
        self._base = base

    def list_database_backups(self) -> dict[str, object]:
        """Get the list of the successful and failed backups.

        :returns: Raw response dict from the API.
        """
        resp = self._base.get("/api/admin/database-backups")
        return resp.json()

    def delete_database_backup(self, dto: dict[str, object]) -> None:
        """Delete a backup by its filename.

        :param dto: Dict with backup filename to delete.
        """
        self._base.delete("/api/admin/database-backups", json=dto)

    def download_database_backup(self, filename: str) -> bytes:
        """Download the database backup file.

        :param filename: Backup filename.
        :returns: Raw backup file bytes.
        """
        resp = self._base.get(f"/api/admin/database-backups/{filename}")
        return resp.content

    def upload_database_backup(self, file: tuple[str, bytes]) -> None:
        """Upload .sql/.sql.gz file to restore backup from.

        :param file: Tuple of (filename, bytes).
        """
        self._base.post("/api/admin/database-backups/upload", files={"file": file})

    def start_database_restore_flow(self) -> None:
        """Put Immich into maintenance mode to restore a backup."""
        self._base.post("/api/admin/database-backups/start-restore")
