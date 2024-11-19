import random


sala_1 = [[random.choice([0, 1]) for _ in range(10)] for _ in range(8)]  # 8x10
sala_2 = [[random.choice([0, 1]) for _ in range(12)] for _ in range(10)]  # 10x12
sala_3 = [[random.choice([0, 1]) for _ in range(8)] for _ in range(6)]  # 6x8

salas = [sala_1, sala_2, sala_3]


def mostrar_sala(numero_sala):
    try:
        sala = salas[numero_sala - 1]
        print(f"\n--- Sala {numero_sala} ---")
        for fila in sala:
            print(" ".join(['O' if asiento == 0 else 'X' for asiento in fila]))
    except IndexError:
        print("Numero de sala invalido")


def reservar_asiento(numero_sala, fila, columna):
    try:
        sala = salas[numero_sala - 1]
        if sala[fila - 1][columna - 1] == 0:
            sala[fila - 1][columna - 1] = 1
            print(f"Asiento en fila {fila}, columna {columna} reservado exitosamente.")
        else:
            print(f"El asiento en fila {fila}, columna {columna} ya está ocupado.")
    except IndexError:
        print("Fila o columna fuera de rango.")
    except ValueError:
        print("No señor, ingrese un numero valido")


def calcular_ingresos(numero_sala):
    try:
        sala = salas[numero_sala - 1]
        ingresos = 0
        for i, fila in enumerate(sala):
            precio = 10 if i < 3 else (8 if i < 6 else 6)
            ingresos += sum(asiento == 1 for asiento in fila) * precio
        print(f"Los ingresos totales de la Sala {numero_sala} son: ${ingresos}")
    except IndexError:
        print("No señor, ingrese un numero valido")


def sala_mas_ocupada():
    ocupaciones = []
    for i, sala in enumerate(salas):
        total_asientos = sum(len(fila) for fila in sala)
        asientos_ocupados = sum(asiento == 1 for fila in sala for asiento in fila)
        ocupaciones.append((i + 1, asientos_ocupados / total_asientos * 100))

    sala_mayor = max(ocupaciones, key=lambda x: x[1])
    print(f"La sala más ocupada es la Sala {sala_mayor[0]} con un {sala_mayor[1]:.2f}% de ocupación.")


def menu_salas():
    while True:
        print("***** SALAS *****")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Calcular ingresos")
        print("4. Ver sala más ocupada")
        print("5. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("No señor, ingrese un numero valido.")
            continue

        match opcion:
            case 1:
                try:
                    numero_sala = int(input("Ingrese el número de sala (1-3): "))
                    mostrar_sala(numero_sala)
                except ValueError:
                    print("No señor, ingrese un numero valido.")
            case 2:
                try:
                    numero_sala = int(input("Ingrese el número de sala (1-3): "))
                    fila = int(input("Ingrese el número de fila: "))
                    columna = int(input("Ingrese el número de columna: "))
                    reservar_asiento(numero_sala, fila, columna)
                except ValueError:
                    print("")
            case 3:
                try:
                    numero_sala = int(input("Ingrese el número de sala (1-3): "))
                    calcular_ingresos(numero_sala)
                except ValueError:
                    print("No señor, ingrese un numero valido.")
            case 4:
                sala_mas_ocupada()
            case 5:
                print("Regresando al menú principal.")
                break
            case _:
                print("Opcion invalida, try again.")
