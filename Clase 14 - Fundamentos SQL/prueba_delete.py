import sqlite3
# Conectarse a la base de datos y crear un cursor
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()
# Eliminar el registro de José en la tabla Personas
cursor.execute("DELETE FROM Personas WHERE nombre = 'Pedro'")
# Guardar los cambios
conexion.commit()
cursor.execute("SELECT * FROM Personas")
resultados = cursor.fetchall()
for registro in resultados:
    print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])
# Cerrar la conexión
conexion.close()