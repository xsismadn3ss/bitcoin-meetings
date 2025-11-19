from typing import Any
from pydantic import BaseModel, Field
from .email import EmailSchema


class AuthLoginDto(EmailSchema, BaseModel):
    password: str = Field(
        ...,
        min_length=6,
        max_length=128,
        json_schema_extra={
            "error_message": "La contraseña debe tener entre 6 y 128 carácteres"
        },
    )
