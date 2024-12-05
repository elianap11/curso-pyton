# Scope: da error porque la variable es de la función: Alcance local

def saludar():
    mensaje = "Hola, ¿cómo estás?"
    print(mensaje)
    
saludar()
#print(mensaje) # Esto va a dar un error

# Alcance global
mensaje_global = "Hola, ¿cómo estás?"

def saludar():
    print(mensaje_global)

saludar()
print(mensaje_global) # Esto funciona bien