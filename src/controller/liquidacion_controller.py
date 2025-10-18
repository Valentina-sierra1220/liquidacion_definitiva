# src/controller/liquidacion_controller.py
from __future__ import annotations
from datetime import date
from decimal import Decimal

from ..model.LiquidacionLaboral import calcular_total, InteresesNoPagosError
from .empleado_controller import EmpleadoController


def calcular_liquidacion_de_empleado(identificacion: str, fecha_fin: date) -> dict:
    """
    Busca un empleado por su identificación y calcula su liquidación.
    Devuelve un diccionario con los resultados de cálculo.
    """
    empleado = EmpleadoController.buscar_por_cedula(identificacion)
    if not empleado:
        raise ValueError(f"No existe empleado con identificación {identificacion}")

    # Datos base
    salario = Decimal(empleado.salario)
    fecha_inicio = empleado.fecha_ingreso
    vacaciones_tomadas = empleado.vacaciones_tomadas or 0
    despido_sin_causa = bool(empleado.despido_sin_causa)

    # Auxilio (ajústalo si lo guardas en BD)
    auxilio = Decimal(0)

    try:
        total = calcular_total(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            salario=salario,
            auxilio=auxilio,
            vacaciones_tomadas=vacaciones_tomadas,
            despido_sin_causa=despido_sin_causa,
        )
        return {
            "empleado": empleado.nombre,
            "cargo": empleado.cargo,
            "salario": f"${salario:,.0f}",
            "fecha_inicio": str(fecha_inicio),
            "fecha_fin": str(fecha_fin),
            "vacaciones_tomadas": vacaciones_tomadas,
            "total_liquidacion": f"${total:,.2f}",
        }

    except InteresesNoPagosError as e:
        raise InteresesNoPagosError(f"Error de intereses: {e}")
    except Exception as e:
        raise RuntimeError(f"Error inesperado al calcular liquidación: {e}")

