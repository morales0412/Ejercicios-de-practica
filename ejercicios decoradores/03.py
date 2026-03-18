#validar enteros

def validar_enteros(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"El argumento {arg} no es un entero.")
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"El argumento {key} = {value} no es un entero.")
        return func(*args, **kwargs)
    return wrapper

@validar_enteros
def sumar(a,b):
    return a + b

print(sumar(1,2))