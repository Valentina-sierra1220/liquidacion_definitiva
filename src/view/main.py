import sys
sys.path.append("src")

from datetime import datetime
from model.LiquidacionLaboral import calcular_total

def pedir_fecha(mensaje):
    while True:
        entrada = input(mensaje + " (AAAA-MM-DD): ")
        try:
            return datetime.strptime(entrada, "%Y-%m-%d").date()
        except ValueError:
            print("⚠️ Formato incorrecto. Usa el formato AAAA-MM-DD.")

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje + ": ")
        try:
            return int(entrada)
        except ValueError:
            print("⚠️ Debes ingresar un número entero.")

def pedir_vacaciones():
    while True:
        entrada = input("Días de vacaciones tomadas (o 'F' si no aplican): ").lower()
        if entrada == 'F':
            return False
        try:
            return int(entrada)
        except ValueError:
            print("⚠️ Ingresa un número o 'F'.")

def pedir_si_no(mensaje):
    while True:
        entrada = input(mensaje + " (S/N): ").lower()
        if entrada == 'S':
            return True
        elif entrada == 'N':
            return False
        else:
            print("⚠️ Ingresa 'S' para SÍ o 'N' para NO.")

def main():
    print("=== Calculadora de Liquidación Laboral ===\n")

    fecha_inicio = pedir_fecha("Fecha de inicio")
    fecha_fin = pedir_fecha("Fecha de finalización")

    salario = pedir_entero("Salario mensual")
    auxilio = pedir_entero("Auxilio de transporte")

    vacaciones_tomadas = pedir_vacaciones()
    despido_sin_causa = pedir_si_no("¿Fue despedido sin justa causa?")

    print("\nCalculando...\n")
    total = calcular_total(fecha_inicio, fecha_fin, salario, auxilio, vacaciones_tomadas, despido_sin_causa)

    print(f"\n💵 Total a pagar: ${total:,.0f} COP")

if __name__ == "__main__":
    main()