# Eliminar
# Diccionario de productos
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Eliminamos las "Bananas" del diccionario
del productos["Bananas"]
# Mostramos el diccionario después de la eliminación
print(productos)
# Resultado: {'Manzanas': 50, 'Peras': 30}

# Eliminar y devolver valor
# Diccionario de productos
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}

# Eliminamos "Peras" y obtenemos su valor
cantidad_peras = productos.pop("Peras", 0)
# Si no existe "Peras", devuelve 0
# Mostramos el valor eliminado y el diccionario actualizado
print("Cantidad eliminada:", cantidad_peras)
# Resultado: Cantidad eliminada: 30
print(productos)
# Resultado: {'Manzanas': 50, 'Bananas': 20

# Eliminar todos los elementos con .clear()

# Diccionario de productos
productos = {
"Manzanas": 50,
"Peras": 30,
"Bananas": 20
}
# Limpiamos el diccionario
productos.clear()
# Mostramos el diccionario después de limpiarlo
print(productos)
# Resultado: {}

