def comparar_listas(lista1, lista2):
    """
    Compara dos listas y devuelve un diccionario con los elementos que solo estan en la primera lista , que solo estan en la segunda lista y que estan en ambas listas.
    """
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise ValueError("Ambas entradas deben ser listas.")
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud.")
    set1 = set(lista1)
    set2 = set(lista2)
    resultado = {
        "solo_en_primera": list(set1.difference(set2)),
        "solo_en_segunda": list(set2.difference(set1)),
        "en_ambas": list(set1.intersection(set2)),
    }
    return resultado


try:
    resultado = comparar_listas([1, 2, 3], [3, 4, 5])
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
except ValueError as e:
    print(e)
