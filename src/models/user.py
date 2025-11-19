from pydantic import BaseModel, Field
from .email import EmailSchema
from .password import PasswordSchema


class RegisterUserDto(EmailSchema, PasswordSchema, BaseModel):
    name: str = Field()
