a = (1, 2, 3)
b = (4, 5)

c = a + b
print(c)

try:
    c.append(6)
except AttributeError:
    print("Los objetos tupla no son mutables")