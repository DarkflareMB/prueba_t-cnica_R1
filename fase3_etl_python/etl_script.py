import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Python_test"
)
cursor = conn.cursor()

excel_path = "fase3_etl_python/datos_fuente.xlsx"

df_productos = pd.read_excel(excel_path, sheet_name="productos")
df_ventas = pd.read_excel(excel_path, sheet_name="ventas")

df_productos = df_productos.dropna()
df_ventas = df_ventas.dropna()

cursor.execute("DELETE FROM ventas")
cursor.execute("DELETE FROM productos")
conn.commit()

for _, row in df_productos.iterrows():
    cursor.execute("""
        INSERT INTO productos (id_producto, nombre_producto, categoria)
        VALUES (%s, %s, %s)
    """, (int(row["id_producto"]), row["nombre_producto"], row["categoria"]))

for _, row in df_ventas.iterrows():
    cursor.execute("""
        INSERT INTO ventas (id_producto, continente, pais, cliente, unidades, importe, año)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["id_producto"]),
        row["continente"],
        row["pais"],
        row["cliente"],
        int(row["unidades"]),
        float(row["importe"]),
        int(row["año"])
    ))

conn.commit()
cursor.close()
conn.close()

print("Proceso ETL finalizado correctamente.")
