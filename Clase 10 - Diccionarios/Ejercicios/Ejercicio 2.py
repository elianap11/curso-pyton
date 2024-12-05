'''
Consultar stock en inventario
El inventario de una tienda está almacenado en un diccionario, donde las claves son los
nombres de los productos y los valores son las cantidades disponibles en stock. Creá un
programa que:
1. Te permita ingresar el nombre de un producto.
2. Utilice el método .get() para buscar el stock disponible. Si el producto no existe,
deberá mostrar un mensaje diciendo "Producto no encontrado".
3. Si el producto está disponible, mostrará cuántas unidades quedan en stock.
'''

# Diccionario inicial con productos y su stock
productos = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 25
}

# Ingresar el nombre de un producto
producto_buscado = input("Ingresa el nombre del producto: ").lower

# Utilizar el método .get() para buscar el stock
stock = productos.get(producto_buscado)

# Comprobar si el producto existe en el diccionario
if stock is None:
    print("Producto no encontrado.")
else:
    print(f"Stock disponible de {producto_buscado}: {stock}")
    
    
#en clase
inventario = {
    "manzanas": 50,
    "bananas": 30,
    "peras": 20,
    "uvas": 15,
    "naranjas": 40
}

#Solicitar el nombre del producto al usuario

producto = input("Ingresa el nombre del producto: ").lower()

#Usar método.get() para obtener el stock del product.

stock = inventario.get(producto)

#Verificar si el producto existe en el inventario
if stock is None:
    print("Producto no encontrado")
else:
    print(f"Quedan {stock} unidades de {producto} en stock.")