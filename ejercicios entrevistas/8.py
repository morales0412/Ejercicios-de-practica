def suma_digitos(n):
    """
    Suma los digitos de un numero
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El numero debe ser un entero no negativo.")
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)


print(suma_digitos(1234))
