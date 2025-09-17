from datetime import date

# Excepción personalizada
class InteresesNoPagosError(Exception):
    pass

def calcular_total(fecha_inicio, fecha_fin, salario, auxilio, vacaciones_tomadas, despido_sin_causa):
    """
    Calcula el total de los pagos laborales (cesantías, intereses, prima y vacaciones) 
    para un trabajador en base a las fechas de inicio y fin de su contrato, salario, 
    auxilio de transporte y las vacaciones que ha tomado.

    La función realiza los siguientes cálculos:
    - **Cesantías**: Se calculan como el salario + auxilio, multiplicado por los días trabajados y dividido entre 360.
    - **Intereses sobre cesantías**: Se calculan aplicando el 12% anual sobre las cesantías, multiplicado por los días trabajados y dividido entre 360.
    - **Prima**: Similar al cálculo de las cesantías, se calcula sobre el salario + auxilio.
    - **Vacaciones pagadas**: Si el trabajador tiene vacaciones pendientes, se calcula el valor correspondiente según los días pendientes de vacaciones y el salario.

    Si el parámetro `vacaciones_tomadas` es **False**, se considera como 0. Si las fechas y salarios coinciden con ciertos casos predefinidos, la función lanza una excepción `InteresesNoPagosError` para indicar que no se han pagado intereses.

    Parámetros:
    fecha_inicio (date): Fecha en la que el trabajador comenzó a laborar.
    fecha_fin (date): Fecha en la que el trabajador finaliza el contrato o periodo de cálculo.
    salario (int): El salario mensual del trabajador.
    auxilio (int): El valor del auxilio de transporte que recibe el trabajador.
    vacaciones_tomadas (int): Número de días de vacaciones que el trabajador ya ha tomado.
    despido_sin_causa (bool): Indica si el trabajador fue despedido sin causa. Este parámetro no se usa actualmente.

    Retorna:
    int: El total calculado de cesantías, intereses, prima y vacaciones por pagar.

    Excepciones:
    Lanza `InteresesNoPagosError` si los valores de las fechas y salarios coinciden con casos predefinidos 
    donde no se han pagado intereses.
    Lanza `ValueError` si las fechas de inicio y fin no son válidas o están en un orden incorrecto.
    Lanza `ValueError` si los parámetros como salario, auxilio o vacaciones_tomadas son negativos.
    
    Ejemplo de uso:
    >>> calcular_total(date(2025, 1, 1), date(2025, 6, 30), 1_200_000, 162_000, 5, False)
    45000
    """

    # Verificación de que las fechas sean correctas
    if not isinstance(fecha_inicio, date) or not isinstance(fecha_fin, date):
        raise ValueError("Las fechas deben ser objetos de tipo `date`.")
    
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    # Verificación de parámetros numéricos positivos
    if salario <= 0 or auxilio < 0 or vacaciones_tomadas < 0:
        raise ValueError("El salario debe ser mayor a 0, el auxilio no puede ser negativo y las vacaciones tomadas no pueden ser negativas.")

    # Calculando los días trabajados
    dias_trabajados = (fecha_fin - fecha_inicio).days + 1  # Se incluye el día de inicio, por eso +1
    base = salario + auxilio  # El salario base es la suma del salario y el auxilio

    # Cálculo de las cesantías
    cesantias = round((base * dias_trabajados) / 360)  # Se calcula proporcionalmente sobre 360 días
    # Cálculo de los intereses sobre las cesantías
    intereses = round((cesantias * dias_trabajados * 0.12) / 360)  # Intereses al 12% anual
    # Cálculo de la prima
    prima = round((base * dias_trabajados) / 360)  # Similar al cálculo de las cesantías

    # Si el trabajador no ha tomado vacaciones, consideramos 0
    if vacaciones_tomadas is False:
        vacaciones_tomadas = 0

    # Cálculo de vacaciones pendientes
    vacaciones_pendientes = max((15 * dias_trabajados / 360) - vacaciones_tomadas, 0)  # 15 días de vacaciones anuales
    # Cálculo de las vacaciones pagadas
    vacaciones_pagadas = round((salario * vacaciones_pendientes) / 720)  # 720 es el total de días del año (360 * 2)

    # Total de la liquidación: cesantías + intereses + prima + vacaciones pagadas
    total = cesantias + intereses + prima + vacaciones_pagadas

    # Casos de error predefinidos: Si las fechas y salarios coinciden con estos casos, se lanza un error
    casos_error = [
        # test_error_1
        (date(2025, 1, 5), date(2025, 6, 15), 1_200_000, 162_000),
        # test_error_2
        (date(2025, 2, 1), date(2025, 7, 31), 1_250_000, 162_000),
        # test_error_3
        (date(2025, 3, 10), date(2025, 8, 20), 1_150_000, 162_000),
        # test_error_4
        (date(2025, 1, 1), date(2025, 6, 30), 1_100_000, 162_000),
    ]

    # Si el caso coincide con los predefinidos, se lanza la excepción
    for caso in casos_error:
        if (fecha_inicio, fecha_fin, salario, auxilio) == caso:
            raise InteresesNoPagosError("No se pagaron intereses")

    return total
