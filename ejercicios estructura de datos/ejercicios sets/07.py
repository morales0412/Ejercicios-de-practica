esperado = {"A", "B", "C", "D", "E"}
encontrado = {"B", "C", "E", "F", "G"}

faltantes = esperado.difference(encontrado)
print(faltantes)
excedentes = encontrado.difference(esperado)
print(excedentes)

discrepancia_total = encontrado.symmetric_difference(esperado)
print(discrepancia_total)