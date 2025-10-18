# src/model/LiquidacionLaboral.py
from __future__ import annotations
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

class InteresesNoPagosError(Exception):
    """Excepción para simular/validar manejo de casos en que no se pagaron intereses."""
    pass

def _dias_360(inicio: date, fin: date) -> int:
    """Convención bancaria 360 días (simple y estable para proporciones)."""
    return (fin - inicio).days

def _money(x: Decimal | int | float) -> Decimal:
    return (Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def calcular_total(
    fecha_inicio: date,
    fecha_fin: date,
    salario: int | float | Decimal,
    auxilio: int | float | Decimal,
    vacaciones_tomadas: int = 0,
    despido_sin_causa: bool = False,
) -> Decimal:
    """
    Calcula un total aproximado y estable para pruebas/demostración.
    Componentes:
      - Cesantías: salario * (días/360)
      - Intereses cesantías: cesantías * 0.12 * (días/360)
      - Prima: salario * (días/360)
      - Vacaciones no tomadas: (salario/30) * max(0, 15 - vacaciones_tomadas) * (días/360)
    Nota: Fórmulas simples para propósito académico. Ajustables según requerimientos.
    """
    if fecha_fin < fecha_inicio:
        raise ValueError("fecha_fin no puede ser anterior a fecha_inicio")

    dias = Decimal(_dias_360(fecha_inicio, fecha_fin))
    prop = dias / Decimal(360)

    salario = _money(salario)
    auxilio = _money(auxilio)

    cesantias = _money(salario * prop)
    intereses = _money(cesantias * Decimal("0.12") * prop)
    prima = _money(salario * prop)

    # Vacaciones no tomadas (tope 15 días/año, proporcional)
    dias_vac_no_tomados = max(0, 15 - int(vacaciones_tomadas))
    vacaciones = _money((salario / Decimal(30)) * Decimal(dias_vac_no_tomados) * prop)

    total = cesantias + intereses + prima + vacaciones

    # Ejemplo de caso "extraordinario" para pruebas
    # (puedes remover esto si no lo necesitas)
    if despido_sin_causa and intereses == Decimal("0.00"):
        raise InteresesNoPagosError("No se pagaron intereses sobre cesantías")

    return _money(total)
