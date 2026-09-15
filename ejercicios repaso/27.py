textos = [
    {
        "id": 1,
        "autor": "Ana",
        "contenido": "Python es un lenguaje increible y poderoso",
        "categoria": "tecnologia",
    },
    {
        "id": 2,
        "autor": "Luis",
        "contenido": "El cafe es la mejor bebida del mundo mundial",
        "categoria": "cultura",
    },
    {
        "id": 3,
        "autor": "Ana",
        "contenido": "Django es el mejor framework de Python",
        "categoria": "tecnologia",
    },
    {
        "id": 4,
        "autor": "Maria",
        "contenido": "La musica clasica relaja el alma y el cuerpo",
        "categoria": "cultura",
    },
    {
        "id": 5,
        "autor": "Luis",
        "contenido": "FastAPI es moderno y rapido para APIs",
        "categoria": "tecnologia",
    },
]


def palabras_mas_frecuentes(textos, n):
    palabras = " ".join(texto["contenido"] for texto in textos).lower().split()
    resultado = {}

    for palabra in palabras:
        if len(palabra) < 4:
            continue
        resultado[palabra] = resultado.get(palabra, 0) + 1

    resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1], reverse=True)

    return resultado_ordenado[:n]


def autor_mas_prolijo(textos):
    autores = {}
    for texto in textos:
        autor = texto["autor"]
        autores[autor] = autores.get(autor, 0) + len(texto["contenido"].split())
    return max(autores, key=autores.get)


def textos_por_categoria(textos):
    categorias = {}
    for texto in textos:
        categoria = texto["categoria"]
        if categoria not in categorias:
            categorias[categoria] = 0
        tamano = len(texto["contenido"].split())
        categorias[categoria] += tamano
    return categorias


print("Palabras más frecuentes:", palabras_mas_frecuentes(textos, 3))
print("Autor más prolijo:", autor_mas_prolijo(textos))
print("Textos por categoría:", textos_por_categoria(textos))
