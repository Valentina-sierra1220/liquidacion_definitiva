import psycopg2
from database.secret_config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Este método se puede usar si deseas crear tablas desde Python (opcional)."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        identificacion VARCHAR(20) PRIMARY KEY,
        nombre TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario NUMERIC(12,2) NOT NULL,
        fecha_ingreso DATE NOT NULL,
        vacaciones_tomadas INTEGER NOT NULL,
        despido_sin_causa BOOLEAN NOT NULL,
        creado_en TIMESTAMP DEFAULT now()
    );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
