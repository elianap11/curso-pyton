'''
Gestión de inventario con diccionarios.
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa
que permita:
1. Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en
un diccionario donde la clave es el nombre del producto y el valor es su precio.
2. Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
'''

# Inicializar un diccionario vacío para almacenar los productos y precios
inventario = {}

# Ingresar tres productos y sus precios
for i in range(3):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio de {producto}: "))
    inventario[producto] = precio

# Mostrar todos los productos y sus precios
print("\nProductos y precios en el inventario:")
for producto, precio in inventario.items():
    print(f"Producto: {producto}, Precio: $ {precio:.2f}")