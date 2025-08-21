print("======================================")
print("      PROGRAMA: DATOS DE PERSONA      ")
print("======================================\n")

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
genero = input("Ingrese el género (varon/mujer): ").lower()
celular = input("Ingrese el número de celular: ")

print("\n--------------------------------------")
print(f"Nombre: {nombre}")

if genero == "varon":
    print(f"Edad: {edad} años")
elif genero == "mujer":
    print(f"Celular: {celular}")
else:
    print("Género no válido, debe ser 'varon' o 'mujer'.")

print("--------------------------------------")

