total_productos = 0 # Inicializamos el contador
for dia in range(3): # Supongamos que ingresamos productos durante 3 días
    print("Día",dia + 1, ":")
    productos_agregados = int(input("Productos ingresados en el día: "))
    total_productos = total_productos + productos_agregados
    print("Se ingresaron",total_productos,"productos en total al inventario.")