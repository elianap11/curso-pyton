'''
Escribe un programa en Python que genere cinco códigos únicos de cinco dígitos para
usarlos como identificadores de productos en un inventario. Para esto, utiliza el módulo
random. Cada código generado debe ser diferente de los otros.
Tip: Puedes usar random.randint() para generar números dentro de un rango determinado
'''

import random

def generar_codigos_unicos(cantidad, longitud):
    codigos = set()  # Usamos un conjunto para evitar duplicados

    while len(codigos) < cantidad:
        # Generar un código de cinco dígitos
        codigo = random.randint(10000, 99999)  # Rango de 10000 a 99999
        #codigo = random.randint(10**(longitud-1), 10**longitud-1)
        codigos.add(codigo)  # Agregar al conjunto (automáticamente evita duplicados)

    return list(codigos)  # Convertir el conjunto a lista para mostrar

# Generar 5 códigos únicos de 5 dígitos
codigos_generados = generar_codigos_unicos(5, 5)

print("Códigos únicos generados:")
for codigo in codigos_generados:
    print(codigo)