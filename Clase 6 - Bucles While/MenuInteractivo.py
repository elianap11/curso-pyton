opcion = 0

while opcion != 3:
    print("\nMenú de Opciones")
    print("1. Ver productos")
    print("2. Agregar un producto")
    print("3. Salir")
    opcion = int(input("Seleccioná una opción: "))

    if opcion == 1:
        print("Mostrando productos...")
    elif opcion == 2:
        print("Agregando un producto...")
    elif opcion == 3:
        print("Saliendo del menú.")
    else:
        print("Opción no válida. Por favor, ingresá una opción entre 1 y 3.")
