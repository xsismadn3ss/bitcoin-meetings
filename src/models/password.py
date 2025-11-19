from typing import Any
from pydantic import BaseModel, Field, field_validator
from utils.password import is_secure


class PasswordSchema(BaseModel):
    password: str = Field(min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate(cls, value: Any):
        print(is_secure(value))
        if not is_secure(value):
            raise ValueError("La contraseña no es segura")
        return value
