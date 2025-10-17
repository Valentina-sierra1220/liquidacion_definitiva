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
