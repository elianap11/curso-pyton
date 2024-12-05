'''
Cálculo de promedio de ventas
Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:
1. Creá una función que reciba como parámetro una lista de ventas diarias y devuelva
el promedio de esas ventas.
2. Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días). 
Usá la función para calcular y mostrar el promedio de ventas al finalizar
'''

def calcular_promedio_ventas(ventas_diarias):
    """
    Calcula el promedio de ventas diarias.
    
    Parámetros:
    ventas_diarias (list): Lista de ventas diarias.
    
    Retorna:
    float: El promedio de las ventas.
    """
    if len(ventas_diarias) == 0:
        return 0
    return sum(ventas_diarias) / len(ventas_diarias)

# Inicializar una lista para almacenar las ventas diarias
ventas = []

# Solicitar las ventas diarias durante una semana (7 días)
for i in range(7):
    venta = float(input(f"Ingrese la venta del día {i + 1}: "))
    ventas.append(venta)

# Calcular y mostrar el promedio de ventas
promedio = calcular_promedio_ventas(ventas)
print(f"El promedio de ventas durante la semana es: {promedio:.2f}")

#Otra forma
#Función para calcular el promedio de una lista de ventas
def calcular_promedio(ventas):
    total_ventas = sum(ventas) #sumar todas las ventas
    promedio = total_ventas / len(ventas) #Dividir por la cantidad de ventas
    return promedio
#Lista para almacena las ventas diarias

ventas_diarias = []

#Pedir al usuario las ventas de cada día durante 7 días
for dia in range(1, 8):
    venta = float(input("Ingresá la venta del día " + str(dia) + ":"))
    ventas_diarias.append(venta)

#Calcular el promedio de las ventas usando la función
promedio_ventas = calcular_promedio(ventas_diarias)

#Mostrar el promedio al usuario
print(f"El promedio de ventas es: {promedio_ventas:.2f}")