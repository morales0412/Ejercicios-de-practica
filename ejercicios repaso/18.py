from math import pi

while True:
    print("\n--- Menú de opciones cálculo de área y perímetro ---")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Cuadrado")
    print("4. Círculo")
    print("5. Salir")

    # Validar opción
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion < 1 or opcion > 5:
                print("Ingrese una opción dentro del rango (1-5)")
            else:
                break

        except ValueError:
            print("Por favor, ingrese un número válido")

    # TRIÁNGULO
    if opcion == 1:
        while True:
            try:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                lado_1 = float(input("Ingrese el lado 1 del triángulo: "))
                lado_2 = float(input("Ingrese el lado 2 del triángulo: "))
                lado_3 = float(input("Ingrese el lado 3 del triángulo: "))

                if base <= 0 or altura <= 0:
                    print("La base y la altura deben ser mayores que 0")
                    continue

                if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
                    print("Los lados deben ser mayores que 0")
                    continue

                # Comprobar que los lados formen un triángulo
                if (
                    lado_1 + lado_2 <= lado_3
                    or lado_1 + lado_3 <= lado_2
                    or lado_2 + lado_3 <= lado_1
                ):
                    print("Los lados ingresados no forman un triángulo")
                    continue

                break

            except ValueError:
                print("Por favor, ingrese medidas válidas")

        area = (base * altura) / 2
        perimetro = lado_1 + lado_2 + lado_3

        print(f"El área del triángulo es: {area}")
        print(f"El perímetro del triángulo es: {perimetro}")

    # RECTÁNGULO
    elif opcion == 2:
        while True:
            try:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))

                if base <= 0 or altura <= 0:
                    print("Las medidas deben ser mayores que 0")
                else:
                    break

            except ValueError:
                print("Por favor, ingrese medidas válidas")

        area = base * altura
        perimetro = 2 * (base + altura)

        print(f"El área del rectángulo es: {area}")
        print(f"El perímetro del rectángulo es: {perimetro}")

    # CUADRADO
    elif opcion == 3:
        while True:
            try:
                lado = float(input("Ingrese el lado del cuadrado: "))

                if lado <= 0:
                    print("La medida debe ser mayor que 0")
                else:
                    break

            except ValueError:
                print("Por favor, ingrese una medida válida")

        area = lado**2
        perimetro = 4 * lado

        print(f"El área del cuadrado es: {area}")
        print(f"El perímetro del cuadrado es: {perimetro}")

    # CÍRCULO
    elif opcion == 4:
        while True:
            try:
                radio = float(input("Ingrese el radio del círculo: "))

                if radio <= 0:
                    print("El radio debe ser mayor que 0")
                else:
                    break

            except ValueError:
                print("Por favor, ingrese una medida válida")

        area = pi * radio**2
        perimetro = 2 * pi * radio

        print(f"El área del círculo es: {area}")
        print(f"El perímetro del círculo es: {perimetro}")

    # SALIR
    elif opcion == 5:
        print("Saliendo del programa...")
        break
