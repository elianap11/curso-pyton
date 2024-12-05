'''
Desarrollá un programa que permita al usuario ingresar el nombre de varios productos 
y la cantidad en stock que hay de cada uno. El programa debe seguir pidiendo que ingrese 
productos hasta que el usuario decida salir, ingresando "salir" como nombre de producto. 
Después de que el bucle termine, el programa debe mostrar la cantidad total de productos 
ingresados.

Tips: 
Vas a necesitar un contador.
Tené presente las estructuras condicionales.
'''

productos = ""
# Contador para la cantidad total de productos
total_productos = 0 

while productos != "salir":
    productos = input("Ingresá el nombre del producto (o 'salir' para terminar): ")
    # Solo solicita la cantidad si el producto no es 'salir'
    if productos != "salir":  
        cantidad = int(input("Ingresá la cantidad que hay en stock: "))
        # Incrementa el total de productos ingresados
        total_productos = total_productos + cantidad

print(f"Has salido. El total de productos ingresados es: {total_productos}")