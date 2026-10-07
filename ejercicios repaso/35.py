def numero_a_romano(numero):
    """
    Convierte un número entero a su representación en números romanos.

    Args:
        numero (int): Número entero positivo
    Returns:
        str: Representación en números romanos
    """
    if not isinstance(numero, int):
        raise ValueError("El número debe ser un entero.")
    if numero <= 0 or numero > 3999:
        raise ValueError("El número debe estar entre 1 y 3999.")

    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = ""

    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado


print(numero_a_romano(3))  # III
print(numero_a_romano(9))  # IX
print(numero_a_romano(58))  # LVIII
print(numero_a_romano(1994))  # MCMXCIV
