empleados = [
    ("Elena", "Ventas", 55000),
    ("David", "IT", 70000),
    ("Carlos", "Ventas", 48000),
    ("Ana", "IT", 62000),
    ("Beto", "Marketing", 50000)
]

salarios_altos = {}

for empleado in empleados:
    if empleado[2] >= 60000:
        salarios_altos[empleado[0]] = empleado[2]

print(salarios_altos)