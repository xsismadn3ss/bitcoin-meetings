import httpx
from config.api import PREFIX
from models.auth import AuthLoginDto


async def login(email, password) -> dict:
    data = AuthLoginDto(email=email, password=password)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PREFIX}/auth/login",
            json=data.model_dump(),
            timeout=10.0,
        )
        response.raise_for_status()
        return response.json()
