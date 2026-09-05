ventas = [
    {"vendedor": "Ana", "monto": 5000000},
    {"vendedor": "Luis", "monto": 3000000},
    {"vendedor": "Ana", "monto": 7000000},
]

promedio = sum(venta["monto"] for venta in ventas) / len(ventas)


usuarios_mayores_promedio = list(
    filter(lambda venta: venta["monto"] > promedio, ventas)
)
print(usuarios_mayores_promedio)


nombres = [("Andres", 25), ("Maria", 30), ("Juan", 20)]
edad_promedio = sum(edad[1] for edad in nombres) / len(nombres)

print(f"Edad promedio: {edad_promedio}")

mayores = list(filter(lambda persona: persona[1] > edad_promedio, nombres))
print(f"Personas mayores que la edad promedio: {mayores}")
