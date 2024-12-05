# Lista de productos
productos = ["P001", "P002", "P003", "P004", "P005"]
# Producto que queremos encontrar
producto_a_buscar = "P003"
# Recorremos la lista buscando el producto
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto encontrado:", producto)
        break # Detenemos el bucle al encontrar el producto
    print("Buscando...")

print("Fin de la búsqueda.")

print("\n##################################################\n")