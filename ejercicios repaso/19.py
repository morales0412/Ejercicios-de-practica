edades = []

for i in range(10):
    while True:
        try:
            edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
            if edad < 0 or edad > 120:
                print("La edad no puede ser negativa ni mayor a 120.")
                continue
            edades.append(edad)
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

menores_edad = sum(1 for edad in edades if edad < 18)
mayores_edad = sum(1 for edad in edades if edad >= 18 and edad < 60)
promedio = sum(edades) / len(edades)

print(f"Cantidad de personas menores de edad: {menores_edad}")
print(f"Cantidad de personas mayores de edad: {mayores_edad}")
print(f"edad mas baja: {min(edades)} años")
print(f"edad mas alta: {max(edades)} años")
print(f"Promedio de edades: {promedio:.2f} años")
