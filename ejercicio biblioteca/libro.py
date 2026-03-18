class Libro: 
    def __init__ (self,titulo,año_publicacion,autor):
        self.titulo = titulo 
        self.año_publicacion = año_publicacion
        self.autor = autor
        self.disponible = True
    
    def prestar_libro(self):
        if self.disponible: 
            self.disponible = False
    
    def devolver_libro (self):
        self.disponible = True
    
    def __str__ (self):
        return f"Libro(titulo = {self.titulo}, año_publicacion = {self.año_publicacion}, autor = {self.autor}, disponible = {self.disponible})"