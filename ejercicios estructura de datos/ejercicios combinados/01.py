ordenes = [
    (101, "Laptop", 1, 1200),
    (102, "Mouse", 3, 25),
    (101, "Monitor", 2, 300),
    (103, "Teclado", 1, 75),
    (102, "Webcam", 1, 50)
]
resumen_ordenes = {}

for orden in ordenes:
    if orden[0] not in resumen_ordenes:
        resumen_ordenes[orden[0]] = orden[2] * orden[3]
    else:
        resumen_ordenes[orden[0]] += orden[2] * orden[3]

print(resumen_ordenes)