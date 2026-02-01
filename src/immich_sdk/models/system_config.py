"""System config DTOs."""

from pydantic import BaseModel, ConfigDict


class SystemConfigDto(BaseModel):
    """System configuration (nested structure varies by API version)."""

    model_config = ConfigDict(extra="allow")


class SystemConfigUpdateDto(BaseModel):
    """System config update (partial)."""

    model_config = ConfigDict(extra="allow")


class StorageTemplateOptionsDto(BaseModel):
    """Storage template options response."""

    model_config = ConfigDict(extra="allow")
