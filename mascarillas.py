
def mostrar_menu():
    print("\n" + "="*50)
    print("        MEDICARP - MASCARILLAS LAVABLES")
    print("="*50)
    print("1. Realizar compra")
    print("2. Salir")
    print("="*50)

def calcular_compra():
    print("\n" + "="*50)
    print("               REALIZAR COMPRA")
    print("="*50)
    print("Precio unitario: $500")
    
    # Solicitar cantidad de mascarillas con validación
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de mascarillas a comprar: "))
            if cantidad > 0:
                break
            else:
                print("Por favor ingrese un número mayor a cero.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
    
    # Calcular subtotal
    subtotal = cantidad * 500
    
    # Calcular costo de envío
    if subtotal > 15000:
        envio = 0
        tipo_envio = "GRATIS (compra superior a $15.000)"
    else:
        print("\nOpciones de envío:")
        print("1. Pedro Aguirre Cerda - $1.000")
        print("2. Comuna aledaña - $2.000")
        print("3. Otra comuna - $3.000")
        
        # Validar opción de envío
        while True:
            try:
                opcion = int(input("Seleccione su comuna (1-3): "))
                if opcion == 1:
                    envio = 1000
                    tipo_envio = "Pedro Aguirre Cerda"
                    break
                elif opcion == 2:
                    envio = 2000
                    tipo_envio = "Comuna aledaña"
                    break
                elif opcion == 3:
                    envio = 3000
                    tipo_envio = "Otra comuna"
                    break
                else:
                    print("Opción no válida. Por favor seleccione 1, 2 o 3.")
            except ValueError:
                print("Error: Por favor ingrese un número válido (1-3).")
    
    # Calcular total sin IVA
    total_sin_iva = subtotal + envio
    
    # Calcular IVA (19%)
    iva = int(total_sin_iva * 0.19)
    
    # Calcular total final
    total_final = total_sin_iva + iva
    
    # Mostrar resumen
    print("\n" + "="*50)
    print("                 RESUMEN DE COMPRA")
    print("="*50)
    print(f"Empresa: Medicarp")
    print(f"Cantidad de mascarillas: {cantidad}")
    print(f"Precio unitario: ${500}")
    print(f"Subtotal: ${subtotal}")
    print(f"Envío ({tipo_envio}): ${envio}")
    print("-" * 50)
    print(f"TOTAL SIN IVA: ${total_sin_iva}")
    print(f"IVA (19%): ${iva}")
    print("="*50)
    print(f"TOTAL FINAL: ${total_final}")
    print("="*50)
    
    input("\nPresione Enter para continuar...")

def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-2): "))
            
            if opcion == 1:
                calcular_compra()
            elif opcion == 2:
                print("\n¡Gracias por visitar Medicarp! ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor seleccione 1 o 2.")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido (1 o 2).")

# Ejecutar el programa
if __name__ == "__main__":
    main()