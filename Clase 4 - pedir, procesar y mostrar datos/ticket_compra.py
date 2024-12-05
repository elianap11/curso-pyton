'''
Programa que pida al usuario el nombre, la cantidad y el valor unitario de tres productos. 
Después, tiene que calcular el importe de IVA (21%) de cada uno y mostrar en la terminal un 
ticket de compra con todos los datos.
'''
# Solicitar el nombre, la cantidad y el valor unitario de tres productos
nombre1 = input("Ingresá el nombre del primer producto: ")
cantidad1 = int(input("Ingresá la cantidad: "))
valor_unitario1 = float(input("Ingresá el valor unitario: "))
nombre2 = input("Ingresá el nombre del segundo producto: ")
cantidad2 = int(input("Ingresá la cantidad: "))
valor_unitario2 = float(input("Ingresá el valor unitario: "))
nombre3 = input("Ingresá el nombre del tercer producto: ")
cantidad3 = int(input("Ingresá la cantidad: "))
valor_unitario3 = float(input("Ingresá el valor unitario: "))

# Calcular el importe de IVA (21%) para cada producto
iva1 = (valor_unitario1 * cantidad1) * 0.21
iva2 = (valor_unitario2 * cantidad2) * 0.21
iva3 = (valor_unitario3 * cantidad3) * 0.21

# Calcular el costo total de cada producto (sin IVA)
costo1 = valor_unitario1 * cantidad1
costo2 = valor_unitario2 * cantidad2
costo3 = valor_unitario3 * cantidad3

# Calcular el total con IVA
total_con_iva1 = costo1 + iva1
total_con_iva2 = costo2 + iva2
total_con_iva3 = costo3 + iva3

# Mostrar el ticket de compra simulado
print("\n--- TICKET DE COMPRA ---")
print("Cantidad\tDescripción\t\tPrecio Unitario\t\tTotal")
print(cantidad1, "\t\t", nombre1, "\t\t\t", 
format(valor_unitario1, ".2f"), "\t\t\t", 
format(total_con_iva1, ".2f"))
print(cantidad2, "\t\t", nombre2, "\t\t\t",
format(valor_unitario2, ".2f"), "\t\t\t", 
format(total_con_iva2, ".2f"))
print(cantidad3, "\t\t", nombre3, "\t\t\t", 
format(valor_unitario3, ".2f"), "\t\t\t", 
format(total_con_iva3, ".2f"))
print("-------------------------------------------")

# Calcular el total neto y el IVA total
total_neto = costo1 + costo2 + costo3

#Ejemplo en clase
producto1 = input("Ingresá el nombre del primer producto: ")
cantidad1 = int(input("Ingresá la cantidad: "))
valor_unitario1 = float(input("Ingresá el valor unitario: "))

producto2 = input("Ingresá el nombre del segundo producto: ")
cantidad2 = int(input("Ingresá la cantidad: "))
valor_unitario2 = float(input("Ingresá el valor unitario: "))

producto3 = input("Ingresá el nombre del tercer producto: ")
cantidad3 = int(input("Ingresá la cantidad: "))
valor_unitario3 = float(input("Ingresá el valor unitario: "))

#Calcular el importe del IVA 21% 
iva1 = (valor_unitario1 * cantidad1) * 0.21
iva2 = (valor_unitario2 * cantidad2) * 0.21
iva3 = (valor_unitario3 * cantidad3) * 0.21

#Calcular el costo total de cada producto sin el iva
costo1 = valor_unitario1 * cantidad1
costo2 = valor_unitario2 * cantidad2
costo3 = valor_unitario3 * cantidad3

#Calcular el total con IVA
total_iva1 = costo1 + iva1 
total_iva2 = costo2 + iva2 
total_iva3 = costo3 + iva3 

print("\n--- TICKET DE COMPRA ---")
print("Cantidad\tDescripción\t\tPrecio Unitario\t\tTotal")
print(cantidad1, "\t\t", producto1, "\t\t\t",
format(valor_unitario1, ".2f"), "\t\t\t",
format(total_iva1, ".2f"))
print(cantidad2, "\t\t", producto2, "\t\t\t",
format(valor_unitario2, ".2f"), "\t\t\t",
format(total_iva2, ".2f"))
print(cantidad3, "\t\t", producto3, "\t\t\t",
format(valor_unitario3, ".2f"), "\t\t\t",
format(total_iva3, ".2f"))