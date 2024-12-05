'''
Supongamos que deseás simular los precios de 10 productos en un inventario. Escribí un
programa que:
● Utilice el módulo random para generar 10 precios aleatorios entre $10.00 y $100.00.
● Redondee los precios generados a dos decimales usando una función del módulo
math
'''

import random
import math

def generar_precios(cantidad, rango_inferior, rango_superior):
    precios = []

    for _ in range(cantidad):
        # Generar un precio aleatorio
        precio = random.uniform(rango_inferior, rango_superior)  # Genera un float
        # Redondear el precio a dos decimales
        precio_redondeado = math.floor(precio * 100) / 100  # Redondeo hacia abajo
        precios.append(precio_redondeado)

    return precios

# Definir parámetros
cantidad_productos = 10
rango_inferior = 10.00
rango_superior = 100.00

# Generar precios
precios_generados = generar_precios(cantidad_productos, rango_inferior, rango_superior)

# Mostrar precios generados
print("Precios generados para productos:")
for precio in precios_generados:
    print(f"${precio:.2f}")
    
#Hecho en clase
'''
import random
import math

def generar_precio():
    #Generamos un precio aleatorio con decimales
    precio = random.uniform(10.00, 100.00)

    #Redondear a dos decimales
    redondeo = math.floor(precio * 100) / 100
    return redondeo

#Generar y mostrar los precios de 10 productos
 
precios = []
for i in range(10):
    precio = generar_precio()
    precios.append(precio)
    print("Precio del producto", i + 1, ":", precio)
'''