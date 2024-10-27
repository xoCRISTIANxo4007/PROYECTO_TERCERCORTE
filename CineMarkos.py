import confiteria
from confiteria import vender_producto, vender_combo
men=""" 
█▀█ █▀█ █▄█ ▄▀█ █░░   █▀▀ █ █▀▄▀█ █░░ █▀
█▀▄ █▄█ ░█░ █▀█ █▄▄   █▀░ █ █░▀░█ █▄▄ ▄█
"""
def menu():
    while True:
        print(men)
        print("\n--- Menú CineMarkos ---")
        print("1. Confitería")
        print("2. Miembros")
        print("3. Cartelera")
        print("4. Salas")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            continue

        match opcion:
            case 1:
                confiteria.confiteria_menu()
            case 2:
                print("Nada, no hay no existe.")
            case 3:
                print("Nada, no hay no existe.")
            case 4:
                print("Nada, no hay no existe.")
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

# primero haces una commit para actualizar los datos, luego vas al git y haces update y push
