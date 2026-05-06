from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PROCESSMINE_", env_file=".env")

    anthropic_api_key: str = ""
    model: str = "claude-sonnet-4-6"
    db_url: str = "sqlite:///processmine.db"
    vault_root: str = "vault"
    log_level: str = "INFO"


settings = Settings()
