from persona import Persona

class SocioBiblioteca(Persona):
    def __init__ (self,nombre,id):
        super().__init__(nombre,id)
        self.libros_prestados = []
    
    def pedir_libro (self,libro):
        if not libro.disponible:
            print(f"El libro '{libro.titulo}' no esta disponible.")
            return
        if libro not in self.libros_prestados:
            libro.prestar_libro()
            self.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {self.nombre}.")
            return
        print(f"El libro '{libro.titulo}' ya lo tienes prestado.")
        
    def devolver_libro (self,libro):
        
        if libro in self.libros_prestados: 
            libro.devolver_libro()
            self.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo}' devuelto por {self.nombre}.")
            return
        print(f"El libro '{libro.titulo}' no fue prestado a {self.nombre}.")
    
    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros prestados.")
            return
        print(f"Libros prestados a {self.nombre}:")
        for libro in self.libros_prestados:
            print(f"- {libro.titulo}")
    