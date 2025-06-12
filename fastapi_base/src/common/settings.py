from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URI: str
    DATABASE_URL: str
    DATABASE_DRIVER: str
    ENVIRONMENT: str = "development"
    APP_VERSION: str
    APP_TITLE: str
    APP_DESCRIPTION: str

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", str_strip_whitespace=True, str_min_length=1
    )


def get_settings():
    return Settings()


settings = get_settings()
