'''
Crea un programa en Python que inserte varios registros en la tabla Personas usando una
lista de tuplas predefinida. Cada tupla debe contener un nombre, una edad y una ciudad.
Usa un bucle para recorrer la lista e insertar cada persona en la base de datos. La lista debe
tener al menos cinco personas nuevas y al finalizar el programa deben mostrarse todos los
registros en la tabla Personas.
La lista de tuplas tiene una estructura como la siguiente:
nuevas_personas = [
("Esteban", 32, "Mar del Plata"),
("Valeria", 27, "Bahía Blanca"),
("Fernando", 41, "Rosario"),
("Carolina", 29, "La Plata"),
("Juan", 35, "Córdoba")
]
'''

import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

# Crear la tabla Personas si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL
    )
''')

# Lista de nuevas personas a insertar
nuevas_personas = [
    ("Esteban", 32, "Mar del Plata"),
    ("Valeria", 27, "Bahía Blanca"),
    ("Fernando", 41, "Rosario"),
    ("Carolina", 29, "La Plata"),
    ("Juan", 35, "Córdoba")
]

# Insertar cada persona en la tabla
for persona in nuevas_personas:
    cursor.execute('''
        INSERT INTO Personas (nombre, edad, ciudad)
        VALUES (?, ?, ?)
    ''', persona)

# Guardar (commit) los cambios
conexion.commit()

# Mostrar todos los registros en la tabla Personas
cursor.execute('SELECT * FROM Personas')
registros = cursor.fetchall()

print("Registros en la tabla Personas:")
for registro in registros:
    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Edad: {registro[2]}, Ciudad: {registro[3]}")

# Cerrar la conexión
conexion.close()