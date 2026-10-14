def contar_caracter(cadena, caracter):

    if not isinstance(caracter, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto")

    contador = 0
    for char in cadena:
        if char == caracter:
            contador += 1
    return contador


def contar_caracter2(cadena, caracter):
    if not isinstance(caracter, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto")

    return sum(1 for char in cadena if char == caracter)


def contar_caracter3(cadena, caracter):
    if not isinstance(caracter, str):
        raise TypeError("El argumento debe ser una cadena de texto")

    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto")

    return cadena.count(caracter)
