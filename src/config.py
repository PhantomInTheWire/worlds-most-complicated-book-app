from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL : str
    JWT_SECRET:str
    JWT_ALGORITHM:str
    REFRESH_TOKEN_EXPIRY: int
    REDIS_PORT: int
    REDIS_HOST: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings()