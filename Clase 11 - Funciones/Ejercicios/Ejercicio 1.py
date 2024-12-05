'''
Gestión de descuentos
Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a
desarrollar un programa que permita calcular el precio final de un producto después de
aplicar un descuento. Para hacerlo:
1. Crea una función que reciba como parámetros el precio original del producto y el
porcentaje de descuento, y que retorne el precio final con el descuento aplicado.
2. Luego, solicitá que se ingrese el precio y el porcentaje de descuento. Mostrá el
precio final después de aplicar el descuento
'''

def calcular_precio_final(precio_original, porcentaje_descuento):
    """
    Calcula el precio final después de aplicar un descuento.
    
    Parámetros:
    precio_original (float): El precio original del producto.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar.
    
    Retorna:
    float: El precio final después del descuento.
    """
    descuento = (porcentaje_descuento / 100) * precio_original
    precio_final = precio_original - descuento
    return precio_final

# Solicitar precio original y porcentaje de descuento
precio_ingresado = float(input("Ingrese el precio original del producto: "))
descuento_ingresado = float(input("Ingrese el porcentaje de descuento: "))

# Calcular el precio final
precio_final = calcular_precio_final(precio_ingresado, descuento_ingresado)

# Mostrar el resultado
print(f"El precio final después de aplicar el descuento es: {precio_final:.2f}")