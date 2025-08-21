# FoodPlace - cálculo de venta interactivo por producto
company_name = "foodplace"
company_address = "Av. Siempre Viva 742, Springfield"

PRICES = {
    "Churrasco": 1500,
    "Completo": 1000,
    "Vegetariano": 2000,
    "Barros Luco": 3000
}

def format_clp(amount):
    """Formatea número a estilo CLP sin decimales: $1.500"""
    return f"${amount:,.0f}".replace(",", ".")

def pedir_entero(prompt):
    while True:
        try:
            v = input(prompt).strip()
            if v == "":
                return 0
            n = int(v)
            if n < 0:
                print("Ingrese un número entero no negativo.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def mostrar_menu():
    print("="*40)
    print(f"{company_name.upper():^40}")
    print(f"{company_address:^40}")
    print("Productos disponibles:")
    for i, (name, price) in enumerate(PRICES.items(), start=1):
        print(f" {i}. {name:<12} {format_clp(price)}")
    print(" 5. Terminar compra")
    print("Escriba el nombre o el número del producto para agregarlo.")
    print("="*40)

def obtener_producto_por_entrada(user_input):
    user_input = user_input.strip()
    if user_input == "":
        return None
    if user_input.lower() in ("fin", "done", "salir", "exit"):
        return "FIN"
    if user_input.isdigit():
        idx = int(user_input)
        if idx == 5:
            return "FIN"
        if 1 <= idx <= len(PRICES):
            return list(PRICES.keys())[idx-1]
        else:
            return None
    for name in PRICES:
        if user_input.lower() == name.lower():
            return name
    for name in PRICES:
        if name.lower().startswith(user_input.lower()):
            return name
    return None

def main():
    mostrar_menu()
    quantities = {name: 0 for name in PRICES}

    while True:
        entrada = input("Producto (nombre/número / 5=terminar): ").strip()
        producto = obtener_producto_por_entrada(entrada)
        if producto == "FIN":
            break
        if producto is None:
            print("Producto no reconocido. Intente nuevamente.")
            continue
        cantidad = pedir_entero(f"¿Cuántos {producto} desea?: ")
        if cantidad == 0:
            print("Cantidad 0 — no se agrega nada.")
            continue
        quantities[producto] += cantidad
        print(f"Agregados {cantidad} x {producto}. (Total {quantities[producto]} de este producto)")

    if sum(quantities.values()) == 0:
        print("No se han ingresado productos. Total $0.")
        return

    tiene_desc = input("¿Tiene código de descuento? (s/n): ").strip().lower()
    descuento_rate = 0.10 if tiene_desc.startswith("s") else 0.0

    line_totals = {name: PRICES[name] * qty for name, qty in quantities.items()}
    subtotal = sum(line_totals.values())
    descuento = round(subtotal * descuento_rate)
    subtotal_desc = subtotal - descuento
    iva = round(subtotal_desc * 0.19)
    total = subtotal_desc + iva

    # Ticket
    print("\n" + "="*40)
    print(f" TICKET - {company_name.upper()} | {company_address}")
    print("="*40)
    print(f"{'Producto':<16}{'Cant.':>6}{'Precio':>10}{'Total':>12}")
    print("-"*40)
    for name in PRICES:
        q = quantities[name]
        if q == 0:
            continue
        price = PRICES[name]
        lt = line_totals[name]
        print(f"{name:<16}{q:>6}{format_clp(price):>10}{format_clp(lt):>12}")
    print("-"*40)
    print(f"{'SUBTOTAL:':<28}{format_clp(subtotal):>12}")
    if descuento_rate > 0:
        print(f"{'Descuento 10%:':<28}-{format_clp(descuento):>11}")
        print(f"{'SUBTOTAL (descuento):':<28}{format_clp(subtotal_desc):>12}")
    print(f"{'IVA (19%):':<28}{format_clp(iva):>12}")
    print(f"{'TOTAL A PAGAR:':<28}{format_clp(total):>12}")
    print("="*40)
    print("Gracias por su compra :)")

if __name__ == "__main__":
    main()
