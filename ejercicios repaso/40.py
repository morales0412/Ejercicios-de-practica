def comprimir_string(cadena):
    """Funcion que recibe una cadena de texto y devuelve una nueva cadena donde aparece el caracter seguido de la cantidad de apariciones"""
    if not cadena:
        raise ValueError("La cadena no puede estar vacia.")

    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto.")

    resultado = ""
    apariciones = {}

    for char in cadena:
        apariciones[char] = apariciones.get(char, 0) + 1

    for char, aparicion in apariciones.items():
        if aparicion == 1:
            resultado += char
        else:
            resultado += f"{char}{aparicion}"
    return resultado


print(comprimir_string("abcd"))
print(comprimir_string("aaabbbcc"))
