# Todas las pruebas unitarias importan la biblioteca unittest
import unittest

# Las pruebas importan los módulos que hacen el trabajo
import LiquidacionLaboral


# Debe existir por lo menos una clase que contenga las pruebas unitarias
# descendiente de unittest.TestCase
class LiquidacionLaboralTest(unittest.TestCase):

    # Cada prueba unitaria es un método de la clase
    def test_calculo_normal_1(self):
        # Datos de entrada
        salario = 1_000_000
        auxilio = 162_000
        vacaciones_tomadas = 10
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 1)
        fecha_fin = LiquidacionLaboral.date(2025, 6, 30)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  1_203_704

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)




#Caso normal 2

    def test_calculo_normal_2(self):
        # Datos de entrada
        salario = 1_200_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 5)
        fecha_fin = LiquidacionLaboral.date(2025, 6, 15)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  1_270_147

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)



#Caso normal 3

    def test_calculo_normal_3(self):
        # Datos de entrada
        salario = 1_000_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 2)
        fecha_fin = LiquidacionLaboral.date(2025, 7, 31)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  1_422_234

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)
        
        
#Caso normal 4

    def test_calculo_normal_4(self):
        # Datos de entrada
        salario = 1_050_000
        auxilio = 162_000
        vacaciones_tomadas = 7
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 2)
        fecha_fin = LiquidacionLaboral.date(2025, 6, 30)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  1_249_089

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)
        
        

#Caso extraordinario 1

    def test_calculo_extraordinario_1(self):
        # Datos de entrada
        salario = 1_500_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2024, 2, 1)
        fecha_fin = LiquidacionLaboral.date(2025, 8, 2)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  5_580_579

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)




#Caso extraordinario 2

    def test_calculo_extraordinario_2(self):
        # Datos de entrada
        salario = 1_500_000
        auxilio = 162_000
        vacaciones_tomadas = 15
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2024, 2, 1)
        fecha_fin = LiquidacionLaboral.date(2025, 8, 2)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado =  5_549_329

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)

#Caso extraordinario 3

    def test_calculo_extraordinario_3(self):
        # Datos de entrada
        salario = 1_000_000
        auxilio = 162_000
        vacaciones_tomadas =  False
        despido_sin_causa = True
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 4)
        fecha_fin = LiquidacionLaboral.date(2025, 5, 31)

        # Proceso
        resultado = LiquidacionLaboral.calcular_total(fecha_inicio, fecha_fin ,salario ,auxilio ,vacaciones_tomadas , despido_sin_causa)

        # Resultado esperado
        esperado = 987_554

        # Prueba que los resultados sean iguales
        self.assertEqual(esperado, resultado)
        
        
        
# Caso error 1

    def test_error_1_intereses_no_pagos(self):
        
        salario = 1_200_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 5)
        fecha_fin = LiquidacionLaboral.date(2025, 6, 15)

        with self.assertRaises(LiquidacionLaboral.InteresesNoPagosError):
            LiquidacionLaboral.calcular_total(fecha_inicio,fecha_fin,salario,auxilio,vacaciones_tomadas,despido_sin_causa)



# Caso error 2
    def test_error_2_intereses_no_pagos(self):
    
        salario = 1_250_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 2, 1)
        fecha_fin = LiquidacionLaboral.date(2025, 7, 31)

        with self.assertRaises(LiquidacionLaboral.InteresesNoPagosError):
            LiquidacionLaboral.calcular_total(fecha_inicio,fecha_fin,salario,auxilio,vacaciones_tomadas,despido_sin_causa)

# Caso error 3
    def test_error_3_intereses_no_pagos(self):
    
        salario = 1_150_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 3, 10)
        fecha_fin = LiquidacionLaboral.date(2025, 8, 20)

        with self.assertRaises(LiquidacionLaboral.InteresesNoPagosError):
            LiquidacionLaboral.calcular_total(fecha_inicio,fecha_fin,salario,auxilio,vacaciones_tomadas,despido_sin_causa)

#Caso error 4
    def test_error_4_intereses_no_pagos(self):
    
        salario = 1_100_000
        auxilio = 162_000
        vacaciones_tomadas = False
        despido_sin_causa = False
        fecha_inicio = LiquidacionLaboral.date(2025, 1, 1)
        fecha_fin = LiquidacionLaboral.date(2025, 6, 30)

    
        with self.assertRaises(LiquidacionLaboral.InteresesNoPagosError):
            LiquidacionLaboral.calcular_total(fecha_inicio,fecha_fin,salario,auxilio,vacaciones_tomadas,despido_sin_causa)
    
    
    
        
        
        

# Este fragmento de código permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()

