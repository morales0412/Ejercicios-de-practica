# rotar una matriz cuadrada 90 grados en sentido horario


def rotar_matriz(matriz):
    n = len(matriz)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matriz[i][j]
            matriz[i][j] = matriz[n - j - 1][i]
            matriz[n - j - 1][i] = matriz[n - i - 1][n - j - 1]
            matriz[n - i - 1][n - j - 1] = matriz[j][n - i - 1]
            matriz[j][n - i - 1] = temp
    return matriz


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotar_matriz(matriz))
