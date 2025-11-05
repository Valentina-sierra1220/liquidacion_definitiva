from flask import Flask, render_template, request
from datetime import datetime
from src.controller.empleado_controller import EmpleadoController
from src.controller.liquidacion_controller import calcular_liquidacion_de_empleado
from src.model.empleado_model import Empleado

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/empleado/nuevo')
def nuevo_empleado():
    return render_template('crear_empleado.html')

@app.route('/empleado/guardar', methods=['POST'])
def guardar_empleado():
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
        return f"Error al guardar empleado: {str(e)}"


@app.route('/empleado/buscar')
def buscar_empleado():
    return render_template('buscar_empleado.html')

@app.route('/empleado/resultado', methods=['POST'])
def resultado_busqueda():
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


@app.route('/liquidacion/form')
def formulario_liquidacion():
    return render_template('formularios.html')

@app.route('/liquidacion/calcular', methods=['POST'])
def calcular_liquidacion():
    try:
        identificacion = request.form.get('nombre', '')
        fecha_fin = datetime.strptime(request.form['fecha_retiro'], '%Y-%m-%d').date()
        resultado = calcular_liquidacion_de_empleado(identificacion, fecha_fin)
        return render_template('resultado_liquidacion.html', r=resultado)
    except Exception as e:
        return f" Error al calcular la liquidación: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
