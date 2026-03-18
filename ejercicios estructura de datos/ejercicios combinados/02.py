usuarios = {
    "alice": {"edad": 30, "ciudad": "NY", "skills": ["Python", "SQL", "Cloud"]},
    "bob": {"edad": 24, "ciudad": "LA", "skills": ["Java", "API", "Testing"]},
    "charlie": {"edad": 35, "ciudad": "SF", "skills": ["Python", "ML", "Pandas"]}
}

habilidades_unicas = set()

for usuario in usuarios.values():
    habilidades_unicas.update(usuario["skills"])

print(list(habilidades_unicas))