# convertir texto a mayusculas

def mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args,**kwargs)
        return resultado.upper()
    return wrapper

@mayusculas
def saludo(nombre):
    return f"Hola, {nombre}"

print(saludo("Juan"))