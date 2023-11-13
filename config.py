from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str  # you must need environment variable bot_token = secret token from BotFather. Case doesn't matter


setting = Setting()
