import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MambaDoc AI"
    API_V1_STR: str = "/api/v1"
    UPLOAD_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "uploads")
    DATABASE_URL: str = "sqlite:///./mambadoc.db"
    EMBEDDING_MODEL_TAG: str = "BAAI/bge-small-en-v1.5"
    MODEL_TAG: str = "state-spaces/mamba-130m-hf"

    class Config:
        case_sensitive = True

settings = Settings()
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)