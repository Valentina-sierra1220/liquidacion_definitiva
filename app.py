# -----------------------------------------------
# Aplicación Web Flask: Liquidación Definitiva
# -----------------------------------------------

from flask import Flask, render_template, request
from datetime import datetime

# Importamos nuestros controladores y modelos
from src.controller.empleado_controller import EmpleadoController
from src.controller.liquidacion_controller import calcular_liquidacion_de_empleado
from src.model.empleado_model import Empleado

# Inicializamos Flask
app = Flask(__name__)


# ----------------------------
# RUTA PRINCIPAL (MENÚ)
# ----------------------------
@app.route('/')
def menu():
    return render_template('menu.html')


# ----------------------------
# FORMULARIO: CREAR EMPLEADO
# ----------------------------
@app.route('/empleado/nuevo')
def nuevo_empleado():
    return render_template('crear_empleado.html')


@app.route('/empleado/guardar', methods=['POST'])
def guardar_empleado():
    """Guarda un nuevo empleado en la base de datos."""
    try:
        empleado = Empleado(
            identificacion=request.form['identificacion'],
            nombre=request.form['nombre'],
            cargo=request.form['cargo'],
            salario=float(request.form['salario']),
            fecha_ingreso=request.form['fecha_ingreso'],
            vacaciones_tomadas=int(request.form['vacaciones_tomadas']),
            despido_sin_causa=request.form['despido_sin_causa'].lower() == 'true'
        )
        EmpleadoController.insertar(empleado)
        mensaje = f"Empleado {empleado.nombre} registrado correctamente."
        return render_template('menu.html', mensaje=mensaje)
    except Exception as e:
        return f" Error al guardar empleado: {str(e)}"


# ----------------------------
# FORMULARIO: BUSCAR EMPLEADO
# ----------------------------
@app.route('/empleado/buscar')
def buscar_empleado():
    return render_template('buscar_empleado.html')


@app.route('/empleado/resultado', methods=['POST'])
def resultado_busqueda():
    """Busca un empleado por cédula y muestra la información."""
    cedula = request.form['identificacion']
    empleado = EmpleadoController.buscar_por_cedula(cedula)
    if not empleado:
        return render_template('menu.html', mensaje=f"No se encontró empleado con cédula {cedula}")
    
    return f"""
        <h3>Empleado encontrado:</h3>
        <p><b>Nombre:</b> {empleado.nombre}</p>
        <p><b>Cargo:</b> {empleado.cargo}</p>
        <p><b>Salario:</b> {empleado.salario}</p>
        <p><b>Fecha ingreso:</b> {empleado.fecha_ingreso}</p>
        <a href="/">Volver al menú</a>
    """


# ----------------------------
# FORMULARIO: CALCULAR LIQUIDACIÓN
# ----------------------------
@app.route('/liquidacion/form')
def formulario_liquidacion():
    """Muestra el formulario de liquidación (tu antiguo formularios.py adaptado)."""
    return render_template('formularios.html')


@app.route('/liquidacion/calcular', methods=['POST'])
def calcular_liquidacion():
    """Procesa los datos del formulario y calcula la liquidación."""
    try:
        # Capturamos datos del formulario
        identificacion = request.form.get('nombre', '')
        fecha_fin = datetime.strptime(request.form['fecha_retiro'], '%Y-%m-%d').date()

        # Llamamos a la función de cálculo
        resultado = calcular_liquidacion_de_empleado(identificacion, fecha_fin)

        # Mostramos los resultados en plantilla HTML
        return render_template('resultado_liquidacion.html', r=resultado)

    except Exception as e:
        return f" Error al calcular la liquidación: {str(e)}"


# ----------------------------
# MAIN
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
