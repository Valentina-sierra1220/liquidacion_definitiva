import sys
sys.path.append("src")

import psycopg2
from model.empleado_model import Empleado
import secret_config


class EmpleadoController:

    @staticmethod
    def crear_tabla():
        """Crea la tabla empleados ejecutando el script SQL."""
        cursor = EmpleadoController.obtener_cursor()
        with open("sql/crear-empleados.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def borrar_tabla():
        """Elimina la tabla empleados si existe."""
        cursor = EmpleadoController.obtener_cursor()
        with open("sql/borrar-empleados.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def insertar(empleado: Empleado):
        """Inserta un objeto Empleado en la base de datos."""
        cursor = EmpleadoController.obtener_cursor()
        consulta = """
            INSERT INTO empleados (
                identificacion, nombre, cargo, salario, fecha_ingreso,
                vacaciones_tomadas, despido_sin_causa
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (
            empleado.identificacion,
            empleado.nombre,
            empleado.cargo,
            empleado.salario,
            empleado.fecha_ingreso,
            empleado.vacaciones_tomadas,
            empleado.despido_sin_causa
        ))
        cursor.connection.commit()

    @staticmethod
    def buscar_por_cedula(identificacion) -> Empleado:
        """Busca un empleado por su cédula y devuelve un objeto Empleado."""
        cursor = EmpleadoController.obtener_cursor()
        consulta = """
            SELECT identificacion, nombre, cargo, salario, fecha_ingreso,
                   vacaciones_tomadas, despido_sin_causa
            FROM empleados
            WHERE identificacion = %s
        """
        cursor.execute(consulta, (identificacion,))
        fila = cursor.fetchone()

        if fila:
            return Empleado(
                identificacion=fila[0],
                nombre=fila[1],
                cargo=fila[2],
                salario=fila[3],
                fecha_ingreso=fila[4],
                vacaciones_tomadas=fila[5],
                despido_sin_causa=fila[6]
            )
        else:
            return None

    @staticmethod
    def obtener_cursor():
        """Establece conexión a la base de datos y retorna un cursor."""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        return connection.cursor()
