import sqlite3
from app.src.utils.constants import DATABASE_FILE
from typing import List, Optional, Tuple
from app.src.models.hcc import HCC


DataType = List[Tuple[str, str, str]]


def create_database() -> None:
    """Creates the database and table if they do not exist.
    Drops the table if it already exists before creating a new one."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS icd_codes")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS icd_codes (
        code TEXT,
        description TEXT,
        tags TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_data(data: DataType) -> None:
    """Inserts data into the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO icd_codes (code, description, tags) VALUES (?, ?, ?)", data
    )
    conn.commit()
    conn.close()


def get_by_code(code: str) -> Optional[HCC]:
    """Fetches a record by code and returns it as an ICDCode model."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT code, description, tags FROM icd_codes WHERE code = ?", (code,)
    )
    record = cursor.fetchone()
    conn.close()

    return (
        HCC(code=record[0], description=record[1], tags=record[2]) if record else None
    )
