from typing import Any
from pydantic import BaseModel, Field, field_validator
from utils.email import validate_email


class EmailSchema(BaseModel):
    email: str = Field()

    @field_validator("email")
    @classmethod
    def validate(cls, value: Any):
        if not validate_email(value):
            raise ValueError("El formato de correo electrónico es inválido")
        return value
