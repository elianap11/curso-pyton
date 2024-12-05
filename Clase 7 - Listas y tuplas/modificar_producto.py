# Lista de productos: nombre, precio y cantidad
inventario = [
    ["manzanas", 100, 50],
    ["pan", 50, 20],
    ["leche", 60, 30]
]

# Pedir al usuario qué producto quiere modificar
producto_modificar = input("¿Qué producto querés modificar?: ")

# Recorrer el inventario para encontrar el producto y modificar su precio
indice = 0
encontrado = False  # Variable para verificar si el producto fue encontrado

while indice < len(inventario):
    if inventario[indice][0] == producto_modificar:
        nuevo_precio = float(input("Ingresá el nuevo precio: "))
        inventario[indice][1] = nuevo_precio
        encontrado = True  # Se marca como encontrado al modificar
        break
    indice += 1

# Si no se encontró el producto
if not encontrado:
    print("No se encontró el producto para modificar.")

# Mostrar el inventario actualizado
print("\nInventario actualizado:")
indice = 0
while indice < len(inventario):
    producto = inventario[indice]
    print("Producto:", producto[0])
    print("Precio: $", producto[1])
    print("Cantidad disponible:", producto[2])
    print("-------------------------")
    indice += 1