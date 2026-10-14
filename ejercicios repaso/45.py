def sumar_elementos(lista):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")

    total = 0
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos de la lista deben ser un numero")
        total += elemento
    return total


def sumar_elementos2(lista):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")

    return sum(lista)
