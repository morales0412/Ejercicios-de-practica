def pipeline(valor, *args):
    x = valor
    for funcion in args:
        x = funcion(x)
    return x


print(
    pipeline(
        5,
        lambda x: x * 2,  # 5 * 2 = 10
        lambda x: x + 3,  # 10 + 3 = 13
        lambda x: x**2,  # 13 ** 2 = 169
    )
)
