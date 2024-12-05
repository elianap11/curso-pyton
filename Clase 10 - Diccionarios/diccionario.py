# Diccionario de productos con nombre y cantidad
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 40
}

# Acceder a un valor
print("Cantidad de manzanas:", productos["Manzanas"])

# Es conveniente usar el método get
# La sintaxis básica de .get() es: valor = diccionario.get(clave, valor_por_defecto
# Si "Peras" no está en el diccionario, devuelve 0
cantidad_peras = productos.get("Peras", 0)
print("Cantidad de peras:", cantidad_peras)

# Diccionario de productos
productos = {
"Manzanas": 50,
"Peras": 30
}
# Tratamos de obtener un producto que no existe
cantidad_uvas = productos.get("Uvas", 0) # Si "Uvas" no está, devuelve
0
print("Cantidad de uvas:", cantidad_uvas)

# No especificamos valor por defecto
cantidad_bananas = productos.get("Bananas")
print(cantidad_bananas) # Imprime None