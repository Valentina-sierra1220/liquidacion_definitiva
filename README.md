
# Realizado por Juanita Legarda Ramírez, Valentina Sierra Ospina y Francisco Gomez Gomez

#  `PREREQUISITOS BASE DE DATOS`

Instale el paquete psycopg2 con:

pip install psycopg2

Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso.

Copie el archivo secret_config.py y establezca en este archivo los datos de conexión a su base de datos.

Antes de ejecutar la aplicación por primera vez, debe ejecutar las pruebas unitarias, para que vean las tablas en la base de datos.

#  `Configuración de la base de datos`
Esta aplicación requiere que este creado una tabla de llamada de usuarios.

Utilice el script en SQL\crear-empleados.sql para crear antes de ejecutar la aplicación o las pruebas unitarias para que se creen las tablas necesarias.

#  `USO DE LA APLICACIÓN `

💼 Liquidación Definitiva - Calculadora de Prestaciones Laborales en Python

Este proyecto implementa una calculadora de liquidación laboral para trabajadores en Colombia, desarrollada en Python. Permite calcular el valor total a pagar a un empleado al finalizar su contrato, incluyendo conceptos como:

- Cesantías
- Intereses sobre cesantías
- Prima de servicios
- Vacaciones no disfrutadas

Además, el sistema maneja errores específicos mediante excepciones personalizadas y cuenta con una completa suite de pruebas unitarias.


🏗️ Arquitectura del Proyecto

El proyecto está estructurado de forma modular, siguiendo una aproximación tipo **MVC (Model - View - test)** para mantener una separación clara entre la lógica del negocio, la interfaz de usuario y las pruebas.

#  `ESTRUCTURA ` 


<img width="674" height="326" alt="Capture" src="https://github.com/user-attachments/assets/d8036110-b13e-41cf-9cec-2fb6c1ab4145" />



# 🔍 Descripción de Componentes

 # 📦 `src/model/LiquidacionLaboral.py`
Contiene la función principal `calcular_total()`, la cual recibe como parámetros:

- `fecha_inicio`: fecha de ingreso del trabajador
- `fecha_fin`: fecha de salida
- `salario`: salario mensual
- `auxilio`: auxilio de transporte mensual
- `vacaciones_tomadas`: número de días de vacaciones disfrutadas
- `despido_sin_causa`: booleano que indica si fue despedido sin justa causa

Calcula los siguientes componentes:

- **Cesantías:** proporcionales al tiempo trabajado
- **Intereses sobre cesantías:** 12% anual
- **Prima de servicios:** proporcional al tiempo trabajado
- **Vacaciones no tomadas:** máximo 15 días por año

Además, lanza la excepción personalizada `InteresesNoPagosError` en ciertos casos simulados para validar el manejo de errores en las pruebas.


#  `src/view/main.py`

Este archivo permite al usuario interactuar con el sistema desde la terminal. Solicita los datos necesarios, valida el formato y muestra el resultado en pesos colombianos (`COP`).

Inputs solicitados:
- Fechas en formato `AAAA-MM-DD`
- Salario y auxilio como números enteros
- Vacaciones tomadas (o `F` si no aplican)
- Si fue despedido sin justa causa (`S/N`)
  

#  `test/test_liquidacion.py`

El archivo contiene más de 10 casos de prueba que validan:

#### ✅ Casos normales:
- Cálculos con vacaciones tomadas y no tomadas
- Periodos variados de tiempo
- Diferentes niveles salariales

#### ⚠️ Casos extraordinarios:
- Contratos de duración prolongada (más de un año)
- Combinaciones extremas de entrada

#### ❌ Casos con errores simulados:
Pruebas diseñadas para lanzar la excepción `InteresesNoPagosError`
Por ejemplo:
(date(2025, 1, 5), date(2025, 6, 15), 1_200_000, 162_000)


#  `¿Cómo ejecutar las pruebas unitarias?`

-Asegúrate de tener Python 3.x instalado.

-Navega a la carpeta del proyecto.

-Ejecuta las pruebas con el siguiente comando: python -m unittest test/test_LiquidacionLaboral.py

Esto correrá todos los casos de prueba y mostrará si los resultados esperados coinciden con los obtenidos.

#  `¿Cómo ejecutar la calculadora de liquidación por consola?`

-Abre una terminal en la carpeta raíz del proyecto.

- Ejecuta el siguiente comando: python src/view/main.py

-El sistema te pedirá los siguientes datos: Fecha de inicio laboral (formato AAAA-MM-DD), Fecha de finalización, Salario mensual, Auxilio de transporte, Vacaciones tomadas (o F si no aplican), Si fue despedido sin justa causa (S/N)
El sistema calculará y mostrará el valor total de la liquidación.

# Casos de Prueba para Liquidación Definitiva Laboral

La **liquidación definitiva laboral** es el cálculo y pago de las prestaciones sociales que un empleador debe entregar a un trabajador al finalizar un contrato. Este proceso incluye conceptos como:

* Cesantías
* Intereses sobre cesantías
* Prima de servicios
* Vacaciones
* Otros valores pendientes según la legislación laboral vigente

## Objetivo del Repositorio

Este repositorio proporciona una colección de **casos de prueba** diseñados para validar el correcto cálculo de la liquidación definitiva en diferentes escenarios laborales. Está orientado a desarrolladores, testers, abogados laborales y académicos que deseen verificar o implementar este tipo de cálculo en sistemas informáticos.

## Clasificación de Casos de Prueba

Los casos están organizados en tres categorías principales:

1. **Casos Normales**
   Representan situaciones estándar sin novedades contractuales. Ejemplos:

   * Contrato a término fijo sin interrupciones
   * Finalización por vencimiento de contrato

2. **Casos Extraordinarios**
   Involucran condiciones atípicas que afectan la liquidación, tales como:

   * Despido sin justa causa
   * Licencias no remuneradas
   * Recargos nocturnos o dominicales
   * Indemnizaciones

3. **Casos con Error**
   Simulan omisiones o errores comunes cometidos por el empleador, útiles para pruebas negativas o de validación. Ejemplos:

   * Cesantías mal calculadas
   * Ausencia de pago de intereses
   * Vacaciones no liquidadas

## Usos

Estos casos de prueba pueden ser utilizados en:

* **Pruebas funcionales** de software de nómina
* **Desarrollo de aplicaciones** con cálculos legales incorporados
* **Capacitaciones o materiales educativos** sobre legislación laboral
* **Auditorías o verificaciones de cumplimiento normativo**



