'''
Mostrar los códigos de productos ingresados
En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un
programa que permita ingresar los códigos de 4 productos y luego indicá que se muestren
uno por uno, junto con su posición en la lista. Ejemplo: si los códigos ingresados son
"P001", "P002", "P003", "P004", el programa debe mostrar:
Producto 1: P001
Producto 2: P002
Producto 3: P003
Producto 4: P004
Tips:
● Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.
'''

# Lista vacía para almacenar los códigos de los productos
codigos = []

# Ingresar códigos de 4 productos
for i in range(4):
    codigo = input(f"Ingrese el código del producto {i + 1}: ")
    codigos.append(codigo)

# Mostrar códigos con su posición
for i in range(len(codigos)):
    print(f"Producto {i + 1}: {codigos[i]}")