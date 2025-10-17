from model.LiquidacionLaboral import calcular_total, InteresesNoPagosError
from controller.empleado_controller import EmpleadoController

class LiquidacionController:

    @staticmethod
    def calcular_liquidacion():
        id_emp = int(input("ID del empleado para calcular liquidación: "))
        emp = next((e for e in EmpleadoController.empleados if e["id"] == id_emp), None)

        if not emp:
            print("⚠️ Empleado no encontrado.\n")
            return

        try:
            total = calcular_total(
                emp["fecha_inicio"],
                emp["fecha_fin"],
                emp["salario"],
                emp["auxilio"],
                emp["vacaciones"],
                emp["despido"]
            )
            print(f"\n Total de liquidación para {emp['nombre']}: ${total:,.0f} COP\n")
        except InteresesNoPagosError:
            print(" No se pagaron intereses (error controlado).")
        except Exception as e:
            print(f" Error al calcular la liquidación: {e}")
