suma = 0

for cont in range(15):
    print(cont)
    suma = suma + cont
    if cont == 3:
        break

print("La suma es:", suma)

print("\n##################################################\n")

suma = 0

for cont in range(5):
   num= int(input("Ingrese un número: "))
   suma = suma + num

print('La suma es:',suma)
print('El promedio es:',suma/(cont+1))

print("\n##################################################\n")

total = 0

for i in range(5):
    importe = float(input("Ingrese el importe: "))
    total = total + importe

print("El total de los importes ingresados es:" ,total)

print("\n##################################################\n")

for i in range(5):
    print(i)
    
print("\n##################################################\n")
    
for i in range(3, 7):
    print(i)
    
print("\n##################################################\n")
    
for i in range(0, 10, 2):
    print(i)
    
print("\n##################################################\n")

for i in range(10, 0, -2):
    print(i)
    
print("\n##################################################\n")

frutas = ["manzana", "banana", "naranja"]

for i in range(len(frutas)):
    print(f"Fruta {i + 1}: {frutas[i]}")
    
print("\n##################################################\n")
    
for num in range(5, 16, 2):
    print(num, end=" ")