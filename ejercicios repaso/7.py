def aplanar_lista(lista):
    """Recibe una lista de listas y devuelve una lista con todos los elementos de las sublistas aplanadas. usar recursividad"""
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado += aplanar_lista(elemento)
        else:
            resultado.append(elemento)
    return resultado


print(aplanar_lista([1, [2, 3], [4, [5, 6]], 7]))
