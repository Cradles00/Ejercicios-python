# --- Tienda de artículos ---
precio_mascarilla = 1000
precio_guantes = 1000
precio_delantal = 2000
precio_amonio = 3000

print("\n--- TIENDA LIMPIEZA SANITARIA ---")
print("Lista de precios:")
print(f"1. Mascarilla clínica: ${precio_mascarilla}")
print(f"2. Guantes clínicos: ${precio_guantes}")
print(f"3. Delantal clínico: ${precio_delantal}")
print(f"4. Amonio Cuaternario: ${precio_amonio}")

cant_mascarilla = int(input("\nIngrese la cantidad de mascarillas: "))
cant_guantes = int(input("Ingrese la cantidad de guantes: "))
cant_delantal = int(input("Ingrese la cantidad de delantales: "))
cant_amonio = int(input("Ingrese la cantidad de amonio cuaternario: "))

subtotal = (cant_mascarilla * precio_mascarilla +
            cant_guantes * precio_guantes +
            cant_delantal * precio_delantal +
            cant_amonio * precio_amonio)

respuesta = input("\n¿Tiene código de descuento? (s/n): ").lower()
descuento = 0
if respuesta == "s":
    descuento = float(input("Ingrese porcentaje de descuento (%): "))

total_descuento = subtotal - (subtotal * descuento / 100)
total_final = total_descuento * 1.19  # con IVA 19%

print("\n--- FACTURA ---")
print(f"Subtotal: ${subtotal}")
print(f"Descuento aplicado: {descuento}%")
print(f"Total con descuento: ${total_descuento:.2f}")
print(f"Total final con IVA (19%): ${total_final:.2f}")

# --- boleta ---
boleta = []
boleta.append("===================================")
boleta.append("     TIENDA LIMPIEZA SANITARIA     ")
boleta.append("           *** BOLETA ***          ")
boleta.append("           Av.Ecuador 153          ")
boleta.append("          rut:72.435.677.1         ")
boleta.append("===================================\n")
boleta.append("Artículo               Cant   Total")
boleta.append("-----------------------------------")
if cant_mascarilla > 0:
    boleta.append(f"Mascarilla clínica     {cant_mascarilla:<5} ${cant_mascarilla * precio_mascarilla}")
if cant_guantes > 0:
    boleta.append(f"Guantes clínicos       {cant_guantes:<5} ${cant_guantes * precio_guantes}")
if cant_delantal > 0:
    boleta.append(f"Delantal clínico       {cant_delantal:<5} ${cant_delantal * precio_delantal}")
if cant_amonio > 0:
    boleta.append(f"Amonio Cuaternario     {cant_amonio:<5} ${cant_amonio * precio_amonio}")

boleta.append("-----------------------------------")
boleta.append(f"Subtotal:                     ${subtotal}")
boleta.append(f"Descuento: {descuento}%")
boleta.append(f"Total con descuento:          ${total_descuento:.2f}")
boleta.append(f"IVA (19%):                    ${total_descuento*0.19:.2f}")
boleta.append("===================================")
boleta.append(f"TOTAL A PAGAR:                ${total_final:.2f}")
boleta.append("===================================\n")
boleta.append("   ¡Gracias por su compra!  ")


print("\n".join(boleta))
