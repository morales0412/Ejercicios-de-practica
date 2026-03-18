def log_inicio_fin(func):
    def wrapper(*args,**kwargs):
        print(f"iniciando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Finalizando {func.__name__}")
        return resultado
    return wrapper

@log_inicio_fin
def multiplicar (*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    print(resultado)

multiplicar(2,3,4)