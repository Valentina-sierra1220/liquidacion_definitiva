import unittest
import sys
sys.path.append("src")

from controller.empleado_controller import EmpleadoController
from model.empleado_model import Empleado

class TestEmpleadoController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        EmpleadoController.eliminar_tabla()
        EmpleadoController.crear_tabla()

    def test_insertar_y_buscar_empleado_1(self):
        empleado = Empleado(
            identificacion="1001",
            nombre="Carlos",
            cargo="Ingeniero",
            salario=4500000,
            fecha_ingreso="2020-01-15",
            vacaciones_tomadas=5,
            despido_sin_causa=True
        )
        EmpleadoController.insertar_empleado(empleado)
        buscado = EmpleadoController.buscar_empleado("1001")
        self.assertTrue(buscado.is_equal(empleado))

    def test_insertar_y_buscar_empleado_2(self):
        empleado = Empleado(
            identificacion="2002",
            nombre="Laura",
            cargo="Contadora",
            salario=5200000,
            fecha_ingreso="2018-06-01",
            vacaciones_tomadas=0,
            despido_sin_causa=False
        )
        EmpleadoController.insertar_empleado(empleado)
        buscado = EmpleadoController.buscar_empleado("2002")
        self.assertTrue(buscado.is_equal(empleado))

    def test_insertar_y_buscar_empleado_3(self):
        empleado = Empleado(
            identificacion="3003",
            nombre="Jorge",
            cargo="Administrador",
            salario=6000000,
            fecha_ingreso="2017-03-10",
            vacaciones_tomadas=12,
            despido_sin_causa=True
        )
        EmpleadoController.insertar_empleado(empleado)
        buscado = EmpleadoController.buscar_empleado("3003")
        self.assertTrue(buscado.is_equal(empleado))

if __name__ == '__main__':
    unittest.main()
