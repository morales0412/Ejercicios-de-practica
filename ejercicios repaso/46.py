def maximo(numeros):
    if not isinstance(numeros, list):
        raise TypeError("El argumento debe ser una lista")
    if not numeros:
        return None
    num_maximo = numeros[0]
    for num in numeros[1:]:
        if not isinstance(num, (int, float)):
            raise TypeError("Todos los elementos de la lista deben ser un numero")
        if num > num_maximo:
            num_maximo = num
    return num_maximo


def maximo2(numeros):
    if not isinstance(numeros, list):
        raise TypeError("El argumento debe ser una lista")
    if not numeros:
        return None
    return max(numeros)


print(maximo([3, 5, 2, 8, 1]))  # Salida: 8
