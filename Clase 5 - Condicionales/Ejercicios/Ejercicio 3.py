A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

promedio = ((A + B + C + D) / 4)

if promedio >= 90:
    print("Excelente")
elif promedio >= 75:
    print("Muy bueno")
elif promedio >= 60:
    print("Bueno")
else:
    print("Desaprobado")
    
print(f"El promedio es: {promedio}")
    
