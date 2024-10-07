num= int(input("cuantas tablas: "))

for a in range(1,num + 1):
    print(f"\nTabla del {a}:")
    print(" " * 15)

    for b in range(10, 0, -1):
        resul = a * b
        print(f"{a} * {b} = {resul}")

input("\nPulse Enter para continuar...")
