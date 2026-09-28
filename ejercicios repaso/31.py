class Configuracion:
    def __init__(self, **kwargs):
        self.config = kwargs

    def actualizar(self, **kwargs):
        self.config.update(kwargs)

    def obtener(self, *args, default=None):
        resultado_busqueda = {}
        for busqueda in args:
            resultado_busqueda[busqueda] = self.config.get(busqueda, default)
        return resultado_busqueda

    def eliminar(self, *args):
        for busqueda in args:
            if busqueda in self.config:
                del self.config[busqueda]
        print(f"Se ha eliminado la(s) clave(s): {', '.join(args)}")

    def __str__(self):
        return f"Configuración: {self.config}"
