import carteleras
import confiteria
import miembros
import salas
from confiteria import vender_producto, vender_combo
men=""" 
█▀█ █▀█ █▄█ ▄▀█ █░░   █▀▀ █ █▀▄▀█ █░░ █▀
█▀▄ █▄█ ░█░ █▀█ █▄▄   █▀░ █ █░▀░█ █▄▄ ▄█
"""
def menu():
    while True:
        print(men)
        print("***** Menu CineMarkos *****")
        print("1. Confitería")
        print("2. Miembros")
        print("3. Cartelera")
        print("4. Salas")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error,debe ingresar un numero válido.")
            continue

        match opcion:
            case 1:
                confiteria.confiteria_menu()
            case 2:
                miembros.menu_miembros()
            case 3:
                carteleras.menu_cartelera()
            case 4:
                salas.menu_salas()
            case 5:
                print("Adiosssssssssss")
                break
            case _:
                print("Opcion no valida mi rey try again")
if __name__ == "__main__":
    try:
        menu()
    except ImportError as e:
        print(f"Error al importar módulos: {e}")

