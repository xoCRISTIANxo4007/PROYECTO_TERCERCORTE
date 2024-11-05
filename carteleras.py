
peliculas = ["La La Land","Whiplash","Django Unchained","El Increible Castillo Vagabundo","Parasite","Inception"]

def mostrar_cartelera():
    print("\n--- Cartelera de Películas ---")
    for i, pelicula in enumerate(peliculas, start=1):
        print(f"{i}. {pelicula}")
#-------------------------------------------------------------------------------------------------------
def buscar_pelicula():
    try:
        titulo = input("Ingrese el título de la película que desea buscar: ")
        if any(pelicula.lower() == titulo for pelicula in peliculas):
            print(f"La película se encuentra en la cartelera.")
        else:
            print(f"La película no se encuentra en la cartelera.")
    except Exception as e:
        print(f"Error inesperado al buscar la película: {e}")

#-------------------------------------------------------------------------------------------------------
def agregar_pelicula():
    try:
        nueva_pelicula = input("Ingrese el título de la película que desea agregar: ").strip()
        if nueva_pelicula.lower() in [p.lower() for p in peliculas]:
            print(f"La película '{nueva_pelicula}' ya está en la cartelera.")
        else:
            peliculas.append(nueva_pelicula)
            print(f"La película '{nueva_pelicula}' ha sido añadida a la cartelera.")
    except Exception as e:
        print(f"Error inesperado al agregar la película: {e}")
#-------------------------------------------------------------------------------------------------------
def ordenar_alfabeticamente():
    try:
        peliculas.sort()
        print("\nCartelera ordenada alfabéticamente:")
        mostrar_cartelera()
    except Exception as e:
        print(f"Error inesperado al ordenar la cartelera: {e}")

#-------------------------------------------------------------------------------------------------------
def menu_cartelera():
    while True:
        print("**** CARTELERAS ****")
        print("1. Mostrar cartelera")
        print("2. Buscar película")
        print("3. Agregar película")
        print("4. Ordenar cartelera alfabéticamente")
        print("5. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        match opcion:
            case 1:
                mostrar_cartelera()
            case 2:
                buscar_pelicula()
            case 3:
                agregar_pelicula()
            case 4:
                ordenar_alfabeticamente()
            case 5:
                print("Regresando al menú principal.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
