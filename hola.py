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
palabras = " ".join(texto["contenido"] for texto in textos).lower().split()
print(palabras)

print(textos.get)
