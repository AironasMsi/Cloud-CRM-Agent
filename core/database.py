"""
Asynchronous SQLite Database Manager with Write-Ahead Logging (WAL) Mode
"""
import aiosqlite
from pathlib import Path
from config import config

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS leads (
    lead_id TEXT PRIMARY KEY,
    channel_name TEXT NOT NULL,
    channel_url TEXT NOT NULL,
    contact_email TEXT,
    assigned_operator TEXT,
    state TEXT NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS email_threads (
    message_id TEXT PRIMARY KEY,
    lead_id TEXT NOT NULL,
    sender TEXT NOT NULL,
    subject TEXT,
    body_snippet TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(lead_id) REFERENCES leads(lead_id)
);
"""

class DatabaseManager:
    def __init__(self, db_path: str = config.DATABASE_PATH):
        self.db_path = db_path

    async def initialize(self):
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        async with aiosqlite.connect(self.db_path) as db:
            await db.executescript(SCHEMA_SQL)
            await db.commit()
