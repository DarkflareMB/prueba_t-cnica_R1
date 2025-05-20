# PRUEBA_TECNICA_R1 – Proceso ETL y Análisis de Datos


Este proyecto contiene la solución a una prueba técnica enfocada en el desarrollo de procesos ETL, normalización de datos, consultas SQL y visualización de datos usando Tableau. Está estructurado en 4 fases, cada una con sus archivos, scripts, documentación y resultados correspondientes.

---

##  Estructura general

PRUEBA_TECNICA_R1/
│
├── fase1_sql_teoria/ → Consultas y respuestas teóricas SQL
│ └── respuestas_fase1.md
│
├── fase2_normalizacion/ → Evaluación y normalización de una tabla académica
│ ├── normalizador.py
│ ├── tabla.xlsx
│ ├── respuesta_fase2.md
│ └── output/ → Tablas normalizadas en CSV
│
├── fase3_etl_python/ → Script ETL con conexión a MySQL
│ ├── datos_fuente.xlsx
│ ├── estructura_bd.sql
│ ├── etl_script.py
│ └── README_ETL.md → Guía paso a paso de ejecución
│
├── fase4_tableau/ → Visualización interactiva en Tableau
│ ├── Ejercicio práctico PBI o Tableau.xlsx
│ ├── prueba_tecnica_Roldan_SantiagoOrtegon.twb
│ └── README_ETL.md → Explicación del diseño de dashboard
│
├── capturas_resultados/ → Evidencias gráficas (si aplica)
├── requirements.txt → Librerías necesarias para la ETL
└── README.md → Este archivo

---

## Fase 1 – SQL Teoría
 Archivo: `fase1_sql_teoria/respuestas_fase1.md`

Contiene respuestas teóricas a preguntas sobre consultas SQL avanzadas, optimización y administración de bases de datos.

---

## 🧩 Fase 2 – Normalización

Archivo: `fase2_normalizacion/respuesta_fase2.md`  
Archivos: `normalizador.py`, `tabla.xlsx`, `output/`

Explicación y ejecución de las reglas de normalización (1NF, 2NF y 3NF) sobre una tabla académica. El script transforma y genera nuevas tablas exportadas a CSV.

Ver los resultados en la carpeta `output/`.

---

## Fase 3 – Python + MySQL (ETL)

Guía: `fase3_etl_python/README_ETL.md`  
Archivos clave:
- `estructura_bd.sql` → Crea la base de datos y tablas
- `etl_script.py` → Ejecuta el proceso ETL
- `datos_fuente.xlsx` → Archivo plano de entrada

Pasos para validar:
1. Crear la base de datos local `Python_test` en MySQL (usando `estructura_bd.sql`)
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar el script: `python etl_script.py`
4. Verificar los datos insertados.

---

## Fase 4 – Tableau

Archivos:
- `prueba_tecnica_Roldan_SantiagoOrtegon.twb` → Libro de trabajo de Tableau
- `Ejercicio práctico PBI o Tableau.xlsx` → Data fuente
- `README_ETL.md` → Detalle del diseño y funcionalidades del dashboard

Dashboard incluye:
- Mapa global de ventas y rentabilidad
- Top 10 productos por unidades
- Productos con mayor coste por región y año
- Clientes representativos y sus productos por año
- Filtros por zona, canal de venta y año

Se puede visualizar con Tableau Public o Tableau Desktop.

---

## Requisitos

- Python 3.8+
- MySQL (local)
- Tableau Public Edition (gratuito)
- Dependencias: ver `requirements.txt`

---

## Desarrollado por **Santiago Ortegón Trujillo**  
Contacto: [santiagoortegon10@gmail.com]

---
