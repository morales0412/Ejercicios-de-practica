class Curso: 
    def __init__ (self,nombre,codigo,creditos,cupo_maximo):
        self.nombre = nombre 
        self.codigo = codigo 
        self.creditos = creditos
        self.cupo_maximo = cupo_maximo
        self.profesor = None
        self.estudiantes = []
    
    def asignar_profesor(self,profesor):
        if self.profesor is None:
            self.profesor = profesor
        else:
            print(f"El curso {self.nombre} ya tiene un profesor asignado.")
    
    def matricular_estudiante(self,estudiante):

        if len(self.estudiantes) < self.cupo_maximo:
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} matriculado en el curso {self.nombre}.")
        else:
            print(f"No se puede matricular al estudiante {estudiante.nombre} en el curso {self.nombre}. Cupo máximo alcanzado.")
    
    def desmatricular_estudiante(self,estudiante):
        if not self.estudiantes:
            print(f"No hay estudiantes matriculados en el curso {self.nombre}.")

        elif estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante.nombre} desmatriculado del curso {self.nombre}.")
        else:
            print(f"El estudiante {estudiante.nombre} no está matriculado en el curso {self.nombre}.")
    
    def obtener_numero_estudiantes(self):
        print(f"Curso {self.nombre} = {len(self.estudiantes)} estudiantes matriculados.")
    
    def mostrar_informacion(self):
        print(f"Curso: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Créditos: {self.creditos}")
        print(f"Cupo máximo: {self.cupo_maximo}")
        if self.profesor:
            print(f"Profesor: {self.profesor.nombre}")
        else:
            print("No hay profesor asignado.")
        print(f"Estudiantes matriculados: {[estudiante.nombre for estudiante in self.estudiantes]}")