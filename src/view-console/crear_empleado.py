import sys
sys.path.append("src")

from model.empleado_model import Empleado
from controller.empleado_controller import EmpleadoController

# Insertar un Empleado en la tabla
empleado = Empleado(
    identificacion="",
    nombre="",
    cargo="",
    salario=0,
    fecha_ingreso="",
    vacaciones_tomadas=0,
    despido_sin_causa=False
)

print("Por favor ingrese los datos del empleado que desea crear")

empleado.identificacion = input("Identificación: ")
empleado.nombre = input("Nombre: ")
empleado.cargo = input("Cargo: ")
empleado.salario = float(input("Salario: "))
empleado.fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ")
empleado.vacaciones_tomadas = int(input("Vacaciones tomadas (días): "))

despedido = input("¿Fue despedido sin causa? (S/N): ").strip().upper()
empleado.despido_sin_causa = True if despedido == "S" else False

EmpleadoController.insertar(empleado)

print("Empleado insertado correctamente!")
