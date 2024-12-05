import sqlite3
# Conectarse a la base de datos y crear un cursor
conexion = sqlite3.connect("base_datos.db")
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

# Insertar un nuevo registro en la tabla Personas
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Carlos', 27, 'Tucumán')")
# Guardar los cambios
conexion.commit()
# Cerrar la conexión
conexion.close()