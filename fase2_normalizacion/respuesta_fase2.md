La tabla proporcionada representa un registro académico donde se mezclan datos de estudiantes, asignaturas, profesores y calificaciones. Al analizarla desde el punto de vista de normalización, encontramos lo siguiente:


1. La tabla si cumple 1NF. Todos los campos tienen valores atómicos (un único dato por celda), sin listas ni campos repetidos, por lo que cumple con 1NF.
2. No cumple 2NF. Si consideramos que la clave principal está compuesta por (id_estudiante, asignatura), encontramos que hay datos que no dependen completamente de esa clave:
   -nombre_estudiante depende solo de id_estudiante.
   -profesor y departamento_profesor dependen solo de la asignatura.
   -Estas dependencias parciales no cumplen la 2NF.
3. Tampoco cumple 3NF. Existe una dependencia transitiva: el departamento_profesor depende del profesor, no directamente de la clave. Esto contradice la 3NF.


Para cumplir con las tres primeras formas normales, es necesario dividir la tabla original en varias tablas relacionadas, separando las entidades clave:

Estudiante(id_estudiante, nombre_estudiante)
Profesor(id_profesor, nombre_profesor, departamento)
Asignatura(id_asignatura, nombre_asignatura, id_profesor)
Historial_Academico(id_estudiante, id_asignatura, calificacion)

Esto reduce la redundancia, mejora la consistencia de los datos y hace más sencilla su administración a futuro.

Para una posible muestra de como resultaría, se creó un pequeño script en Python que toma el archivo original en formato .xlsx ubicado en la carpeta fase2_normalizacion/tabla.xlsx, y genera las cuatro tablas normalizadas como archivos CSV. El script se encuentra en esta misma carpeta conocido como: normalizador.py
