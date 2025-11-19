from typing import Any
from pydantic import BaseModel, Field, field_validator
from utils.password import is_secure


class PasswordSchema(BaseModel):
    password: str = Field()

    @field_validator("password")
    @classmethod
    def validate(cls, value: Any):
        if not is_secure(value):
            raise ValueError("La contraseña no es segura")
        return value
