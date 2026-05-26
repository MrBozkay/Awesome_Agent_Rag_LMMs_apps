from dataclasses import dataclass
from typing import Annotated
from pydantic import BaseModel, Field, field_validator

from pydantic_ai_triage.database import MockDatabase


class TriageOutput(BaseModel):
    response_text: str = Field(description="Hastaya iletilecek tıbbi/tavsiye mesajı.")
    escalate: bool = Field(description="Durum bir üst birime/hemşireye aktarılmalı mı?")
    urgency: int = Field(description="1 ile 10 arasında aciliyet seviyesi.")

    @field_validator("urgency")
    @classmethod
    def validate_urgency(cls, v: int) -> int:
        if v < 1 or v > 10:
            raise ValueError("urgency must be between 1 and 10")
        return v


@dataclass
class TriageDependencies:
    patient_id: int
    db: MockDatabase
