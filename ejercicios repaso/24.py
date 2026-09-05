from functools import reduce

ventas = [
    {"vendedor": "Ana", "mes": "enero", "monto": 5000000, "region": "norte"},
    {"vendedor": "Luis", "mes": "enero", "monto": 3000000, "region": "sur"},
    {"vendedor": "Ana", "mes": "febrero", "monto": 7000000, "region": "norte"},
    {"vendedor": "Maria", "mes": "enero", "monto": 4000000, "region": "norte"},
    {"vendedor": "Luis", "mes": "febrero", "monto": 6000000, "region": "sur"},
    {"vendedor": "Maria", "mes": "febrero", "monto": 2000000, "region": "norte"},
]


def total_ventas_por_vendedor(ventas):
    ventas_por_vendedor = {}
    for venta in ventas:
        vendedor = venta["vendedor"]
        ventas_por_vendedor[vendedor] = (
            ventas_por_vendedor.get(vendedor, 0) + venta["monto"]
        )
    return ventas_por_vendedor


def top_vendedores(ventas, cantidad_max=1):
    promedio_ventas = sum(venta["monto"] for venta in ventas) / len(ventas)
    mayores_promedio = list(
        filter(lambda venta: venta["monto"] > promedio_ventas, ventas)
    )

    ordenados = sorted(mayores_promedio, key=lambda venta: venta["monto"], reverse=True)

    return ordenados[:cantidad_max]


def ventas_por_region(ventas):
    ventas_por_region = {}
    for venta in ventas:
        region = venta["region"]
        ventas_por_region[region] = ventas_por_region.get(region, 0) + venta["monto"]
    return ventas_por_region


print("Total de ventas por vendedor:")
print(total_ventas_por_vendedor(ventas))

print("Total de ventas por región:")
print(ventas_por_region(ventas))

top_vendedores_list = top_vendedores(ventas, cantidad_max=5)
print("Top vendedores con ventas mayores al promedio:")
for vendedor in top_vendedores_list:
    print(
        f"Vendedor: {vendedor['vendedor']}, Monto: {vendedor['monto']}, Mes: {vendedor['mes']}, Región: {vendedor['region']}"
    )
