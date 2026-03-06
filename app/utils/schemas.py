from pydantic import BaseModel, Field


class MissingRequest(BaseModel):
    number: int = Field(..., ge=1, le=100, description="Number to extract (1..100)")


class MissingResponse(BaseModel):
    extracted: int = Field(..., ge=1, le=100)
    missing: int = Field(..., ge=1, le=100)
    message: str
