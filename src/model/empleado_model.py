from datetime import date

class Empleado:
    """
    Pertenece a la capa de Reglas de Negocio (Model)

    Representa a un empleado registrado en la aplicación de Liquidación Definitiva.
    """

    def __init__(self, identificacion, nombre, cargo, salario, fecha_ingreso, vacaciones_tomadas, despido_sin_causa):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.fecha_ingreso = fecha_ingreso
        self.vacaciones_tomadas = vacaciones_tomadas
        self.despido_sin_causa = despido_sin_causa

    def is_equal(self, comparar_con):
        """
        Compara el objeto actual con otra instancia de la clase Empleado.
        """
        assert self.identificacion == comparar_con.identificacion
        assert self.nombre == comparar_con.nombre
        assert self.cargo == comparar_con.cargo
        assert self.salario == comparar_con.salario
        assert self.fecha_ingreso == comparar_con.fecha_ingreso
        assert self.vacaciones_tomadas == comparar_con.vacaciones_tomadas
        assert self.despido_sin_causa == comparar_con.despido_sin_causa
        return True
