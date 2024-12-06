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
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return
        
        descripcion = input("Ingrese la descripción del producto: ").strip()
        
        cantidad = input("Ingrese la cantidad disponible: ")
        if not cantidad.isdigit() or int(cantidad) < 0:
            print("Error: La cantidad debe ser un número entero positivo.")
            return
        cantidad = int(cantidad)
        
        precio = input("Ingrese el precio: ")
        try:
            precio = float(precio)
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                return
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return
        
        categoria = input("Ingrese la categoría: ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            return

        cursor.execute("INSERT INTO Productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto registrado con éxito.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
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
    
def buscar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    try:
        id_producto = int(input("Ingrese el ID del producto que desea buscar: "))
        cursor.execute("SELECT * FROM Productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        if producto:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
        else:
            print("No se encontró un producto con ese ID.")
    except ValueError:
        print("Error: El ID ingresado debe ser un número.")
    finally:
        conexion.close()


# Función para actualizar la cantidad de un producto
def actualizar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    try:
        id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        
        cursor.execute("UPDATE Productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
        if cursor.rowcount > 0:
            print("La cantidad del producto ha sido actualizada con éxito.")
        else:
            print("No se encontró un producto con ese ID.")
        conexion.commit()
    except ValueError:
        print("Error: Los valores ingresados deben ser números válidos.")
    finally:
        conexion.close()


# Función para eliminar un producto del inventario
def eliminar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    try:
        id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
        cursor.execute("DELETE FROM Productos WHERE id = ?", (id_producto,))
        if cursor.rowcount > 0:
            print("El producto ha sido eliminado con éxito.")
        else:
            print("No se encontró un producto con ese ID.")
        conexion.commit()
    except ValueError:
        print("Error: El ID ingresado debe ser un número válido.")
    finally:
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
        print("6. Buscar producto por ID")
        print("7. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrar_producto()
            elif opcion == 2:
                mostrar_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == 5:
                reporte_bajo_stock()
            elif opcion == 6:
                buscar_producto()
            elif opcion == 7:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione un número entre 1 y 7.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")


# Iniciar el programa llamando al menú principal
mostrar_menu()