"""Trash-related DTOs."""

from pydantic import BaseModel, Field


class TrashResponseDto(BaseModel):
    """Trash summary response (e.g. count)."""

    count: int = Field(..., description="Number of items in trash")
