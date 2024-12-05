producto = "Notebook" # Cadena original
nombre_acumulado = "" # Inicializamos el acumulador
# Recorrer cada letra de la cadena y acumularla
for letra in producto:
# Acumulamos letra por letra
  nombre_acumulado = nombre_acumulado + letra
  print("Nombre parcial:", nombre_acumulado)
print("Nombre completo:", nombre_acumulado)
