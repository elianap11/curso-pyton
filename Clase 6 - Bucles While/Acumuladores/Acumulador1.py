total_productos = 0 # Inicializamos el acumulador
# Simulamos el ingreso de productos durante 3 días
for dia in range(3):
  print("Día", dia + 1, ":")
  productos_ingresados = int(input("Productos ingresados en el día: "))
# Vamos sumando la cantidad de productos al acumulador
  total_productos = total_productos + productos_ingresados
  print("El total de productos agregados al inventario es:", total_productos)