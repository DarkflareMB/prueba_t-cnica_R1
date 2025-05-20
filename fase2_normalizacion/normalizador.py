import pandas as pd
import os

# Cargar archivo original
archivo = "fase2_normalizacion/tabla.xlsx"
df = pd.read_excel(archivo)

os.makedirs("fase2_normalizacion/output", exist_ok=True)

# Normalizar estudiantes
estudiantes = df[['id_estudiante', 'nombre_estudiante']].drop_duplicates()
estudiantes.to_csv("fase2_normalizacion/output/estudiantes.csv", index=False)

# Normalizar profesores
profesores = df[['profesor', 'departamento_profesor']].drop_duplicates().reset_index(drop=True)
profesores['id_profesor'] = profesores.index + 1
profesores = profesores[['id_profesor', 'profesor', 'departamento_profesor']]
profesores.to_csv("fase2_normalizacion/output/profesores.csv", index=False)

# Relacionar asignaturas con profesor
asignaturas = df[['asignatura', 'profesor']].drop_duplicates()
asignaturas = asignaturas.merge(profesores[['id_profesor', 'profesor']], on='profesor')
asignaturas['id_asignatura'] = range(1, len(asignaturas) + 1)
asignaturas = asignaturas[['id_asignatura', 'asignatura', 'id_profesor']]
asignaturas.to_csv("fase2_normalizacion/output/asignaturas.csv", index=False)

# Crear historial académico (relación estudiante - asignatura - calificación)
historial = df.merge(asignaturas[['asignatura', 'id_asignatura']], on='asignatura')
historial = historial[['id_estudiante', 'id_asignatura', 'calificacion']]
historial.to_csv("fase2_normalizacion/output/historial_academico.csv", index=False)

print("Tablas normalizadas exportadas exitosamente en 'fase2_normalizacion/output'.")
