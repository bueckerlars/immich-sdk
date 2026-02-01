"""Plugin-related DTOs."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class PluginContextType(str, Enum):
    """Plugin context type."""

    ASSET = "asset"
    ALBUM = "album"
    PERSON = "person"


class PluginTriggerType(str, Enum):
    """Plugin trigger type."""

    ASSET_CREATE = "AssetCreate"
    PERSON_RECOGNIZED = "PersonRecognized"


class PluginActionResponseDto(BaseModel):
    """Plugin action response."""

    id: str = Field(..., description="Action ID")
    pluginId: str = Field(..., description="Plugin ID")
    title: str = Field(..., description="Action title")
    description: str = Field(..., description="Action description")
    methodName: str = Field(..., description="Method name")
    schema_: dict[str, Any] | None = Field(
        None, alias="schema", description="Action schema"
    )
    supportedContexts: list[PluginContextType | str] = Field(
        ..., description="Supported contexts"
    )


class PluginFilterResponseDto(BaseModel):
    """Plugin filter response."""

    id: str = Field(..., description="Filter ID")
    pluginId: str = Field(..., description="Plugin ID")
    title: str = Field(..., description="Filter title")
    description: str = Field(..., description="Filter description")
    methodName: str = Field(..., description="Method name")
    schema_: dict[str, Any] | None = Field(
        None, alias="schema", description="Filter schema"
    )
    supportedContexts: list[PluginContextType | str] = Field(
        ..., description="Supported contexts"
    )


class PluginTriggerResponseDto(BaseModel):
    """Plugin trigger response."""

    type: PluginTriggerType | str = Field(..., description="Trigger type")
    contextType: PluginContextType | str = Field(..., description="Context type")


class PluginResponseDto(BaseModel):
    """Plugin response."""

    id: str = Field(..., description="Plugin ID")
    name: str = Field(..., description="Plugin name")
    title: str = Field(..., description="Plugin title")
    description: str = Field(..., description="Plugin description")
    author: str = Field(..., description="Plugin author")
    version: str = Field(..., description="Plugin version")
    createdAt: str = Field(..., description="Creation date")
    updatedAt: str = Field(..., description="Last update date")
    actions: list[PluginActionResponseDto] = Field(..., description="Plugin actions")
    filters: list[PluginFilterResponseDto] = Field(..., description="Plugin filters")
