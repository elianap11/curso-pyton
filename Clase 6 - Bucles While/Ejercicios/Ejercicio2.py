'''
Escribí un programa que permita al usuario ingresar el precio de un producto, 
pero que sólo acepte valores mayores a 0. Si el usuario ingresa un valor inválido 
(negativo o cero), el programa debe mostrar un mensaje de error, y volver a pedir 
el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el 
precio aceptado.

Tips: 
Antes de empezar, pensá si es necesario usar contadores o acumuladores.
Recordá que input() siempre devuelve cadenas de caracteres.
'''

#Ejemplo 1
# Inicializo con un valor no válido
precio = 0  

while precio <= 0:  
    precio = float(input("Ingresá el precio del producto (debe ser mayor a 0): "))
    
    if precio > 0: 
        print(f"El precio aceptado es: {precio}.")
    else:
        print("Error: El precio debe ser un número mayor a 0. Intente nuevamente.")
        
        
#Ejemplo 2

precio = float(input("Ingresá el precio del producto (debe ser mayor a 0): "))

while precio <= 0:
    print("Error: El precio debe ser un número mayor a 0. Intente nuevamente.")
    precio = float(input("Por favor, ingresá el precio del producto (debe ser mayor a 0): "))
print(f"El precio aceptado es: {precio}.")