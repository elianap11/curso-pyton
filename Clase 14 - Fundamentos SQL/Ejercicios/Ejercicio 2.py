'''
Desarrolla un programa en Python que elimine todos los registros en la tabla Personas
donde la edad sea menor a 25 años. Usa un bucle para consultar y eliminar cada registro
que cumpla con esta condición. Al final del programa, muestra todos los registros restantes
para confirmar que se han eliminado correctamente los registros que cumplen la condición
'''

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

# Eliminar registros donde la edad sea menor a 25 años
cursor.execute("SELECT * FROM Personas WHERE edad < 25")
personas_a_eliminar = cursor.fetchall()  # Obtener todas las personas a eliminar

for persona in personas_a_eliminar:
    cursor.execute("DELETE FROM Personas WHERE id = ?", (persona[0],))  # Eliminar por ID

# Guardar (commit) los cambios
conexion.commit()

# Mostrar todos los registros restantes en la tabla Personas
cursor.execute('SELECT * FROM Personas')
registros_restantes = cursor.fetchall()

print("Registros restantes en la tabla Personas:")
for registro in registros_restantes:
    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Edad: {registro[2]}, Ciudad: {registro[3]}")

# Cerrar la conexión
conexion.close()