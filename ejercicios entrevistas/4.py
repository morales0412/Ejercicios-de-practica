def contar_palabras(frase):
    """
    Cuenta la cantidad de veces que cada palabra aparece en una frase."""
    if not isinstance(frase, str):
        raise ValueError("La entrada debe ser una cadena de texto.")
    palabras = frase.split()
    conteo = {palabra: palabras.count(palabra) for palabra in set(palabras)}
    return conteo


def contar_palabras_2(frase):

    if not isinstance(frase, str):
        raise ValueError("La entrada debe ser una cadena de texto.")
    palabras = frase.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


try:
    resultado = contar_palabras("hola mundo hola")
    print(resultado)
    resultado2 = contar_palabras_2("hola mundo hola")
    print(resultado2)
except ValueError as e:
    print(e)
