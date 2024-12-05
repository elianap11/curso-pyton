'''
Visualización personalizada de productos
Agregá una función al sistema que permita simular la venta de un producto. El usuario o
usuaria deberá ingresar el código del producto y la cantidad a vender. Si la cantidad en
stock es suficiente, la función debe restar esa cantidad del inventario. Si la cantidad
solicitada es mayor a la disponible, debe mostrar un mensaje de error
'''
# # Inventario inicial como un diccionario
# inventario = {}

# def registrar_producto():
#     while True:
#         nombre = input("Ingrese el nombre del producto: ")
        
#         while True:
#             try:
#                 cantidad = int(input("Ingrese la cantidad del producto (debe ser mayor que 0): "))
#                 if cantidad > 0:
#                     break
#                 else:
#                     print("Error: La cantidad debe ser mayor que 0. Inténtalo de nuevo.")
#             except ValueError:
#                 print("Error: La cantidad debe ser un número entero. Inténtalo de nuevo.")

#         while True:
#             try:
#                 precio = float(input("Ingrese el precio del producto (debe ser un valor positivo): "))
#                 if precio > 0:
#                     break
#                 else:
#                     print("Error: El precio debe ser un valor positivo. Inténtalo de nuevo.")
#             except ValueError:
#                 print("Error: El precio debe ser un número. Inténtalo de nuevo.")

#         inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
#         print(f"Producto registrado: {nombre}, Cantidad: {cantidad}, Precio: ${precio:.2f}")
#         break

# def vender_producto():
#     while True:
#         codigo_producto = input("Ingrese el nombre del producto a vender: ")
        
#         if codigo_producto not in inventario:
#             print("Error: Producto no encontrado en el inventario. Inténtalo de nuevo.")
#             continue
            
#         while True:
#             try:
#                 cantidad_a_vender = int(input("Ingrese la cantidad a vender: "))
#                 if cantidad_a_vender > 0:
#                     break
#                 else:
#                     print("Error: La cantidad a vender debe ser mayor que 0. Inténtalo de nuevo.")
#             except ValueError:
#                 print("Error: La cantidad debe ser un número entero. Inténtalo de nuevo.")

#         # Comprobar si hay suficiente stock
#         if inventario[codigo_producto]['cantidad'] >= cantidad_a_vender:
#             inventario[codigo_producto]['cantidad'] -= cantidad_a_vender
#             print(f"Venta exitosa: Se vendieron {cantidad_a_vender} unidades de {codigo_producto}.")
#             print(f"Quedan {inventario[codigo_producto]['cantidad']} unidades en stock.")
#             break
#         else:
#             print("Error: No hay suficiente stock para completar la venta.")

# # Ejemplo de uso
# registrar_producto()
# vender_producto()

#Hecho en clase
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")

    #Validar la cantidad sea mayor a 0 

    while True: 
        try:
            cantidad = int(input("Ingrese la cantidad del producto ojo deber ser mayor a 0."))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0. Intentalo nuevamente.")
            else: 
                break 
        except ValueError:
            print("Error: La cantiad debe ser un número entero. Intentalo de nuevo.")
#Validar el precio 
    while True:
        try:
            precio = float(input("Ingrese el precio del producto ojo deber ser positivo."))
            if precio <=0:
                print("Error: El precio deber ser un valor positivo.")
            else:
                break
        except ValueError:
            print("Error: el precio debe ser un número válido. Intenta nuevamente.")
            
            #Registrar el producto en el inventario

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    print("Producto regustrado con éxito:", producto)
    return producto

#Llamar la función para registrar un producto

producto = registrar_producto()
 
def mostrar_productos_personalizados():
    print("1. Mostrar todos los productos")
    print("2. Mostrar productos por categoría")
    print("3. Mostrar productos con stock bajo")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_productos()
    elif opcion == 2: 
        categoria = input("Ingrese la categoría de productos a mostrar:")
        for codigo, datos in inventario.items():
            if datos['categoria'].lower() == categoria.lower():
                print("Código:", codigo)
                print("Nombre:", datos['nombre'])
                print("Descripción:", datos['descripcion'])
                print("Cantidad:", datos['cantidad'])
                print("Precio:", datos['precio'])
                print("Categoría:", datos['categoria'])
                print("-" * 30)
            elif opcion == 3:
                print("Prouctos con stock bajo:")
            for codigo,datos in inventario.items():
                if datos['cantidad'] < 5:
                    print("Código:", codigo)
                    print("Nombre:", datos['nombre'])
                    print("Descripción:", datos['descripcion'])
                    print("Cantidad:", datos['cantidad'])
                    print("Precio:", datos['precio'])
                    print("Categoría:", datos['categoria'])
                    print("-" * 30)
                else: 
                    print("Opción no válida. Intente nuevamente.")

mostrar_productos_personalizados()