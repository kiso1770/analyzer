from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Analyzer"
    db_host: str
    db_port: int = 5432
    db_user: str
    db_pass: str
    tg_bot_token: str
    binance_api_key: str
    binance_api_secret: str


    model_config = SettingsConfigDict(env_file=".env")