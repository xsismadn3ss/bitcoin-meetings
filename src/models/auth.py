from typing import Any
from pydantic import BaseModel, Field, field_validator
from utils.email import validate_email


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
        if not validate_email(value):
            raise ValueError("El formato de correo electrónico es inválido")
        return value
