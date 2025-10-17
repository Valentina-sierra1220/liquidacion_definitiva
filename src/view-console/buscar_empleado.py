import sys
sys.path.append("src")

from controller.empleado_controller import EmpleadoController

try:
    cedula = input("Ingrese la identificación del empleado que desea buscar: ")
    empleado = EmpleadoController.buscar_por_cedula(cedula)
    print(f"Empleado encontrado: {empleado.nombre} - {empleado.cargo}")
except Exception as err:
    print("Error:")
    print(str(err))
