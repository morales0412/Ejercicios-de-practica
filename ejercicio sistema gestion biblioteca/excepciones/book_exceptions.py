from .base import LibraryError


class BookError(LibraryError):
    pass


class BookNotAvailableError(BookError):
    def __init__(self, codigo: str):
        self.codigo = codigo
        super().__init__(
            f"El libro con codigo {self.codigo} no se encuentra disponible"
        )


class BookAlreadyLoanedError(BookError):
    def __init__(self, codigo: str):
        self.codigo = codigo
        super().__init__(f"El libro con codigo {self.codigo} ya se encuentra prestado")


class InvalidBookStateError(BookError):
    def __init__(self, codigo: str, estado: str):
        self.codigo = codigo
        self.estado = estado
        super().__init__(
            f"El estado {self.estado} no es valido para el libro con codigo {self.codigo}"
        )


class DuplicateBookError(BookError):
    def __init__(self, codigo: str):
        self.codigo = codigo
        super().__init__(f"El libro con codigo {self.codigo} ya existe")


class BookNotFoundError(BookError):
    def __init__(self, codigo: str):
        self.codigo = codigo
        super().__init__(f"El libro con codigo {self.codigo} no se encuentra")
