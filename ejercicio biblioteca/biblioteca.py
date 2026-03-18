class Biblioteca:
    
    def __init__(self):
        self.libros = []
        self.socios = []
    
    def agregar_libro(self, libro):

        if libro not in self.libros:
            self.libros.append(libro)
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
            return
        else:
            print(f"El libro '{libro.titulo}' ya está en la biblioteca.")
    
    def registrar_socio(self, socio):

        if socio not in self.socios:
            self.socios.append(socio)
            print(f"socio '{socio.nombre}' registrado en la biblioteca.")
            return
        else:
            print(f"El socio '{socio.nombre}' ya está registrado en la biblioteca.")
    
    def prestar_libro (self,socio, libro):
        if socio in self.socios and libro in self.libros:
            socio.pedir_libro(libro)
        else:
            print(" El socio o el libro no estan registrados en la biblioteca.")
    
    def devolver_libro(self, socio, libro):
        if socio in self.socios and libro in self.libros:
            socio.devolver_libro(libro)
        else:
            print(" El socio o el libro no estan registrados en la biblioteca.")
    
    def buscar_libro (self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
    
    def buscar_socio (self, id):
        for socio in self.socios:
            if socio.id == id:
                return socio
        print(f"El socio con ID '{id}' no se encuentra en la biblioteca.")
    
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        print("Libros disponibles en la biblioteca:")

        for i,libro in enumerate(self.libros,start = 1):
            print(f"{i}. {libro.titulo} - {'Disponible' if libro.disponible else 'No disponible'}\n")