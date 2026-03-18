class Universidad:
    def __init__ (self,nombre_universidad):
        self.nombre_universidad = nombre_universidad
        self.lista_estudiantes = []
        self.lista_profesores = []
        self.lista_cursos = []
    
    def agregar_estudiante(self, estudiante):
        if estudiante not in self.lista_estudiantes:
            self.lista_estudiantes.append(estudiante)
            print(f" Estudiante {estudiante.nombre} ha sido agregado a la universidad")
        else:
            print(f" El estudiante {estudiante.nombre} ya esta registrado en la universidad")
    
    def agregar_profesor(self,profesor):
        if profesor not in self.lista_profesores:
            self.lista_profesores.append(profesor)
            print(f" Profesor {profesor.nombre} ha sido agregado a la universidad")
        else:
            print(f" El profesor {profesor.nombre} ya esta registrado en la universidad")
    
    def agregar_curso(self, curso):

        if curso not in self.lista_cursos:
            self.lista_cursos.append(curso)
            print(f" Curso {curso.nombre} ha sido agregado a la universidad")
        else:
            print(f" El curso {curso.nombre} ya esta registrado en la universidad")
    
    def asignar_profesor_a_curso(self, curso, profesor):
        if curso in self.lista_cursos and profesor in self.lista_profesores:
            curso.asignar_profesor(profesor)
            profesor.asignar_curso(curso)
            print(f"Profesor {profesor.nombre} fue asignado al curso {curso.nombre}")
        else:
            print("Curso o profesor no encontrado en la universidad.")

    def matricular_estudiante_a_curso(self, estudiante, curso):

        if estudiante in self.lista_estudiantes and curso in self.lista_cursos:
            curso.matricular_estudiante(estudiante)
            estudiante.matricular_curso(curso)
            print(f"Estudiante {estudiante.nombre} fue matriculado en el curso {curso.nombre}")
        else:
            print("Estudiante o curso no encontrado en la universidad.")

    def mostrar_cursos (self):
            if not self.lista_cursos:
                print("No hay cursos disponibles en la universidad.")
                return
            print("Cursos disponibles en la universidad:")
            for curso in self.lista_cursos:
                curso.mostrar_informacion()
            
    
    def mostrar_estudiantes (self):
        if not self.lista_estudiantes:
            print(f"No hay estudiantes inscritos en la universidad")
            return
        print(f"Estudiantes de universidad {self.nombre_universidad}")
        for estudiante in self.lista_estudiantes:
            print(f"Nombre: {estudiante.nombre} , ID universitario: {estudiante.id_universitario}, Carrera: {estudiante.carrera}")
        print(f"Total estudiantes: {len(self.lista_estudiantes)} estudiantes ")

    def mostrar_profesores (self):
        if not self.lista_profesores:
            print(f"No hay profesores inscritos en la universidad")
            return
        print(f"Profesores de la universidad {self.nombre_universidad}")
        for profesor in self.lista_profesores:
            print(f"Nombre: {profesor.nombre}, ID universitario: {profesor.id_universitario}, Especialidad: {profesor.especialidad}")
    
    def buscar_estudiante(self, id_universitario):
        for estudiante in self.lista_estudiantes:
            if estudiante.id_universitario == id_universitario:
                return estudiante
        print(f"Estudiante con ID {id_universitario} no encontrado.")
    
    def buscar_curso (self,codigo):
        for curso in self.lista_cursos:
            if curso.codigo == codigo:
                return curso
        print(f"Curso con código {codigo} no encontrado.")

    def buscar_profesor (self, id_universitario):
        for profesor in self.lista_profesores:
            if profesor.id_universitario == id_universitario:
                return profesor
        print(f"Profesor con ID {id_universitario} no encontrado")
