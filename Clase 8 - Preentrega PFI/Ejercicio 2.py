'''
Actualización del inventario a partir de un arreglo:
En una tienda es necesario actualizar el inventario cuando se venden productos. A continuación, 
te proporcionamos un arreglo con una lista de productos, donde cada producto tiene un código, 
una descripción y una cantidad en stock. Escribí un programa que permita:
● Seleccionar un producto a partir de su código.
● Ingresar la cantidad vendida (que debe ser mayor que cero).
● Actualizar la cantidad en stock de ese producto restando la cantidad vendida.
El arreglo de productos disponibles es el siguiente:
productos = [
  ["P001", "Manzanas", 50],
  ["P002", "Peras", 40],
  ["P003", "Bananas", 30],
  ["P004", "Naranjas", 60]
  ]
  El script que tenés que hacer debe modificar la cantidad en stock de acuerdo a cada venta
  realizada. Si la cantidad vendida es mayor que la cantidad disponible en stock, el programa
  debe mostrar un mensaje de error
'''

# Arreglo de productos disponibles
productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30],
    ["P004", "Naranjas", 60]
]

while True:
    print("\nInventario de Productos:")
    for producto in productos:
        print(f"Código: {producto[0]}, Descripción: {producto[1]}, Cantidad en stock: {producto[2]}")

    # Seleccionar un producto a partir de su código
    codigo_producto = input("Ingrese el código del producto a vender (o 'salir' para terminar): ")
    
    if codigo_producto.lower() == 'salir':
        print("Saliendo del programa...")
        break

    producto_encontrado = False

    for producto in productos:
        if producto[0] == codigo_producto:
            producto_encontrado = True
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
            
            # Valido que la cantidad vendida sea mayor que cero
            if cantidad_vendida <= 0:
                print("La cantidad vendida debe ser mayor que cero.")
                break
            
            # Verifico si hay suficiente stock
            if cantidad_vendida > producto[2]:
                print(f"Error: No hay suficiente stock. Solo hay {producto[2]} disponibles.")
            else:
                # Actualizo la cantidad en stock
                producto[2] -= cantidad_vendida
                print(f"Venta realizada. Nuevas unidades en stock de {producto[1]}: {producto[2]}.")

    if not producto_encontrado:
        print("Error: Código de producto no encontrado.")