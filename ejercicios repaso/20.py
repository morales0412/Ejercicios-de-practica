vector_1 = []
vector_2 = []
num_anterior = None

for i in range(5):
    while True:
        try:
            num = int(input(f"Ingrese el numero {i + 1} del primer vector: "))
            if num_anterior is not None and num < num_anterior:
                print(
                    f"El numero debe ser mayor que el numero anterior, numero anterior: {num_anterior}"
                )
                continue
            num_anterior = num
            vector_1.append(num)
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

num_anterior = None
for i in range(5):
    while True:
        try:
            num = int(input(f"Ingrese el numero {i + 1} del segundo vector: "))
            if num_anterior is not None and num < num_anterior:
                print(
                    f"El numero debe ser mayor que el numero anterior, numero anterior: {num_anterior}"
                )
                continue
            num_anterior = num
            vector_2.append(num)
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

vector_ordenado = sorted(vector_1 + vector_2)
print(f"El vector ordenado es: {vector_ordenado}")
