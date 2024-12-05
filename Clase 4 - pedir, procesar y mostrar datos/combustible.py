'''
El programa solicita que se ingrese cuántos litros de combustible gasta el auto por cada 100 km, 
el costo por litro del mismo y la distancia del viaje. Con estos datos, tu programa va a calcular
cuánto consumió el vehículo y cuánto dinero se gastó en combustible.
'''
# Entrada de datos
litros_por_100km = float(input("Ingresá la cantidad de litros que consume el coche por cada 100 km: "))
costo_por_litro = float(input("Ingresá el costo de cada litro de combustible: "))
longitud_viaje = float(input("Ingresá la longitud del viaje en kilómetros: "))

# Proceso: Calcular los litros consumidos y el dinero gastado
litros_consumidos = (litros_por_100km * longitud_viaje) / 100
dinero_gastado = litros_consumidos * costo_por_litro

# Salida: Mostrar los litros consumidos y el dinero gastado
print("Litros de combustible consumidos: ", litros_consumidos)
print("Dinero gastado en combustible: $", dinero_gastado)

