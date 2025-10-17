CREATE TABLE IF NOT EXISTS empleados (
  identificacion VARCHAR(20) PRIMARY KEY NOT NULL,
  nombre TEXT NOT NULL,
  cargo TEXT NOT NULL,
  salario DECIMAL NOT NULL,
  fecha_ingreso DATE NOT NULL,
  vacaciones_tomadas INT DEFAULT 0,
  despido_sin_causa BOOLEAN DEFAULT FALSE,
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
