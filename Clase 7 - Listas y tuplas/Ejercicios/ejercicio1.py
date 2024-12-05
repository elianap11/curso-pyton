productos = []  # Lista vacía que guarda productos

codigo = input("Ingresá el código del producto o 'salir' para finalizar: ")

while codigo != "salir":
    nombre = input("Ingresá el nombre: ")
    precio = float(input("Ingresá el precio: "))
    stock = int(input("Ingresá el stock: "))

    # Agregamos los datos del producto en una lista dentro de la lista de productos
    productos.append([codigo, nombre, precio, stock])

    codigo = input("Ingresá el código del siguiente producto o 'salir' para finalizar: ")

print("Productos ingresados:")
# Verifica si la lista no está vacía
if productos:  
    for producto in productos:
        print("Código:", producto[0], "Nombre:", producto[1], "Precio:", producto[2], "Cantidad:", producto[3])
else:
    print("No ingresaste productos.")