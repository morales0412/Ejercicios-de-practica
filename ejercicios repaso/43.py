def son_anagramas(cadena1, cadena2):
    if not isinstance(cadena1, str) or not isinstance(cadena2, str):
        raise TypeError("Los argumentos deben ser cadenas de texto")

    if len(cadena1) != len(cadena2):
        return False
    dic_cadena1 = {}
    dic_cadena2 = {}
    for char in cadena1:
        dic_cadena1[char] = dic_cadena1.get(char, 0) + 1
    for char in cadena2:
        dic_cadena2[char] = dic_cadena2.get(char, 0) + 1
    return dic_cadena1 == dic_cadena2


def son_anagramas2(cadena1, cadena2):
    if not isinstance(cadena1, str) or not isinstance(cadena2, str):
        raise TypeError("Los argumentos deben ser cadenas de texto")

    return sorted(cadena1) == sorted(cadena2)
