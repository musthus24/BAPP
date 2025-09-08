from pydantic import BaseSettings
class Settings(BaseSettings):
    APP_ENV: str = "dev"
    DB_URL; str = "sqlite:///./data.sqlite3"
    class Config:
        env_file = ".env"

settings = Settings()