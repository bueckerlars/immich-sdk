"""Immich API client and sub-clients."""

from immich_sdk.client._base import BaseClient
from immich_sdk.client.activity import ActivitiesClient
from immich_sdk.client.album import AlbumsClient
from immich_sdk.client.api_key import APIKeysClient
from immich_sdk.client.asset import AssetsClient
from immich_sdk.client.auth import AuthClient
from immich_sdk.client.auth_admin import AuthAdminClient
from immich_sdk.client.database_backup import DatabaseBackupClient
from immich_sdk.client.download import DownloadClient
from immich_sdk.client.duplicate import DuplicatesClient
from immich_sdk.client.face import FacesClient
from immich_sdk.client.job import JobsClient
from immich_sdk.client.library import LibrariesClient
from immich_sdk.client.map_ import MapClient
from immich_sdk.client.maintenance import MaintenanceClient
from immich_sdk.client.memory import MemoriesClient
from immich_sdk.client.notification import NotificationsClient
from immich_sdk.client.oauth import OAuthClient
from immich_sdk.client.partner import PartnersClient
from immich_sdk.client.person import PeopleClient
from immich_sdk.client.plugin import PluginsClient
from immich_sdk.client.queue import QueueClient
from immich_sdk.client.search import SearchClient
from immich_sdk.client.server import ServerClient
from immich_sdk.client.shared_link import SharedLinksClient
from immich_sdk.client.sync import SyncClient
from immich_sdk.client.system_config import SystemConfigClient
from immich_sdk.client.system_metadata import SystemMetadataClient
from immich_sdk.client.tag import TagsClient
from immich_sdk.client.timeline import TimelineClient
from immich_sdk.client.trash import TrashClient
from immich_sdk.client.user import UserClient
from immich_sdk.client.user_admin import UserAdminClient
from immich_sdk.client.view import ViewClient
from immich_sdk.client.workflow import WorkflowClient


class ImmichClient:
    """Main client for the Immich API.

    Create with base_url and api_key, then use sub-clients for each endpoint group
    (e.g. :class:`AlbumsClient`, :class:`AssetsClient`, :class:`AuthClient`).
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        timeout: float = 30.0,
        max_retries: int = 3,
        enable_logging: bool = True,
    ) -> None:
        """Initialize the Immich client.

        :param base_url: Immich server URL without trailing slash (e.g. https://immich.example.com).
        :param api_key: API key for authentication (x-api-key header).
        :param timeout: Request timeout in seconds.
        :param max_retries: Maximum number of retries for 429/5xx and connection errors.
        :param enable_logging: Whether to log requests and responses.
        """
        self._base = BaseClient(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            max_retries=max_retries,
            enable_logging=enable_logging,
        )
        self.activities = ActivitiesClient(self._base)
        self.albums = AlbumsClient(self._base)
        self.api_keys = APIKeysClient(self._base)
        self.assets = AssetsClient(self._base)
        self.auth = AuthClient(self._base)
        self.auth_admin = AuthAdminClient(self._base)
        self.database_backup = DatabaseBackupClient(self._base)
        self.download = DownloadClient(self._base)
        self.duplicates = DuplicatesClient(self._base)
        self.faces = FacesClient(self._base)
        self.jobs = JobsClient(self._base)
        self.libraries = LibrariesClient(self._base)
        self.map = MapClient(self._base)
        self.maintenance = MaintenanceClient(self._base)
        self.memories = MemoriesClient(self._base)
        self.notifications = NotificationsClient(self._base)
        self.oauth = OAuthClient(self._base)
        self.partners = PartnersClient(self._base)
        self.people = PeopleClient(self._base)
        self.plugins = PluginsClient(self._base)
        self.queue = QueueClient(self._base)
        self.search = SearchClient(self._base)
        self.server = ServerClient(self._base)
        self.shared_links = SharedLinksClient(self._base)
        self.sync = SyncClient(self._base)
        self.system_config = SystemConfigClient(self._base)
        self.system_metadata = SystemMetadataClient(self._base)
        self.tags = TagsClient(self._base)
        self.timeline = TimelineClient(self._base)
        self.trash = TrashClient(self._base)
        self.user = UserClient(self._base)
        self.user_admin = UserAdminClient(self._base)
        self.view = ViewClient(self._base)
        self.workflow = WorkflowClient(self._base)


__all__ = [
    "BaseClient",
    "ImmichClient",
    "ActivitiesClient",
    "AlbumsClient",
    "APIKeysClient",
    "AssetsClient",
    "AuthClient",
    "AuthAdminClient",
    "DatabaseBackupClient",
    "DownloadClient",
    "DuplicatesClient",
    "FacesClient",
    "JobsClient",
    "LibrariesClient",
    "MapClient",
    "MaintenanceClient",
    "MemoriesClient",
    "NotificationsClient",
    "OAuthClient",
    "PartnersClient",
    "PeopleClient",
    "PluginsClient",
    "QueueClient",
    "SearchClient",
    "ServerClient",
    "SharedLinksClient",
    "SyncClient",
    "SystemConfigClient",
    "SystemMetadataClient",
    "TagsClient",
    "TimelineClient",
    "TrashClient",
    "UserClient",
    "UserAdminClient",
    "ViewClient",
    "WorkflowClient",
]
