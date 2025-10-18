# src/main.py
from datetime import date
from src.controller.empleado_controller import EmpleadoController
from src.controller.liquidacion_controller import calcular_liquidacion_de_empleado
from src.database.connection import get_connection

def probar_conexion():
    """Verifica que la conexión a la base de datos funcione."""
    try:
        conn = get_connection()
        print("✅ Conexión exitosa a la base de datos.")
        conn.close()
    except Exception as e:
        print("❌ Error de conexión:", e)

def menu():
    print("\n===== 💼 LIQUIDACIÓN DEFINITIVA LABORAL =====")
    print("1. Insertar empleado")
    print("2. Buscar empleado")
    print("3. Calcular liquidación")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion.strip()

def run():
    probar_conexion()
    while True:
        opcion = menu()

        if opcion == "1":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario mensual: "))
            fecha_ingreso = input("Fecha de ingreso (AAAA-MM-DD): ")
            vacaciones = int(input("Vacaciones tomadas (0 si ninguna): "))
            despido = input("¿Despedido sin justa causa? (S/N): ").strip().upper() == "S"

            EmpleadoController.insertar_empleado(
                identificacion,
                nombre,
                cargo,
                salario,
                fecha_ingreso,
                vacaciones,
                despido,
            )
            print("✅ Empleado insertado correctamente.")

        elif opcion == "2":
            cedula = input("Ingrese cédula del empleado: ")
            emp = EmpleadoController.buscar_por_cedula(cedula)
            if emp:
                print(f"👤 {emp.nombre} | Cargo: {emp.cargo} | Salario: {emp.salario}")
            else:
                print("⚠️ No se encontró el empleado.")

        elif opcion == "3":
            cedula = input("Ingrese cédula del empleado: ")
            anio, mes, dia = map(int, input("Fecha final (AAAA-MM-DD): ").split("-"))
            fecha_fin = date(anio, mes, dia)
            try:
                resultado = calcular_liquidacion_de_empleado(cedula, fecha_fin)
                print("\n💰 LIQUIDACIÓN CALCULADA:")
                for k, v in resultado.items():
                    print(f" - {k.capitalize()}: {v}")
            except Exception as e:
                print("❌ Error al calcular la liquidación:", e)

        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    run()
