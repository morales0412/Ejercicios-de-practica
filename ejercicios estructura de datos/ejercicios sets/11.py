codigos_sucios = ["aBC-10", "abc-10", "DCE-22", "dce-22", "AbC-10", "xyz-55"]

formateado = set(valor.lower() for valor in codigos_sucios)
print(formateado)

print(len(formateado))