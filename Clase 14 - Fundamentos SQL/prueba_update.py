import sqlite3
# Conectarse a la base de datos y crear un cursor
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()
# Actualizar la edad de Ana en la tabla Personas
cursor.execute("UPDATE Personas SET edad = 24 WHERE nombre = 'Ana'")
# Guardar los cambios
conexion.commit()
# Cerrar la conexión
conexion.close()