def resumen_lista(lista_numeros):
    """
    Calcula estadísticas básicas de una lista de números sin usar max(), min() ni sum().

    Args:
        lista_numeros (list): Lista de números
    Returns:
        dict: mayor, menor, promedio, cantidad
    """
    if not isinstance(lista_numeros, list):
        raise ValueError("La entrada debe ser una lista.")
    if not lista_numeros:
        return {"mayor": None, "menor": None, "promedio": 0, "cantidad": 0}

    mayor = lista_numeros[0]
    menor = lista_numeros[0]
    suma = 0

    for numero in lista_numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        suma += numero

    return {
        "mayor": mayor,
        "menor": menor,
        "promedio": round(suma / len(lista_numeros), 2),
        "cantidad": len(lista_numeros),
    }


lista_numeros = [1.0, 2.5, 3.0, 4.5, 5.0]

try:
    resultado = resumen_lista(lista_numeros)
    for clave, valor in resultado.items():
        print(f"{clave.capitalize()}: {valor}")
except ValueError as e:
    print(e)
