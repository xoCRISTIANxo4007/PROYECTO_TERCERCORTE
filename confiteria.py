productos = {
    "Crispetas": {"precio": 10, "cantidad": 40},
    "Gaseosa": {"precio": 7.5, "cantidad": 35},
    "Nachos": {"precio": 8.75, "cantidad": 25},
    "Chocolate": {"precio": 3.5, "cantidad": 85}
}

combos = {
    1: {"items": {"Crispetas": 2, "Gaseosa": 2, "Chocolate": 1}, "precio": 30},
    2: {"items": {"Crispetas": 1, "Nachos": 1, "Gaseosa": 2}, "precio": 25},
    3: {"items": {"Nachos": 1, "Gaseosa": 1, "Chocolate": 1}, "precio": 15}
}
def vender_producto():
    print("\n--- Productos disponibles ---")
    for producto, detalles in productos.items():
        print(f"{producto}: {detalles['precio']}$ (Disponibles: {detalles['cantidad']})")

    try:
        producto = input("Ingrese el producto que desea comprar: ").capitalize()
        if producto not in productos:
            raise ValueError("Producto no disponible.")

        cantidad = int(input("Ingrese la cantidad deseada: "))
        if cantidad > productos[producto]["cantidad"]:
            raise ValueError("Cantidad solicitada supera el stock disponible.")

        total = cantidad * productos[producto]["precio"]
        productos[producto]["cantidad"] -= cantidad
        print(f"Total a pagar por {cantidad} {producto}(s): {total}$")

    except ValueError as e:
        print(f"Error: {e}")
def vender_combo():
    print("\n--- Combos disponibles ---")
    for combo, detalles in combos.items():
        productos_combo = ", ".join([f"{cantidad} {prod}" for prod, cantidad in detalles["items"].items()])
        print(f"Combo {combo}: {productos_combo} por {detalles['precio']}$")
    try:
        combo_elegido = int(input("Seleccione un combo (1-3): "))
        if combo_elegido not in combos:
            raise ValueError("Combo no disponible.")

        combo = combos[combo_elegido]["items"]
        for producto, cantidad in combo.items():
            if productos[producto]["cantidad"] < cantidad:
                raise ValueError(f"Stock insuficiente de {producto}. Disponibles: {productos[producto]['cantidad']}")

        # Reducir stock
        for producto, cantidad in combo.items():
            productos[producto]["cantidad"] -= cantidad

        total = combos[combo_elegido]["precio"]
        print(f"Total a pagar por el combo seleccionado: {total}$")

        # Dividir la cuenta si se desea
        dividir = input("¿Desea dividir la cuenta? (s/n): ").lower()
        if dividir == 's':
            personas = int(input("Ingrese el número de personas: "))
            if personas <= 0:
                raise ZeroDivisionError("El número de personas no puede ser menor o igual a cero.")
            print(f"Total por persona: {total / personas}$")
        else:
            print(f"Total a pagar: {total}$")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
def confiteria_menu():
    while True:
        print("\n--- Menu de Confitería ---")
        print("1. Comprar producto para uno")
        print("2. Comprar para varios")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: Debe ingresar un numero válido.")
            continue

        match opcion:
            case 1:
                vender_producto()
            case 2:
                vender_combo()
            case 3:
                break
            case _:
                print("Opcion no valida, Try again")