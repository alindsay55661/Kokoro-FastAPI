from fastapi import HTTPException, Security, Header
from fastapi.security import APIKeyHeader

from .config import settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.api_secret_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    return api_key