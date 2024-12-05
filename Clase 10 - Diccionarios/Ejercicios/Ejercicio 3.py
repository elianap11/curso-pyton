'''
Para una empresa con N empleados, se desarrolla un algoritmo donde se ingresa 
como datos el número de orden y sueldo de cada empleado, debe imprimirse el 
numero de orden del empleado con el mayor sueldo así como su sueldo.
'''

# Solicito el número de empleados
numero_empleados = int(input("Ingrese el número de empleados: "))

# Inicializo las variables necesarias
max_sueldo = 0
numero_orden_max = None

# Ingreso los datos de cada empleado
for _ in range(numero_empleados):
    numero_orden = int(input("Ingrese el número de orden del empleado: "))
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    # Verifico si el sueldo actual es mayor que el máximo registrado
    if sueldo > max_sueldo:
        max_sueldo = sueldo
        numero_orden_max = numero_orden

# Imprimo el resultado
if numero_orden_max is not None:
    print(f"El empleado con el mayor sueldo es el número de orden: {numero_orden_max} con un sueldo de: ${max_sueldo:.2f}")
else:
    print("No se ingresaron empleados.")