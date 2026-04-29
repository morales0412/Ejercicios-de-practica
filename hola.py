class nose:
    def __init__(self, estado):
        self.estado = estado

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado.capitalize() not in ["Activo", "Inactivo"]:
            raise ValueError(f"El estado {nuevo_estado} no es valido.")
        self._estado = nuevo_estado


hola = nose("activo")
hola.estado = "nose"
