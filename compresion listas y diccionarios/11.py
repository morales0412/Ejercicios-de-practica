ciudades = ["Bogotá", "Madrid", "México"]
temperaturas = [15, 20, 25]
clima = {ciudad: temp for ciudad,temp in zip(ciudades,temperaturas)}
print(clima)