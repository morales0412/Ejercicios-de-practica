def es_primo(n):
    # Verifica si un numero es primo
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(es_primo(2))
print(es_primo(7))
print(es_primo(10))
print(es_primo(1))
