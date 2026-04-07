from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://user:password@db:5432/mydatabase"
    SECRET_KEY: str = "super-secret-key"  # Change this in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
