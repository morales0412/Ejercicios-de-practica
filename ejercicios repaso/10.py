def eliminar_duplicados(lista):
    """
    Elimina los elementos duplicados de una lista usando recursión.

    Args:
        lista (list): Lista con posibles elementos repetidos
    Returns:
        list: Lista sin elementos repetidos
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if not lista:
        return []

    resto = eliminar_duplicados(lista[1:])

    if lista[0] in resto:
        return resto
    else:
        return [lista[0]] + resto


print(eliminar_duplicados([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]
print(eliminar_duplicados(["a", "b", "a", "c"]))  # ["a", "b", "c"]
