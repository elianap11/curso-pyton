'''
Creá un programa que solicite el ingreso de dos números enteros. Realizá las siguientes 
operaciones: suma, resta, multiplicación y módulo. Luego, mostrá el resultado de cada 
operación en un formato claro. Asegurate de incluir mensajes personalizados que expliquen 
cada resultado, por ejemplo: "La suma de tus números es: X
'''

numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
modulo = numero1 % numero2
print("La suma de tus números es:", suma)
print("La resta de tus números es:", resta)
print("La multiplicación de tus números es:", multiplicacion)
print("El módulo (resto de la división) de tus números es:", modulo)

#El entero más cercano
division = 7 // 3
print(division)

#Exponente
resultado = 5 ** 3
print(resultado)