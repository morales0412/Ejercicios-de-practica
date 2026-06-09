def factorial(n):
    """
    Calcula el factorial de un numero pasado
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El numero debe ser un entero no negativo.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
