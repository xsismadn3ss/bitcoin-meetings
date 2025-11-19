from typing import Any
from pydantic import BaseModel, Field, field_validator
import re

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


class AuthLoginDto(BaseModel):
    email: str = Field(..., description="Correo electrónico valido")
    password: str = Field(
        ...,
        min_length=6,
        max_length=128,
        json_schema_extra={
            "error_message": "La contraseña debe tener entre 6 y 128 carácteres"
        },
    )

    @field_validator("email")
    @classmethod
    def validate(cls, value: Any):
        if not re.match(EMAIL_REGEX, value):
            raise ValueError("El formato de correo electrónico es inválido")
        return value
