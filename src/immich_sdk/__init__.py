import importlib.metadata

from immich_sdk.client import ImmichClient
from immich_sdk.exception import (
    ImmichAPIException,
    ImmichHTTPError,
    ImmichValidationError,
)

__modulename__: str = __name__.split(".")[0]
__version__ = importlib.metadata.version("immich-sdk")

__all__ = [
    "ImmichClient",
    "ImmichAPIException",
    "ImmichHTTPError",
    "ImmichValidationError",
    "__version__",
]
