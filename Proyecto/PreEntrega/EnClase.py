producto = []
cantidad = []
precio = []

while True: #Opcion para el usuario
    print("Menu Principal")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Ver producto")
    print("5. Salir")
    print()
    opcion = input("Seleccione una opcion:")
    if opcion == "1":
        ap = input("Ingrese el nombre de su producto:")
        ac = int (input("Ingrese la cantidad de su producto:"))
        pac = int(input("Ingrese precio de su producto:"))

        producto.append(ap)
        cantidad.append(ac)
        precio.append(pac)
    elif opcion == "2":
        buscar = input("Ingresa el nombre del producto:")
        posicion = producto.index(buscar)
        print("El nombre del producto es:", producto[posicion])
        print("La cantidad del producto es:", cantidad[posicion])
        print("El precio del producto es:", precio[posicion])
    elif opcion == "3":
        buscar = input("Ingresa el nombre del producto a modificar:")
        posicion = producto.index(buscar)
        ap = input("Ingrese el nombre de su producto:")
        ac = int(input("Ingrese la cantidad del producto:"))
        pac = int(input("Ingrese el precio del producto:"))

        producto[posicion] = ap
        cantidad[posicion] = ac
        precio[posicion] = pac
    elif opcion == "4":
        print("El nombre es:", producto)
        print("La cantidad es:", cantidad)
        print("El precio es;", precio)
    else:
        break