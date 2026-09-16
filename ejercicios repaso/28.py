peliculas = [
    {
        "id": 1,
        "titulo": "Inception",
        "director": "Nolan",
        "genero": "ciencia ficcion",
        "calificacion": 4.8,
        "año": 2010,
        "duracion": 148,
    },
    {
        "id": 2,
        "titulo": "The Dark Knight",
        "director": "Nolan",
        "genero": "accion",
        "calificacion": 4.9,
        "año": 2008,
        "duracion": 152,
    },
    {
        "id": 3,
        "titulo": "Parasite",
        "director": "Bong",
        "genero": "drama",
        "calificacion": 4.6,
        "año": 2019,
        "duracion": 132,
    },
    {
        "id": 4,
        "titulo": "Interstellar",
        "director": "Nolan",
        "genero": "ciencia ficcion",
        "calificacion": 4.7,
        "año": 2014,
        "duracion": 169,
    },
    {
        "id": 5,
        "titulo": "Joker",
        "director": "Phillips",
        "genero": "drama",
        "calificacion": 4.2,
        "año": 2019,
        "duracion": 122,
    },
    {
        "id": 6,
        "titulo": "Avengers",
        "director": "Russo",
        "genero": "accion",
        "calificacion": 4.3,
        "año": 2019,
        "duracion": 181,
    },
]


def top_por_genero(peliculas, genero, n):
    peliculas_filtradas = [
        pelicula for pelicula in peliculas if pelicula["genero"] == genero
    ]
    peliculas_ordenadas = sorted(
        peliculas_filtradas, key=lambda x: x["calificacion"], reverse=True
    )
    peliculas_limpias = [
        {"titulo": pelicula["titulo"], "calificacion": pelicula["calificacion"]}
        for pelicula in peliculas_ordenadas
    ]
    return peliculas_limpias[:n]


def director_mas_peliculas(peliculas):
    directores = {}
    for pelicula in peliculas:
        directores[pelicula["director"]] = directores.get(pelicula["director"], 0) + 1
    return max(directores, key=directores.get)


def promedio_por_ano(peliculas):
    años = {}
    for pelicula in peliculas:
        año = pelicula["año"]
        if año not in años:
            años[año] = []
        años[año].append(pelicula["calificacion"])
    promedios = {
        año: sum(calificaciones) / len(calificaciones)
        for año, calificaciones in años.items()
    }
    return promedios


def peliculas_largas(peliculas, mins):
    peliculas_filtradas = [
        pelicula for pelicula in peliculas if pelicula["duracion"] > mins
    ]
    peliculas_ordenadas = sorted(
        peliculas_filtradas, key=lambda x: x["duracion"], reverse=True
    )
    return peliculas_ordenadas


print(
    "Top películas de ciencia ficción:", top_por_genero(peliculas, "ciencia ficcion", 2)
)
print("Director con más películas:", director_mas_peliculas(peliculas))
print("Promedio de calificaciones por año:", promedio_por_ano(peliculas))
print("Películas con duración mayor a 150 minutos:", peliculas_largas(peliculas, 150))
