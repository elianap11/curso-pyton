def mostrar_menu():
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Salir")
    
mostrar_menu()

def sumar(a, b):
    resultado = a + b
    print("El resultado es:", resultado)

sumar(5, 3)

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")
saludar("Carlos")

def saludar(nombre="invitado"):
    print("Hola", nombre)

saludar() # Usa el valor por defecto
saludar("Lucía") # Sobrescribe el valor por defecto