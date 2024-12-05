ventas = []
seguir = "S"

# Registramos las ventas hasta que el usuario decida no ingresar más
while seguir == "S":
    producto = input("Ingresá el nombre del producto vendido: ")
    ventas.append(producto)
    seguir = input("¿Querés registrar otra venta? (S/N): ").upper()

# Mostramos los productos vendidos al final del día
print("\nProductos vendidos hoy:")

indice = 0
while indice < len(ventas):
    print("Producto", indice + 1, ":", ventas[indice])
    indice = indice + 1
