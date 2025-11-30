from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name = "to do list"
    debug: bool = True
    database_url = "sqlite:///./to_do_list.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"

    class Config:
        env_file = ".env"
settings = Settings()