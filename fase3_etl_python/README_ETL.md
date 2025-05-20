# Fase 3 – Proceso ETL con Python + MySQL

## Estructura de archivos

Ubicada en la carpeta `fase3_etl_python/`:

- `etl_script.py`: Script Python que ejecuta el proceso ETL completo.
- `datos_fuente.xlsx`: Archivo Excel que contiene los registros fuente en dos hojas diferentes.
- `estructura_bd.sql`: Script SQL que crea la base de datos y las tablas necesarias.
- `README_ETL.md`: Este archivo con instrucciones detalladas.

---

## Requisitos previos

1. Tener instalado **MySQL Server** local (puerto 3306).
2. Usuario `root` (o configurar tu usuario en el script).
3. Python 3.x y las siguientes librerías:
   - `pandas`
   - `openpyxl`
   - `mysql-connector-python`

---

## Paso a paso para ejecutar la prueba

### 1. Crear la base de datos y tablas

Se puede hacer desde MySQL Workbench o línea de comandos o abriendo el archivo estructura_bd.sql desde workbench y ejecutarlo.

Esto creará:
Base de datos: Python_test
Tablas: productos, ventas

### 2. Activar entorno virtual (opcional)
python -m venv venv
.\venv\Scripts\activate

### 3 Instalar dependencias
pip install -r requirements.txt

### 4 Ejecutar la ETL
python etl_script.py

Esto realizará:
Conexión a la base de datos Python_test
Eliminación total de los datos existentes en las tablas
Lectura del archivo datos_fuente.xlsx
Inserción de todos los registros

### 5 Verificación

USE Python_test;
SELECT * FROM productos;
SELECT * FROM ventas;
