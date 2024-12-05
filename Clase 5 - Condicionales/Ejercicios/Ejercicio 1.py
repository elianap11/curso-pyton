'''
Una tienda de videojuegos organiza su inventario. Verificar si hay stock suficiente 
de un videojuego y, si no hay, que avise que hay que reponerlo. El programa debería 
pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.
'''

stock_actual = int(input("Ingrese la cantidad actual en stock: "))

if stock_actual <= 0:
    print("No hay stock disponible. Es necesario hacer un nuevo pedido.")
elif stock_actual < 5:
    print("El stock es bajo. Sería conveniente un nuevo pedido")
else:
    print("Hay suficiente stock.")