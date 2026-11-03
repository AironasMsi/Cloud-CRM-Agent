"""
Cloud CRM Agent - Environment Settings and Cloud VPS Configuration
"""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    HOST_ENVIRONMENT: str = "Oracle Cloud Infrastructure (Ubuntu 22.04 LTS)"
    DEPLOYMENT_REGION: str = "eu-frankfurt-1"
    SERVICE_DAEMON_NAME: str = "hero-operations.service"
    
    # Discord
    DISCORD_BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN", "MOCK_TOKEN_SHOWCASE")
    OPERATIONS_GUILD_ID: int = int(os.getenv("OPERATIONS_GUILD_ID", "123456789012345678"))
    
    # Email Bridge (IMAP & SMTP SSL)
    GMAIL_IMAP_SERVER: str = "imap.gmail.com"
    GMAIL_SMTP_SERVER: str = "smtp.gmail.com"
    EMAIL_POLL_INTERVAL_SEC: int = 45
    
    # Database
    DATABASE_PATH: str = "data/operations_crm.db"

config = AppConfig()
