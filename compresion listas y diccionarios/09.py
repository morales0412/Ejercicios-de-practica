edades = {"Juan": 15, "Maria": 25, "Luis": 12, "Ana": 30}
adultos = {nombre: edad for nombre,edad in edades.items() if edad >= 18}
print(adultos)