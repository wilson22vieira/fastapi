from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://wilson:134679@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = "JmwFqm6355TpWGqgQEutQ7DxaHkfww6gYcPuk3oiNtw"
    """ # Gera token

            import secrets

            token: str = secrets.token_urlsafe(32)

        Exemplo:
        
        Abrir o terminal do python

        Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import secrets
        >>> token: str = secrets.token_urlsafe(32)
        >>> token
        'JmwFqm6355TpWGqgQEutQ7DxaHkfww6gYcPuk3oiNtw'
        >>>
    """

    ALGORITHM: str = "HS256"
    # 60 minutos * 24 horas * 7 dias = 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
