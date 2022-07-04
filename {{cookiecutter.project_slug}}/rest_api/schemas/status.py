from pydantic import BaseModel, Field


class Status(BaseModel):
    status: str = Field(..., description="Server Status")
