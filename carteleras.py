peliculas = ["La La Land","Whiplash","Django Unchained","El Increible Castillo Vagabundo","Parasite","Inception"]

def mostrar_cartelera():
    print("\n--- Cartelera de Películas ---")
    for i, pelicula in enumerate(peliculas, 1):
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
directores = [
    "Damien Chazelle",
    "Quentin Tarantino",
    "Christopher Nolan",
    "Bong Joon-ho",
    "Hayao Miyazaki",
    "Stanley Kubrick"
]
#-------------------------------------------------------------------------------------------------------
def eliminar_pelicula():
    mostrar_cartelera()
    try:
        indice = int(input("Ingrese el índice de la película que desea eliminar: ")) - 1
        if 0 <= indice < len(peliculas):
            pelicula_eliminada = peliculas.pop(indice)
            print(f"La película '{pelicula_eliminada}' ha sido eliminada de la cartelera.")
        else:
            print("Índice inválido. Por favor, ingrese un índice dentro del rango.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

#-------------------------------------------------------------------------------------------------------
def peliculas_por_inicial():
    letra = input("Ingrese la letra inicial de las películas que desea ver: ").strip().upper()
    resultado = [p for p in peliculas if p.upper().startswith(letra)]
    if resultado:
        print(f"\nPelículas que comienzan con '{letra}':")
        for pelicula in resultado:
            print(pelicula)
    else:
        print(f"No se encontraron películas que comiencen con la letra '{letra}'.")
#-------------------------------------------------------------------------------------------------------
def buscar_letra_comun():
    print("\n--- Películas y Directores con la misma letra inicial ---")
    for pelicula in peliculas:
        for director in directores:
            if pelicula[0].upper() == director[0].upper():
                print(f"Película: {pelicula} - Director: {director}")
#-------------------------------------------------------------------------------------------------------
def mostrar_combinaciones():
    combinaciones = []
    for pelicula in peliculas:
        for director in directores:
            combinaciones.append((pelicula, director))
            print(f"Película: {pelicula}, Director: {director}")
    print(f"\nTotal de combinaciones posibles: {len(combinaciones)}")
#-------------------------------------------------------------------------------------------------------
def menu_cartelera():
    while True:
        print("\n--- Menú de Cartelera CineMarkos ---")
        print("1. Mostrar cartelera")
        print("2. Buscar película")
        print("3. Agregar película")
        print("4. Ordenar cartelera alfabéticamente")
        print("5. Eliminar película por índice")
        print("6. Buscar películas por letra inicial")
        print("7. Buscar películas y directores con la misma inicial")
        print("8. Mostrar todas las combinaciones de películas y directores")
        print("9. Volver al menú principal")

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
                eliminar_pelicula()
            case 6:
                peliculas_por_inicial()
            case 7:
                buscar_letra_comun()
            case 8:
                mostrar_combinaciones()
            case 9:
                print("Regresando al menu home.")
                break
            case _:
                print("Opcion no valida,try again")