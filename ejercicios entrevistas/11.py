def fibonnaci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El arguemento debe ser un numero entero no negativo")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonnaci(n - 1) + fibonnaci(n - 2)
