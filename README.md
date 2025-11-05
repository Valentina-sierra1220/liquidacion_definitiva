# 💼 Liquidación Definitiva  
### Calculadora de Prestaciones Laborales en Python + Flask + PostgreSQL  

**Autores:**  
👩‍💻 Juanita Legarda Ramírez  
👩‍💻 Valentina Sierra Ospina  
👨‍💻 Francisco Gómez Gómez  

---
### Aplicación desplegada click
https://liquidacion-definitiva.onrender.com/liquidacion/form


## 🧩 Prerrequisitos de Base de Datos  

Antes de comenzar, asegúrate de tener lo siguiente configurado:

1. **Instala los paquetes necesarios:**  
   ```bash
   pip install flask psycopg2

Prepara tu base de datos PostgreSQL, con tus datos de conexión: usuario, contraseña, host y nombre de la base de datos.

Crea el archivo secret_config.py con la siguiente estructura (sin datos reales):

PGHOST = "localhost"
PGDATABASE = "nombre_de_tu_bd"
PGUSER = "tu_usuario"
PGPASSWORD = "tu_contraseña"
PGPORT = "5432"


⚠️ Importante: este archivo no debe contener datos reales cuando se suba al repositorio.

Ejecuta las pruebas unitarias antes de correr la aplicación por primera vez; esto creará las tablas necesarias en tu base de datos.




🛠️ Configuración de la Base de Datos

Esta aplicación requiere la existencia de una tabla llamada empleados.

Puedes crearla con el script SQL incluido en:

sql/crear-empleados.sql


Si necesitas reiniciar la base de datos, usa también:

sql/borrar-empleados.sql


💡 Las pruebas unitarias también crean y eliminan las tablas automáticamente.




🧱 Arquitectura del Proyecto

El sistema sigue el patrón MVC (Model - View - Controller), asegurando una separación clara entre la lógica de negocio, la interfaz de usuario y las pruebas.




📦 LIQUIDACION_DEFINITIVA/
│
├── app.py                       # Punto de entrada principal de la aplicación Flask
│
├── src/
│   ├── model/
│   │   ├── LiquidacionLaboral.py
│   │   └── empleado_model.py
│   │
│   ├── controller/
│   │   ├── empleado_controller.py
│   │   └── liquidacion_controller.py
│   │
│   ├── database/
│   │   └── secret_config.py
│
├── templates/                   # Interfaz HTML (vistas)
│   ├── base.html
│   ├── menu.html
│   ├── crear_empleado.html
│   ├── buscar_empleado.html
│   ├── formularios.html
│   └── resultado_liquidacion.html
│
├── static/                      # Archivos estáticos (CSS)
│   └── css/
│       └── style.css
│
├── sql/
│   ├── crear-empleados.sql
│   └── borrar-empleados.sql
│
└── test/
    └── test_empleado_controller.py







📘 Descripción de Componentes
📗 src/model/LiquidacionLaboral.py

Contiene la función principal calcular_total(), que recibe:

fecha_inicio: fecha de ingreso

fecha_fin: fecha de salida

salario: salario mensual

auxilio: auxilio de transporte mensual

vacaciones_tomadas: número de días de vacaciones disfrutadas

despido_sin_causa: booleano (True o False)

Calcula:

Cesantías

Intereses sobre cesantías (12% anual)

Prima de servicios

Vacaciones no tomadas

Lanza la excepción InteresesNoPagosError en casos simulados para validar el manejo de errores.

📘 src/model/empleado_model.py

Define la clase Empleado con los siguientes atributos:

identificacion, nombre, cargo, salario, fecha_ingreso, vacaciones_tomadas, despido_sin_causa

Incluye el método is_equal() para comparar empleados y verificar su igualdad.

📘 src/controller/empleado_controller.py

Controla la interacción con la base de datos PostgreSQL.

Funciones principales:

crear_tabla() y borrar_tabla() → Ejecutan scripts SQL.

insertar(Empleado) → Inserta un nuevo registro.

buscar_por_cedula(identificacion) → Busca empleados por cédula.

📘 src/controller/liquidacion_controller.py

Se encarga de calcular la liquidación total de un empleado, tomando sus datos desde la base de datos y utilizando la función calcular_total() del modelo LiquidacionLaboral.py.

Devuelve un diccionario con los resultados:

Nombre

Cargo

Salario

Fecha de ingreso y retiro

Vacaciones tomadas

Total liquidación

📘 app.py

Archivo principal de la aplicación Flask.
Define las rutas del sistema web:

<img width="650" height="339" alt="image" src="https://github.com/user-attachments/assets/aee50d59-3e43-4cd3-993f-029c6e6d1be9" />


💻 Interfaz Web

La aplicación cuenta con una interfaz desarrollada en HTML y CSS (Jinja2), inspirada en el estilo del proyecto creditcard-web
.

🧭 Menú lateral:

🏠 Inicio

➕ Registrar Empleado

🔍 Buscar Empleado

💰 Calcular Liquidación

🧾 Formularios:

Registrar Empleado: almacena empleados en la base de datos.

Buscar Empleado: consulta información existente.

Calcular Liquidación: realiza los cálculos según la información ingresada.

🧪 ¿Cómo ejecutar las pruebas unitarias?

Asegúrate de tener Python 3.x instalado.
Navega a la carpeta raíz del proyecto y ejecuta:

python -m unittest test/test_empleado_controller.py


Estas pruebas:

Crean y eliminan automáticamente la tabla empleados.

Insertan registros de ejemplo.

Validan la inserción y búsqueda en la base de datos.

💻 ¿Cómo ejecutar la aplicación web?

Abre una terminal en la raíz del proyecto y ejecuta:

python app.py


Luego, abre el navegador en:
👉 http://127.0.0.1:5000

🧮 Casos de Prueba: Clasificación
✅ Casos Normales

Contrato sin interrupciones

Finalización por vencimiento

Cálculos con vacaciones tomadas y sin vacaciones

⚙️ Casos Extraordinarios

Despido sin justa causa

Licencias no remuneradas

Indemnizaciones

❌ Casos con Error

Cesantías mal calculadas

Vacaciones no liquidadas

Intereses no pagados



