'''
Tu programa debe permitir al usuario consultar el inventario de una tienda 
para verificar si un producto está en stock. Si el producto está en la lista, 
el programa debe informarlo, si no, debe mostrar un mensaje indicando que 
no está disponible.

Tips: 
Usá una lista para almacenar los productos en stock.
Permití que el usuario ingrese el nombre de un producto a consultar.
Recorré la lista con un bucle while para verificar si el producto está en stock
'''
productos = ["pan", "leche", "carne"]

consulta = input("¿Qué producto querés consultar?: ").upper()

# Usamos un índice y un bucle while para recorrer la lista
index = 0
encontrado = False

while index < len(productos):
    if productos[index] == consulta:
        print(f"{consulta} está en la lista")
        encontrado = True
        break  # Salimos del bucle si encontramos el producto
    index += 1

if not encontrado:
    print(f"{consulta} no está en la lista")