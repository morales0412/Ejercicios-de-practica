def segundo_mayor(lista):
    """Funcion que recibe una lista de numeros y devuelve el segundo numero mayor de la lista."""
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista.")
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos elementos.")

    mayor = 0
    segundo_mayor = 0

    for numero in lista:
        if numero > mayor:
            segundo_mayor = mayor
            mayor = numero
        elif numero < mayor and numero > segundo_mayor:
            segundo_mayor = numero
    return segundo_mayor


print(segundo_mayor([1, 5, 3, 9, 2]))
