'''
Suma de números naturales
Desarrolla una función que calcule la suma de los números naturales hasta un número dado
utilizando un bucle for. La suma de los números naturales hasta el número n se define como
la suma de todos los números enteros positivos desde 1 hasta n.
Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.
La función debe recibir un número entero n y devolver la suma de los números naturales
hasta n.
Tips:
● ¡Usá range()!
'''
n = 6 
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma de los números naturales hasta {n} es: {suma}")

print("\n##################################################\n")

n = int(input("Ingresa un número: ")) 

while n <= 0:
    print("El número debe ser mayor a cero")
    n = int(input("Volvé a ingresar un número: ")) 

suma = 0

for i in range(1, n + 1):
    suma += i
    
print(f"La suma de los números naturales hasta {n} es: {suma}")