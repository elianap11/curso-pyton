# Función para calcular las ventas de un producto
def calcular_ventas_producto1():
    ventas = 10 # Ejemplo de ventas
    return ventas

# Función para calcular las ventas de otro producto
def calcular_ventas_producto2():
    ventas = 15 # Ejemplo de ventas
    return ventas

# Función que llama a las anteriores para calcular el total
def calcular_ventas_totales():
    total = calcular_ventas_producto1() + calcular_ventas_producto2()
    return total

# Llamamos a la función principal
ventas_totales = calcular_ventas_totales()
print("Las ventas totales son:", ventas_totales)