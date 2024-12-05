'''
Registro de productos con validaciones
Escribí una función que permita registrar un nuevo producto en el inventario, pero con una
condición: la cantidad de productos debe ser mayor que 0 y el precio también debe ser un
valor positivo. Si se ingresa una cantidad o precio no válido, debe mostrarse un mensaje de
error y pedir los datos nuevamente hasta que sean correctos.
'''

# def registrar_producto():
#     while True:
#         # Solicitar datos del producto
#         nombre = input("Ingrese el nombre del producto: ")
        
#         # Validar la cantidad
#         while True:
#             try:
#                 cantidad = int(input("Ingrese la cantidad del producto (debe ser mayor que 0): "))
#                 if cantidad > 0:
#                     break
#                 else:
#                     print("Error: La cantidad debe ser mayor que 0. Inténtalo de nuevo.")
#             except ValueError:
#                 print("Error: La cantidad debe ser un número entero. Inténtalo de nuevo.")

#         # Validar el precio
#         while True:
#             try:
#                 precio = float(input("Ingrese el precio del producto (debe ser un valor positivo): "))
#                 if precio > 0:
#                     break
#                 else:
#                     print("Error: El precio debe ser un valor positivo. Inténtalo de nuevo.")
#             except ValueError:
#                 print("Error: El precio debe ser un número. Inténtalo de nuevo.")

#         print(f"Producto registrado: {nombre}, Cantidad: {cantidad}, Precio: ${precio:.2f}")
#         break  # Salir del bucle después de registrar correctamente el producto

# # Llamar a la función para registrar un producto
# registrar_producto()

#Ejercicio hecho en clase

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
