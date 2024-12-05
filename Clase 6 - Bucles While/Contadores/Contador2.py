#Otro Ejemplo
intentos = 0 # Inicializamos el contador
cantidad = int(input("Ingresá la cantidad de productos: "))

while cantidad <= 0:
# Aumentamos el contador por cada error
  intentos = intentos + 1
  print("Error: La cantidad debe ser mayor que 0.")
  cantidad = int(input("Por favor, ingresá nuevamente la cantidad de productos: "))
  print(f"Ingresaste un valor válido después de {intentos} intentos.")