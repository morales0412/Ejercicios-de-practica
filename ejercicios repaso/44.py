def comprimir(texto):
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    if not texto:
        return ""
    resultado = ""
    contador = 1
    for indice in range(len(texto) - 1):
        if texto[indice] == texto[indice + 1]:
            contador += 1
        else:
            resultado += texto[indice] + str(contador)
            contador = 1
    resultado += texto[-1] + str(contador)
    return resultado


print(comprimir("aaabbbccaa"))
