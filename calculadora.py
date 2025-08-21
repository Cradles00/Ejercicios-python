# Pedir al usuario un número positivo
numero = int(input("Ingrese un número positivo: "))

# Verificar que sea positivo
if numero > 0:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # del 1 al 10
        print(f"{numero} x {i} = {numero * i}")
else:
    print("El número no es positivo. Intente de nuevo.")

