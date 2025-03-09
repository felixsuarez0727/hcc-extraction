from pydantic import BaseModel
from typing import Optional


class HCC(BaseModel):
    """Model representing HCC relevant codes."""

    code: str
    description: Optional[str] = None
    tags: Optional[str] = None
