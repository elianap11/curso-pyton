compras = ["manzanas", "pan", "leche", "queso"]
#modifico las listas porque son mutables
compras[1] = "yogur"
#append lo agrega al fnal
compras.append("cereales")
#eliminar
compras.remove("leche")
cantidad_compras = len(compras)
print("Cantidad de compras", cantidad_compras)
print(compras)

#Así lo recorremos
productos = ["manzanas", "pan", "leche", "queso"]
indice = 0

while indice < len(productos):
    print("Productos", indice + 1, ":" , productos[indice])
    indice = indice + 1
    
    
    