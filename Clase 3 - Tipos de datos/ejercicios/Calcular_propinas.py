'''
Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.
El script debe solicitar el monto total de la cuenta y el porcentaje de propina que deseás
dejar. Utilizando operadores aritméticos, calculá la cantidad de propina y el total a pagar 
(incluyendo la propina). Finalmente, mostrá los resultados en la pantalla
'''

monto_cuenta = float(input("Ingresa el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 10 para 10%): "))
propina = (monto_cuenta * porcentaje_propina) / 100
total_pagar = monto_cuenta + propina
print("La propina es:", propina)
print("El total a pagar es:",total_pagar)