from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    # Chat model secret
    gemini_api_key: str = ""

    # MongoDB secret
    mongodb_url: str = ""
    mongodb_db_name: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()


def get_settings() -> Settings:

    return settings
