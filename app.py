
# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return render_template("obtener_datos.html")


@app.route('/calcular')      
def calcular():
    nombre = request.args["nombre"]
    apellido = request.args["apellido"]
    fecha_ingreso = request.args["fecha_ingreso"]
    fecha_retiro = request.args["fecha_retiro"]
    salario = request.args["salario"]
    dias_vacaciones = request.args["dias_vacaciones"]

    result = TestEmpleadoController.calc_payment(nombre, apellido ,fecha_ingreso ,fecha_retiro ,salario ,dias_vacaciones)
    return f"Aqui se calcula la liquidacion ddefinitiva. Los datos recibidos fueron {nombre}, {apellido}, {fecha_ingreso}, {fecha_retiro}, {salario}, {dias_vacaciones}. La liquidacion definitiva fue de {result}"
    



# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True)