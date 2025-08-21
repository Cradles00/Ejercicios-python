print("======================================")
print("      PROGRAMA: NÚMERO MAYOR         ")
print("======================================\n")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print("\n--------------------------------------")
print(f"Los números ingresados son: {num1}, {num2}, {num3}")
print(f"➡ El número mayor es: {mayor}")
print("--------------------------------------")
