from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo

figuras = []

while True:
    try:
        cantidad = int(input("Cantidad de figuras: "))
        if cantidad <= 0:
            print("Ingrese un numero positivo.")
            continue
        break
    except ValueError:
        print("Ingrese un numero valido.")

for i in range(cantidad):
    while True:
        tipo = input("Tipo de figura (circulo, rectangulo, triangulo): ").strip().lower()
        if tipo not in ["circulo", "rectangulo", "triangulo"]:
            print("Ingrese una figura valida.")
            continue
        break
    if tipo == "circulo":
        while True:
            try:
                radio = float(input("Radio del circulo:"))
                if radio <= 0:
                    print("Ingrese un numero positivo.")
                    continue
                figura = Circulo(radio)
                figuras.append(figura)
                break
            except ValueError:
                print("Ingrese un numero valido.")
    elif tipo == "rectangulo":
        while True:
            try:
                base = float(input("Base del rectangulo: "))
                altura = float(input("Altura del rectangulo: "))
                if base <= 0 or altura <= 0:
                    print("Ingrese numeros positivos.")
                    continue
                figura = Rectangulo(base,altura)
                figuras.append(figura)
                break
            except ValueError:
                print("Ingrese numeros validos.")
    elif tipo == "triangulo":
        while True:
            try:
                base = float(input("Base: "))
                altura = float(input("Altura:"))
                lado1 = float(input("Lado 1 del triangulo:"))
                lado2 = float(input("Lado 2 del triangulo: "))
                lado3 = float(input("Lado 3 del triangulo: "))
                if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                    print("Ingrese numeros positivos para los lados.")
                    continue
                figura = Triangulo(base,altura,lado1,lado2,lado3)
                figuras.append(figura)
                break
            except ValueError:
                print("Ingrese numeros validos para los lados.")
print("\nFiguras Geometricas Ingresadas:")
for figura in figuras:
    print(figura) 
    print("area:",figura.area())
    print("perimetro:",figura.perimetro())
    print("-" * 40)
    