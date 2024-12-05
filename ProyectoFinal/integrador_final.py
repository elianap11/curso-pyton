'''
MI DUDA ES SI HAY QUE BUSCARLO Y ELIMINARLO POR ID O POR NOMBRE
'''

import sqlite3

# Función para establecer conexión a la base de datos y crear la tabla
def init_db():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para registrar un nuevo producto en la base de datos
def registrar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio: "))
    categoria = input("Ingrese la categoría: ")
    
    cursor.execute("INSERT INTO Productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    
    conexion.commit()
    print("Producto registrado con éxito.")
    conexion.close()

# Función para mostrar todos los productos en el inventario
def mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()

    if resultados:
        print("Listado de productos en el inventario:")
        for registro in resultados:
            print(f"ID: {registro[0]}, Nombre: {registro[1]}, Descripción: {registro[2]}, "
                  f"Cantidad: {registro[3]}, Precio: {registro[4]}, Categoría: {registro[5]}")
    else:
        print("No hay productos en el inventario.")
    
    conexion.close()

# Función para actualizar la cantidad de un producto
def actualizar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    
    cursor.execute("UPDATE Productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
    if cursor.rowcount > 0:
        print("La cantidad del producto ha sido actualizada con éxito.")
    else:
        print("No se encontró un producto con ese ID.")
    
    conexion.commit()
    conexion.close()

# Función para eliminar un producto del inventario
def eliminar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
    
    cursor.execute("DELETE FROM Productos WHERE id = ?", (id_producto,))
    if cursor.rowcount > 0:
        print("El producto ha sido eliminado con éxito.")
    else:
        print("No se encontró un producto con ese ID.")
    
    conexion.commit()
    conexion.close()

# Función para reportar productos con bajo stock
def reporte_bajo_stock():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    limite_stock = int(input("Ingrese el límite de bajo stock: "))
    cursor.execute("SELECT * FROM Productos WHERE cantidad < ?", (limite_stock,))
    resultados = cursor.fetchall()

    if resultados:
        print("Productos con bajo stock:")
        for registro in resultados:
            print(f"ID: {registro[0]}, Nombre: {registro[1]}, Cantidad: {registro[3]}")
    else:
        print("No hay productos con bajo stock.")
    
    conexion.close()

# Función para mostrar el menú principal
def mostrar_menu():
    init_db()  # Inicializa la base de datos y crea la tabla si es necesario

    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar cantidad de un producto")
        print("4. Eliminar producto")
        print("5. Reporte de bajo stock")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Iniciar el programa llamando al menú principal
mostrar_menu()