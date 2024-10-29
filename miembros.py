nombres = []
edades = []
pelicula_favorita = []

def agregar_miembro():
    nombre = input("Ingrese el nombre del nuevo miembro: ")
    edad = int(input("Ingrese la edad del nuevo miembro: "))
    pelicula = input("Ingrese la película favorita del nuevo miembro: ")

    nombres.append(nombre)
    edades.append(edad)
    pelicula_favorita.append(pelicula)

    print(f"Miembro '{nombre}' agregado exitosamente.")

#-----------------------------------------------------------------------------------------------------------------------------------
def eliminar_miembro():
    try:
        nombre = input("Ingrese el nombre del miembro que desea eliminar: ")
        index = nombres.index(nombre)
        nombres.pop(index)
        edades.pop(index)
        pelicula_favorita.pop(index)
        print(f"Miembro '{nombre}' eliminado exitosamente.")

    except ValueError:
        print("Error: El nombre ingresado no existe en la lista de miembros.")
    except IndexError:
        print("Error: Índice fuera de rango al intentar eliminar al miembro.")

#-------------------------------------------------------------------------------------------------------------------------------------
def modificar_miembro():
    try:
        nombre = input("Ingrese el nombre del miembro que desea modificar: ")
        index = nombres.index(nombre)

        print("¿Qué atributo desea modificar?")
        print("1. Nombre")
        print("2. Edad")
        print("3. Película Favorita")

        try:
            opcion = int(input("Seleccione una opción (1-3): "))
        except ValueError:
            print("Error, Ingrese un número válido.")
            return

        match opcion:
            case 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nombres[index] = nuevo_nombre
                print("Nombre modificado exitosamente.")
            case 2:
                nueva_edad = int(input("Ingrese la nueva edad: "))
                edades[index] = nueva_edad
                print("Edad modificada exitosamente.")
            case 3:
                nueva_pelicula = input("Ingrese la nueva película favorita: ")
                pelicula_favorita[index] = nueva_pelicula
                print("Película favorita modificada exitosamente.")
            case _:
                print("Opción no válida.")

    except ValueError:
        print("Error: El nombre ingresado no existe en la lista de miembros.")
        return modificar_miembro()


#-------------------------------------------------------------------------------------------------------------------------------------
def promedio_edades():
    if edades:
        promedio = sum(edades) / len(edades)
        print(f"El promedio de edades de los miembros es: {promedio}")
    else:
        print("No hay miembros registrados para calcular el promedio.")
#--------------------------------------------------------------------------------------------------------------------------------
def menu_miembros():
    while True:
        print("--- Miembros del Cine     ---")
        print("1. Agregar miembro")
        print("2. Eliminar miembro")
        print("3. Modificar miembro")
        print("4. Calcular promedio de edades")
        print("5. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Ingrese un numero válido.")
            continue

        match opcion:
            case 1:
                agregar_miembro()
            case 2:
                eliminar_miembro()
            case 3:
                modificar_miembro()
            case 4:
                promedio_edades()
            case 5:
                print("Regresando al menú principal.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
