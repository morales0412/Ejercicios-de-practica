def primer_unico(texto):
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    contador_caracter = {}
    for char in texto:
        contador_caracter[char] = contador_caracter.get(char, 0) + 1
    for char, cantidad in contador_caracter.items():
        if cantidad == 1:
            return char
    return None
