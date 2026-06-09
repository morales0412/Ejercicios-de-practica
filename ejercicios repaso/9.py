def maximo(numeros):
    if not isinstance(numeros, list):
        raise ValueError("El argumento debe ser una lista")

    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia")

    if len(numeros) == 1:
        return numeros[0]

    max_restante = maximo(numeros[1:])

    return numeros[0] if numeros[0] > max_restante else max_restante


numeros = [3, 1, 4, 1, 5, 9]
print(maximo(numeros))


def minimo(numeros):
    if not isinstance(numeros, list):
        raise ValueError("El argumento debe ser una lista")

    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia")

    if len(numeros) == 1:
        return numeros[0]

    min_restante = minimo(numeros[1:])
    return numeros[0] if numeros[0] < min_restante else min_restante
