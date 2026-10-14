def capitalizar_palabras(cadena):

    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto.")

    palabras = cadena.lower().split()
    resultado = []

    for palabra in palabras:
        palabra = palabra[0].upper() + palabra[1:]
        resultado.append(palabra)

    return " ".join(resultado)


print(capitalizar_palabras("hola mundo"))
print(capitalizar_palabras("pYTHON es GENIAL"))
print(capitalizar_palabras("a"))
print(capitalizar_palabras(""))
print(capitalizar_palabras("hola   mundo"))
print(capitalizar_palabras("  hola mundo  "))
