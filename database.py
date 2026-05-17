import sqlite3
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)

def _secret(key: str, default: str = "") -> str:
    try:
        import streamlit as st
        return st.secrets[key]
    except Exception:
        return os.getenv(key, default)

DB_PATH = _secret("DB_PATH", "schnellplaner.db")
ADMIN_PASSWORD = _secret("ADMIN_PASSWORD", "admin2026")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            situation TEXT,
            zielgruppe TEXT,
            startidee TEXT,
            thema TEXT,
            ziel TEXT,
            result_generated INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_lead(email: str, situation: str, zielgruppe: str,
              startidee: str, thema: str, ziel: str) -> int:
    conn = get_connection()
    cursor = conn.execute("""
        INSERT INTO leads (email, situation, zielgruppe, startidee, thema, ziel)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (email.strip().lower(), situation, zielgruppe, startidee, thema, ziel))
    lead_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return lead_id


def mark_result_generated(lead_id: int):
    conn = get_connection()
    conn.execute("UPDATE leads SET result_generated = 1 WHERE id = ?", (lead_id,))
    conn.commit()
    conn.close()


def get_all_leads() -> list[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM leads ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def email_exists(email: str) -> bool:
    conn = get_connection()
    row = conn.execute(
        "SELECT id FROM leads WHERE email = ?", (email.strip().lower(),)
    ).fetchone()
    conn.close()
    return row is not None
