# Inicialización de variables
# Creación de una lista vacía donde se agregarán los productos
productos = []
# Variable para elegir entre las opciones del menú
opcion = 0

# Bucle que continuará el ciclo mientras la variable opción no sea distinta a 7
while opcion != 7:
    print("\nGestión de Productos\n")
    print("1. Alta de productos")
    print("2. Consulta de productos")
    print("3. Modificar el stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado de productos")
    print("6. Listado de productos con stock mínimo")
    print("7. Salir")

    opcion = int(input("Seleccioná una opción (1-7): "))
    print("Has seleccionado:", opcion)

    # Alta de productos
    if opcion == 1:
        nombre = input("Ingresá el nombre del producto: ")
        cantidad = int(input("Ingresá la cantidad: "))
        precio = float(input("Ingresá el precio: "))
        stock_minimo = int(input("Ingresá el stock mínimo: "))

        # Agrego el producto a la lista (como si fuera un diccionario para un mejor diseño de impresión)
        productos.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "stock_minimo": stock_minimo
        })
        print(f"Producto '{nombre}' agregado exitosamente.")

    # Consulta de datos de productos
    elif opcion == 2:  
        nombre = input("¿Sobre qué producto querés consultar?: ").lower()
        i = 0
        encontrado = False
        while i < len(productos):
            if productos[i]["nombre"].lower() == nombre:
                print(f"{productos[i]['nombre']} - Cantidad: {productos[i]['cantidad']} - Precio: ${productos[i]['precio']} - Stock Mínimo: {productos[i]['stock_minimo']}")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print("Producto no encontrado.")

    # Modificar la cantidad en stock
    elif opcion == 3:  
        nombre = input("Ingresá el nombre del producto cuyo stock deseás modificar: ")
        i = 0
        encontrado = False
        while i < len(productos):
            if productos[i]["nombre"] == nombre:
                nueva_cantidad = int(input("Ingresá el nuevo stock: "))
                productos[i]["cantidad"] = nueva_cantidad
                print(f"Stock del producto '{nombre}' actualizado exitosamente.")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print("Producto no encontrado.")

    # Dar de baja productos
    elif opcion == 4:  
        nombre = input("Ingresá el nombre del producto a dar de baja: ")
        i = 0
        encontrado = False
        while i < len(productos):
            if productos[i]["nombre"] == nombre:
                productos.remove(productos[i])
                print(f"Producto '{nombre}' dado de baja exitosamente.")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print("Producto no encontrado.")

    # Listado completo de los productos
    elif opcion == 5:  
        if productos:
            print("Listado de productos:")
            i = 0
            while i < len(productos):
                print(f"{productos[i]['nombre']} - Cantidad: {productos[i]['cantidad']} - Precio: ${productos[i]['precio']} - Stock Mínimo: {productos[i]['stock_minimo']}")
                i += 1
        else:
            print("El inventario está vacío.")

    # Lista de productos con cantidad bajo mínimo
    elif opcion == 6:  
        print("Lista de productos con stock mínimo:")
        i = 0
        hay_productos_bajo_minimo = False
        while i < len(productos):
            if productos[i]["cantidad"] < productos[i]["stock_minimo"]:
                print(f"{productos[i]['nombre']} - Cantidad: {productos[i]['cantidad']} - Precio: ${productos[i]['precio']} - Stock Mínimo: {productos[i]['stock_minimo']}")
                hay_productos_bajo_minimo = True
            i += 1
        if not hay_productos_bajo_minimo:
            print("No hay productos por debajo del stock mínimo.")

    # Salir
    elif opcion == 7:
        print("Saliendo del programa...")
    else:
        print("Opción no válida, intentá otra vez.")