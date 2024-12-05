'''
Imagina que estás desarrollando un sistema que le ayude a un docente a clasificar a sus 
estudiantes según sus calificaciones. El programa debe permitir ingresar la nota de un 
estudiante y luego clasificarla según las siguientes categorías:
90 o más: "Excelente"
75 a 89: "Muy bueno"
60 a 74: "Bueno"
Menos de 60: "No aprobado"
'''
ingreso_notas = int(input("Ingresá tu nota: "))
if ingreso_notas >= 90:
    print("Excelente")
elif ingreso_notas >=75 and ingreso_notas <= 89:
    print("Muy bueno")
elif ingreso_notas >=60 and ingreso_notas <= 74:
    print("Bueno")
else:
    print("No aprobado")
