from colorama import init, Fore, Back, Style

# Autoreset: cada vez que usemos un color o un estilo en la consola, ese formato se aplicará sólo a esa línea o bloque de texto específico
init(autoreset=True)

# Convert: ajusta automáticamente la compatibilidad en sistemas Windows
# init(convert = True)

# Strip: los códigos de formato que no son compatibles se eliminan de manera automática.
# init(strip=True)


print(Fore.RED + 'Este texto es rojo!')
print(Fore.GREEN + 'Este texto es verde!')
print(Back.YELLOW + 'Este texto tiene fondo amarillo!')

print(Fore.BLUE + Back.WHITE + Style.BRIGHT + 'Este texto es azul con fondo blanco y brillante!')

print(Back.CYAN +"\n--- Menú Principal ---" )
print(Fore.GREEN + "1. Agregar productos")
print(Fore.YELLOW + "2. Eliminar productos")
print(Fore.RED + "3. Lista de productos")


# Style.DIM reduce la intensidad del color
print(Style.DIM + "Nota: asegúrate de ingresar un ID válido.")