def analizar_texto(texto):
    """
    Analiza un texto y devuelve un diccionario con las siguientes estadisticas:
    -cantidad de palabras
    -cantidad de caracteres (sin espacios)
    -cantidad de vocales
    -palabra mas larga
    """
    if not isinstance(texto, str):
        raise ValueError("La entrada debe ser una cadena de texto.")
    estadisticas = {
        "palabras": len(texto.split()),
        "caracteres": sum(len(palabra) for palabra in texto.split()),
        "vocales": 0,
        "palabra_mas_larga": "",
    }
    vocales = "aeiou"
    for palabra in texto.split():
        if len(palabra) > len(estadisticas["palabra_mas_larga"]):
            estadisticas["palabra_mas_larga"] = palabra
        for letra in palabra:
            if letra.lower() in vocales:
                estadisticas["vocales"] += 1
    return estadisticas


try:
    texto = "Hola, este es un texto de ejemplo para analizar."
    resultado = analizar_texto(texto)
    for clave, valor in resultado.items():
        print(f"{clave.capitalize()}: {valor}")
except ValueError as e:
    print(e)
