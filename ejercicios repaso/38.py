def lista_a_numero(lista):
    """Funcion que recibe una lista de numeros y devuelve un numero formado por la concatenacion de todos los elementos de la lista, si hay un 0 a la izquierda se ignora."""

    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista.")

    if not lista:
        raise ValueError("La lista no puede estar vacia.")

    numero = ""

    for elemento in lista:
        numero += str(elemento)
    return int(numero)


print(lista_a_numero([1, 24, 56, 23]))
