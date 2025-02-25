import os
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Extension Pop-up Powered AI"
    PROJECT_DESCRIPTION: str = "API for the Extension Pop-up Powered AI Chrome extension"
    API_VERSION: str = "0.1.0"
    
    CORS_ORIGINS: List[str] = ["*"]  # In production, restrict to your extension's origin
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # Security settings
    SECRET_KEY: str = "your-secret-key"  # Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week
    
    # API Keys for various services
    GOOGLE_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    BING_API_KEY: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

settings = Settings()
