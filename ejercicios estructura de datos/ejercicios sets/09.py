mis_idiomas = {"Español", "Inglés", "Italiano", "Latín"}
populares = {"Inglés", "Francés", "Alemán", "Italiano", "Español"}

unicos = mis_idiomas.difference(populares)
print(unicos)

verificacion = {"Español", "Italiano"}.issubset(mis_idiomas)
print(verificacion)