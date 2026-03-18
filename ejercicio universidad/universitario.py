from persona import Persona

class Universitario(Persona):

    def __init__(self,nombre, id_universitario, carrera):
        super().__init__(nombre, id_universitario)
        self.carrera = carrera
        self.cursos_matriculados = []
    
    def matricular_curso(self, curso):
        if curso not in self.cursos_matriculados:
            self.cursos_matriculados.append(curso)
            print(f"Curso '{curso.nombre}' matriculado para {self.nombre}.")
            return
        print(f"El curso '{curso.nombre}' ya esta matriculado")

    def desmatricular_curso(self,curso):
        if curso in self.cursos_matriculados:
            self.cursos_matriculados.remove(curso)
            print(f"Curso '{curso.nombre}' desmatriculado para {self.nombre}.")
            return
        print(f"El curso '{curso.nombre}' no esta matriculado para {self.nombre}.")
    
    def mostrar_cursos_matriculados(self):

        if not self.cursos_matriculados:
            print("No hay cursos matriculados.")
            return
        print(f"Cursos matriculados por {self.nombre}:")
        
        for curso in self.cursos_matriculads:
            print(f" - {curso.nombre}")
    