'''
 Registro de ventas por día:
 Desarrollá un programa que permita registrar las ventas diarias de un comercio durante cinco días. 
 Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.
 Tips:
 ● Utilizá un bucle while que permita a la persona usuaria ingresar el monto de las ventas diarias.
 ● Asegurate de validar que el monto ingresado sea un valor positivo.
 ● Usá un acumulador para la suma de las ventas.

'''

#Ejemplo 1

print("Registro de ventas diarias")
# Lista para almacenar las ventas de cada día
ventas_diarias = [] 
# Variable para contar los días 
dia = 0   
# Acumulador para el total de ventas           
total_ventas = 0     

# Repetir hasta 5 días
while dia < 5:  

    # Input del monto de ventas
    consulta = float(input(f"Ingrese el monto de las ventas del día {dia + 1}: "))

    # Validar que el monto ingresado sea positivo
    if consulta < 0:
        print("Por favor, ingrese un valor positivo.")
        # Volver al inicio del bucle si el valor no es válido
        continue  

    # Agregar la consulta a la lista de ventas
    ventas_diarias.append(consulta)
    # Acumula las ventas
    total_ventas += consulta  
    # Incrementar el día
    dia += 1  

# Calcular el promedio de ventas
promedio_ventas = total_ventas / len(ventas_diarias) if ventas_diarias else 0

# Mostrar el total de ventas y el promedio
for i in range(len(ventas_diarias)):
    print(f"Total de ventas del día {i + 1}: {ventas_diarias[i]}")
    
print(f"El total de ventas en 5 días es: {total_ventas}")
print(f"El promedio de ventas es: {promedio_ventas}")


# Ejemplo 2


dias = 5
ventas_dias = [] #Lista para almacenar las ventas de cada día
total_ventas = 0 #acumulador para la suma total de ventas

dia = 1
while dia <= dias:
    try: 
        venta = float(input(f"Ingresá el monto de las ventas del día {dia}: "))

        #validamos que el monto sea positivo 
        if venta >= 0:
            ventas_dias.append(venta) #almacenar las ventas del dia en la lista
            total_ventas += venta #suma al acumulador
            dia += 1 #pasamos al siguiente día
        else:
            print("El monto deber ser un valor positivo. Intentá de nuevo.")
    except ValueError:
        print("error: debés ingresar un número válido.")

#Mostrar las ventas de cada día y el promedio
print("\nResumen de ventas diarias:")
for i, venta in enumerate(ventas_dias, 1):
    print(f"Día {i}: ${venta:.2f}")

#calculamos el promedio de ventas
promedio_ventas = total_ventas / dias
print(f"\nTotal de ventas: ${total_ventas:.2f}")
print(f"\nPromedio de ventas: ${promedio_ventas:.2f}")
