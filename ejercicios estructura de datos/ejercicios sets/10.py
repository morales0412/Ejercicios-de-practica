clase_A = {"Ana", "Beto", "Carlos", "Diana"}
clase_B = {"Beto", "Diana", "Esteban", "Fabiola"}
clase_C = {"Carlos", "Diana", "Guillermo"}

estudiantes_b_y_c = clase_B.intersection(clase_C)
print(estudiantes_b_y_c)

estudiantes_comun = (clase_A.intersection(clase_B)) | (clase_A.intersection(clase_C)) | (clase_B.intersection(clase_C))
print(estudiantes_comun)