intereses_ana = {"fotografia", "viajes", "ciclismo", "programacion"}
intereses_luis = {"programacion", "musica", "viajes", "ajedrez"}
intereses_marta = {"ciclismo", "cocina", "viajes", "lectura"}

interseccion = intereses_ana.intersection(intereses_luis)
print(interseccion)

interseccion_global = intereses_ana.intersection(intereses_luis,intereses_marta)
print(interseccion_global)