# 💼 Liquidación Definitiva  
### *Calculadora de Prestaciones Laborales en Python*

**Autores:**  
👩‍💻 Juanita Legarda Ramírez  
👩‍💻 Valentina Sierra Ospina  
👨‍💻 Francisco Gómez Gómez  

---

## 🧩 Prerrequisitos de Base de Datos

Antes de comenzar, asegúrate de tener lo siguiente configurado:

1. **Instala el paquete de conexión a PostgreSQL:**
   ```bash
   pip install psycopg2
Prepara tu base de datos PostgreSQL, con tus datos de conexión: usuario, contraseña, host y nombre de la base de datos.

Crea el archivo secret_config.py con la siguiente estructura (sin datos reales):

python
Copiar código
DB_HOST = "localhost"
DB_NAME = "nombre_de_tu_bd"
DB_USER = "tu_usuario"
DB_PASSWORD = "tu_contraseña"
⚠️ Importante: este archivo no debe contener datos reales cuando se suba al repositorio.

Ejecuta las pruebas unitarias antes de correr la aplicación por primera vez; esto creará las tablas necesarias en tu base de datos.

🛠️ Configuración de la Base de Datos
Esta aplicación requiere la existencia de una tabla llamada usuarios.

Puedes crearla con el script SQL incluido en:

bash
Copiar código
sql/crear-empleados.sql
Si necesitas reiniciar la base de datos, usa también:

bash
Copiar código
sql/borrar-empleados.sql
💡 Las pruebas unitarias también crean y eliminan las tablas automáticamente.

🧱 Arquitectura del Proyecto
El sistema sigue el patrón MVC (Model - View - Controller), asegurando una separación clara entre la lógica de negocio, la interfaz de usuario y las pruebas.

pgsql
Copiar código
📦 src/
 ├── model/
 │   └── LiquidacionLaboral.py
 ├── view/
 │   └── main.py
 ├── controller/
 │   └── empleado_controller.py
 ├── database/
 │   └── connection.py
 └── test/
     └── test_liquidacion.py
<p align="center"> <img src="https://github.com/user-attachments/assets/d8036110-b13e-41cf-9cec-2fb6c1ab4145" width="600" alt="Estructura del proyecto"> </p>
📘 Descripción de Componentes
src/model/LiquidacionLaboral.py
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

Lanza la excepción InteresesNoPagosError en casos simulados para validar manejo de errores.

src/view/main.py
Permite al usuario interactuar desde la terminal. Solicita datos, valida formatos y muestra resultados en pesos colombianos (COP).

Datos solicitados:

Fechas (AAAA-MM-DD)

Salario y auxilio (enteros)

Vacaciones tomadas (o “F” si no aplica)

Si fue despedido sin justa causa (S/N)

test/test_liquidacion.py
Incluye más de 10 casos de prueba, organizados así:

✅ Casos normales

Cálculos con vacaciones/no vacaciones

Distintos periodos y salarios

⚠️ Casos extraordinarios

Contratos prolongados

Combinaciones de datos extremos

❌ Casos de error simulados

Lanza InteresesNoPagosError para validar manejo de excepciones.

🧪 ¿Cómo ejecutar las pruebas unitarias?
Asegúrate de tener Python 3.x instalado.

Navega a la carpeta raíz del proyecto.

Ejecuta:

bash
Copiar código
python -m unittest test/test_LiquidacionLaboral.py
Esto ejecutará todos los casos de prueba y mostrará los resultados en consola.

💻 ¿Cómo ejecutar la calculadora por consola?
Abre una terminal en la raíz del proyecto.

Ejecuta:

bash
Copiar código
python src/view/main.py
Ingresa los datos solicitados:

Fecha de inicio

Fecha de finalización

Salario mensual

Auxilio de transporte

Vacaciones tomadas o F

Si fue despido sin causa (S/N)

El sistema calculará y mostrará el valor total de la liquidación.

🧮 Casos de Prueba: Clasificación
Casos Normales

Contrato sin interrupciones

Finalización por vencimiento

Casos Extraordinarios

Despido sin justa causa

Licencias no remuneradas

Indemnizaciones

Casos con Error

Cesantías mal calculadas

Vacaciones no liquidadas

Intereses no pagados









