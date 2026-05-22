def clasificar_numero(lista_numeros):
    clasificacion = {"positivos": [], "negativos": [], "ceros": []}

    for numero in lista_numeros:
        if numero > 0:
            clasificacion["positivos"].append(numero)
        elif numero < 0:
            clasificacion["negativos"].append(numero)
        else:
            clasificacion["ceros"].append(numero)

    return clasificacion


resultado = clasificar_numero([1, -2, 3, 0, -5, 6])

for categoria, numeros in resultado.items():
    print(f"{categoria.capitalize()}: {numeros}")
