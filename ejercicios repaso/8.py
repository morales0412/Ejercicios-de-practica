def potencia(base, exponente):
    if not isinstance(base, (int, float)) or not isinstance(exponente, int):
        raise ValueError("La base debe ser un numero y el exponente un entero.")

    if exponente < 0:
        return 1 / potencia(base, -exponente)
    elif exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


print(potencia(2, 3))


def contar_ocurrencias(lista, elemento):
    resultado = 0
    if not isinstance(lista, list):
        raise ValueError("El primer argumento debe ser una lista.")
    if len(lista) == 0:
        return 0
    if lista[0] == elemento:
        resultado += 1
    return resultado + contar_ocurrencias(lista[1:], elemento)
