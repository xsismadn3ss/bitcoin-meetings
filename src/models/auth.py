from pydantic import BaseModel, Field, EmailStr


class AuthLoginDto(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico valido")
    password: str = Field(..., min_length=6, max_length=128)
