calificaciones = {
    "matematicas": [4, 5, 3, 2],
    "historia": [2, 3, 4],
    "ingles": [3, 4, 5],
    "biologia": [5, 4, 3],
    "quimica": [4, 5, 5, 4],
}
numeros = [1, 2, 3, 4, 5]

aprobadas = list(
    filter(
        lambda materia: (
            sum(calificaciones[materia]) / len(calificaciones[materia]) >= 3
        ),
        calificaciones,
    )
)
print(aprobadas)

for materia in calificaciones:
    print(materia)
