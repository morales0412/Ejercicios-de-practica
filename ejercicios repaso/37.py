def contar_vocales_consonantes(string):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    contador_vocales = 0
    contador_consonantes = 0

    for char in string:
        if char in vocales:
            contador_vocales += 1
        elif char in consonantes:
            contador_consonantes += 1

    diccionario = {"vocales": contador_vocales, "consonantes": contador_consonantes}
    return diccionario


print(contar_vocales_consonantes("Hola mundo"))

print(contar_vocales_consonantes("Python 3.0!"))
