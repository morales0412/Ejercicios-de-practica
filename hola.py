nombres = {"Alice": 25, "Bob": 30, "Charlie": 35}
nombres["Alice"] = 26  # Actualiza el valor de "Alice" a 26

print(nombres.get("Alice"))

print(nombres.get("David", 0))
