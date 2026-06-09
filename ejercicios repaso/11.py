def buscar_elemento(lista, valor, indice=0):
    """
    Busca un elemento en una lista y retorna su índice usando recursión.

    Args:
        lista (list): Lista de elementos
        valor: Elemento a buscar
        indice (int): Índice actual, por defecto 0
    Returns:
        int: Índice del elemento si existe, -1 si no
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if not lista:
        return -1
    if lista[0] == valor:
        return indice

    resultado = buscar_elemento(lista[1:], valor, indice + 1)
    return resultado


print(buscar_elemento([10, 20, 30, 40], 30))  # 2
print(buscar_elemento([10, 20, 30, 40], 99))  # -1
print(buscar_elemento(["a", "b", "c"], "b"))  # 1
