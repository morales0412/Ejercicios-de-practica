def sumar_lista(lista):
    """
    Recibe una lista de numeros y devuelve la suma de todos los elementos usando recursividad
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista")
    if len(lista) == 0:
        return 0
    return lista[0] + sumar_lista(lista[1:])


lista = [1, 2, 3, 4, 5]

print(sumar_lista(lista))
