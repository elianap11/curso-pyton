cantidad = int(input("Ingresá la cantidad de productos: "))

while cantidad <= 0:
  print("La cantidad debe ser mayor que 0.")
  cantidad = int(input("Por favor, ingresá nuevamente la cantidad de productos: "))
  
print("Has ingresado una cantidad válida:", cantidad)