def segundo_mayor(lista):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")

    if len(lista) < 2:
        return None

    mayor = lista[0]
    segundo = None

    for numero in lista[1:]:
        if not isinstance(numero, (int, float)):
            raise TypeError("Todos los elementos de la lista deben ser un numero")
        if numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero != mayor and (segundo is None or numero > segundo):
            segundo = numero
    return segundo


def segundo_mayor_metodos(lista):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")
    if len(lista) < 2:
        return None
    numeros_unicos = list(set(lista))
    resultado = sorted(numeros_unicos, reverse=True)
    return resultado[1]


print(segundo_mayor([3, 45, 66, 125, 12, 5666, 12]))
