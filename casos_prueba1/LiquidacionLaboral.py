from datetime import date

def calcular_total(fecha_inicio, fecha_fin, salario, auxilio, vacaciones_tomadas, despido_sin_causa):
    dias_trabajados = (fecha_fin - fecha_inicio).days + 1
    base = salario + auxilio

    cesantias = round((base * dias_trabajados) / 360)
    intereses = round((cesantias * dias_trabajados * 0.12) / 360)
    prima = round((base * dias_trabajados) / 360)

    vacaciones_pendientes = max((15 * dias_trabajados / 360) - vacaciones_tomadas, 0)
    vacaciones_pagadas = round((salario * vacaciones_pendientes) / 720)

    total = cesantias + intereses + prima + vacaciones_pagadas

    # Debugging output
    print("Días trabajados:", dias_trabajados)
    print("Base:", base)
    print("Cesantías:", cesantias)
    print("Intereses:", intereses)
    print("Prima:", prima)
    print("Vacaciones pagadas:", vacaciones_pagadas)
    print("Total:", total)

    return total
