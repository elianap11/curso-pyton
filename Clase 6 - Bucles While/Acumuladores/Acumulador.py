'''
El acumulador opera de manera similar a un contador pero, en lugar de sumar de a uno, 
o que hace es acumular un valor que puede ir variando. Mientras que el contador te dice 
cuántas veces pasó algo, esta herramienta indica cuánto se acumuló a lo largo del tiempo 
o de una serie de acciones

'''

total = 0 # Inicializamos el acumulador en cero
dia = 1   # Inicializamos el contador en cero

# Simulamos ventas de productos en una tienda, usando un bucle
# Supongamos que ingresamos productos durante 3 días
while dia <= 3: 
   print("Día", dia)
   venta = float(input("Monto de las ventas del día: "))

   total = total + venta # Acumulamos el monto en el acumulador
   dia = dia + 1        # Incrementamos el contador:
  
# Al final del bucle, mostramos el total acumulado
print("El total de las ventas ingresadas es: $", total)