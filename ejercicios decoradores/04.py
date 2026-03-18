#medir tiempo
import time
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion de {func.__name__}: {fin - inicio} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calculo_largo():
    for _ in range(100000):
        pass
calculo_largo()