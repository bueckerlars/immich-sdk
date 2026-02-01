"""View-related DTOs."""

from pydantic import BaseModel, ConfigDict


class ViewSettingsDto(BaseModel):
    """User view settings (structure may vary by API version). Accepts any keys."""

    model_config = ConfigDict(extra="allow")
