# Recorre valores y claves
# Diccionario de productos con cantidad en stock
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Usamos un bucle for para recorrer claves y valores
for producto, cantidad in productos.items():
    print("Producto:", producto, "Cantidad en stock:", cantidad)
    
# Recorre sólo las claves
# Diccionario de productos con cantidad en stock
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Usamos un bucle for para recorrer solo las claves
for producto in productos.keys():
    print("Producto disponible:", producto)
    
# Recorre solo valores

# Diccionario de productos con cantidad en stock
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Usamos un bucle for para recorrer solo los valores
total = 0
for cantidad in productos.values():
    total = total + cantidad
    print("Cantidad total de productos en stock:", total)
    
# Usamos todos
    
# Diccionario de productos con cantidad en stock
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Recorremos el diccionario para mostrar los productos
print("Inventario de productos:")
for producto, cantidad in productos.items():
    print("Producto:", producto, "- Cantidad en stock:", cantidad)
# Calculamos el total de productos en stock
    total_productos = sum(productos.values())
print("Total de productos en stock:", total_productos)

# Supongamos que querés registrar las ventas del día y luego actualizar el inventario 
# principa al final del día. Usamos dos diccionarios: uno para el inventario y otro para 
# las ventas diarias.
# Inventario inicial
inventario = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 40
}
# Diccionario para registrar ventas del día
ventas_dia = {}
# Pedimos al usuario que ingrese el producto y la cantidad vendida
# Supongamos que vendemos 3 productos diferentes en el día
for _ in range(3):
    producto = input("Ingresá el producto vendido: ")
    cantidad_vendida = int(input("Ingresá la cantidad vendida: "))
# Si el producto está en el inventario, registramos la venta
if producto in inventario:
# Actualizamos el diccionario de ventas
    ventas_dia[producto] = cantidad_vendida
else:
    print("Producto no encontrado en inventario.")
# Actualizamos el inventario con las ventas del día
for producto, cantidad in ventas_dia.items():
    inventario[producto] = inventario[producto] - cantidad
print("Inventario actualizado:", inventario)