def es_palindromo(cadena):
    """
    Funcion que verifica si un texto es un palindromo , se lee igual de izquierda a derecha, se usara recursividad
    """
    if not isinstance(cadena, str):
        raise ValueError("El argumento debe ser una cadena de texto")
    if len(cadena) <= 1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])


texto = "anitalavalatina"
print(es_palindromo(texto))
