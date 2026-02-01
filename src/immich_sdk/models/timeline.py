"""Timeline-related DTOs."""

from pydantic import BaseModel, ConfigDict


class TimelineBucketRequestDto(BaseModel):
    """Request for timeline bucket(s) (structure may vary by API)."""

    model_config = ConfigDict(extra="allow")
