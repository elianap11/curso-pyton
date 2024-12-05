
import sqlite3
# Conectarse a la base de datos y crear un cursor
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()

# Ejecutar la consulta SELECT y obtener todos los registros
cursor.execute("SELECT * FROM Personas")
resultados = cursor.fetchall()

cursor.execute("SELECT * FROM Personas WHERE ciudad = 'Buenos Aires'")
resultados = cursor.fetchall()

cursor.execute("SELECT nombre, edad FROM Personas")
resultados = cursor.fetchall()


# Mostrar los resultados
for registro in resultados:
    print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])
# Cerrar la conexión
conexion.close()

'''
import sqlite3
# Conectarse a la base de datos y crear un cursor
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()
# Ejecutar la consulta SELECT y obtener todos los registros
cursor.execute("SELECT * FROM Personas ORDER BY nombre DESC;")
resultados = cursor.fetchall()
# Mostrar los resultados
for registro in resultados:
print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:",
registro[2])
# Cerrar la conexión
conexion.close()
'''