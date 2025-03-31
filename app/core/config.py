from pathlib import Path

from pydantic import BaseModel, computed_field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parent.parent.parent


class DBSettings(BaseModel):
    host: str
    port: str
    name: str
    user: str
    password: SecretStr

    echo: bool = False
    pool_size: int = 100
    max_overflow: int = 0
    pool_pre_ping: bool = False

    @computed_field
    def url(self) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / '.env',
        env_nested_delimiter='__',
        case_sensitive=False,
        extra='ignore',
    )

    db: DBSettings


settings = Settings()
