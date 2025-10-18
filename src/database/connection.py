import psycopg2
from typing import Any, Dict
from database.secret_config import DB_CONFIG

def get_connection():
    """
    Retorna una conexión psycopg2 usando DB_CONFIG.
    Uso recomendado:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
    """
    required_keys = {"host", "dbname", "user", "password"}
    missing = required_keys - set(DB_CONFIG.keys())
    if missing:
        raise KeyError(f"Faltan claves en DB_CONFIG: {', '.join(sorted(missing))}")

    return psycopg2.connect(
        host=DB_CONFIG["host"],
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG.get("port", 5432),
    )
