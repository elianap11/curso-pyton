'''
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
Para esto, se registran los días que trabajó y las horas de cada día. 
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además 
calcule cuánto pagó la empresa por los N empleados.
'''

# Tarifa por hora de trabajo
tarifa_hora = 20.00 

# Inicializar el total de sueldos pagados
sueldos_pagos = 0 

# Bucle para registrar múltiples empleados
while True:
    nombre_empleado = input("Ingrese el nombre del empleado (o escriba 'salir' para terminar): ")
    
    if nombre_empleado.lower() == "salir":
        break  # Salir del bucle si se ingresa 'salir'

    dias_trabajados = int(input("Cantidad de días trabajados: "))
    horas_trabajadas = int(input("Cantidad de horas trabajadas por día: "))
    
    # Calcular el sueldo semanal
    sueldo_trabajador = dias_trabajados * horas_trabajadas * tarifa_hora
    sueldos_pagos += sueldo_trabajador  # Sumar al total

    print(f"El sueldo semanal de {nombre_empleado} es: ${sueldo_trabajador:.2f}")

# Mostrar el total pagado por todos los empleados
print(f"El total pagado por la empresa a todos los empleados es: ${sueldos_pagos:.2f}")




