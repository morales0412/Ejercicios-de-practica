def dos_sumas(lista, objetivo):
    """
    Dada una lista de numeros y un objetivos, devuelva una lista con los indices de los numeros que al sumarlos den el objetivo.
    """
    indices = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                indices.append((i, j))
    return indices.append("ninguno") if not indices else indices


print(dos_sumas([2, 7, 11, 15], 9))  # Output: [0, 1]
