from functools import reduce


def agrupar_y_ordenar(empleados):
    """
    Agrupa empleados por departamento y ordena cada grupo por salario descendente.

    Args:
        empleados (list): Lista de diccionarios con nombre, salario y departamento
    Returns:
        dict: Diccionario agrupado por departamento, ordenado por salario
    """
    if not isinstance(empleados, list):
        raise ValueError("El parametro empleados debe ser una lista.")

    agrupados = reduce(
        lambda acc, emp: {
            **acc,
            emp["departamento"]: acc.get(emp["departamento"], []) + [emp],
        },
        empleados,
        {},
    )

    return {
        departamento: sorted(lista, key=lambda e: e["salario"], reverse=True)
        for departamento, lista in agrupados.items()
    }


empleados = [
    {"nombre": "Ana", "salario": 2500000, "departamento": "ventas"},
    {"nombre": "Luis", "salario": 3200000, "departamento": "tecnologia"},
    {"nombre": "Maria", "salario": 1800000, "departamento": "ventas"},
    {"nombre": "Pedro", "salario": 4000000, "departamento": "tecnologia"},
    {"nombre": "Sofia", "salario": 2200000, "departamento": "marketing"},
]
