"""
Escribir un programa que guarde en variables el monto del ingreso de cada uno de los
primeros seis meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx”
donde “xxxxx” es el valor calculado.

"""
enero, febrero, marzo, abril, mayo, junio = 12, 200, 35, 76, 120, 80
promedio = (enero + febrero + marzo + abril + mayo + junio) / 6
print("El ingreso promedio en el semestre es de", promedio)
#f-strings 
print(f"El ingreso promedio en el semestre es de {promedio}")
print()