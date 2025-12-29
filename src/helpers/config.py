from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # تعريف المتغيرات
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    # الطريقة الحديثة لربط ملف الـ .env
    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()