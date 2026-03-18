class LibraryError(Exception):
    def __init__(self,mensaje: str):
        self.mensaje = mensaje
        super().__init__(self.mensaje)