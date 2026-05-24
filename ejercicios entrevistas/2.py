def es_palindromo(palabra):
    """
    Esta funcion recibe una palabra y devuelve True si es un palindromo (se lee igual de izquierda a derecha que de derecha a izquierda) y False en caso contrario. No se deben considerar los espacios ni las mayúsculas.
    """
    if not isinstance(palabra, str):
        raise ValueError("La entrada debe ser una cadena de texto.")
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]


try:
    resultado = es_palindromo("Anita lava la tina")
    print(f"¿Es palíndromo? {resultado}")
except ValueError as e:
    print(e)
