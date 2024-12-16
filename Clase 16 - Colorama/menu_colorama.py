from colorama import init, Fore, Back, Style
init(autoreset=True)
# Función del menú principal que permite acceder a cada función
def mostrar_menu():
    while True:
        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + "\n" + "Menú de Gestión de Personas".center(60, " ") + Style.RESET_ALL)       
        print(Style.BRIGHT + Fore.CYAN + "1. Registrar persona")
        print(Style.BRIGHT + Fore.CYAN + "2. Mostrar personas")
        print(Style.BRIGHT + Fore.CYAN + "3. Actualizar edad de una persona")
        print(Style.BRIGHT + Fore.CYAN + "4. Eliminar persona")
        print(Style.BRIGHT + Fore.CYAN + "5. Buscar persona")
        print(Style.BRIGHT + Fore.CYAN + "6. Reporte de personas menores de edad")
        print(Style.BRIGHT + Fore.RED + "7. Salir")
        opcion = input(Fore.YELLOW + "\nSeleccione una opción: ")
        if opcion == "7":
            print(Fore.RED + "Saliendo del programa...")
            break
        else:
            print(Back.RED + Fore.WHITE + "Opción inválida. Por favor, intente nuevamente.")
# Iniciar el programa llamando al menú principal
mostrar_menu()