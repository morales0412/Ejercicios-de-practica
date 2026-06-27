def top_salarios(empleados, n):
    """
    Devuelve una lista con los 3 empleados con los salarios más altos.
    """
    if not isinstance(empleados, list):
        raise ValueError("El parametro empleados debe ser una lista")

    if not isinstance(n, int):
        raise ValueError("El parametro n debe ser un entero")

    salarios_ordenados = sorted(
        empleados, key=lambda empleado: empleado["salario"], reverse=True
    )
    top_n_salarios = salarios_ordenados[:n]

    formatedo = list(
        map(
            lambda empleado: f"{empleado['nombre']} - {empleado['salario']}",
            top_n_salarios,
        )
    )
    return formatedo


empleados = [
    {"nombre": "Ana", "salario": 2500000, "departamento": "ventas"},
    {"nombre": "Luis", "salario": 3200000, "departamento": "tecnologia"},
    {"nombre": "Maria", "salario": 1800000, "departamento": "ventas"},
    {"nombre": "Pedro", "salario": 4000000, "departamento": "tecnologia"},
    {"nombre": "Sofia", "salario": 2200000, "departamento": "marketing"},
]


print(top_salarios(empleados, 5))
