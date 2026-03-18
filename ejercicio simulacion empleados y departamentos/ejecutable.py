from gerente import Gerente
from desarrollador import Desarrollador

personal_empresa = []
cantidad = int(input("Ingrese la cantidad de empleados a registrar: "))
for i in range(cantidad):
    print(f"\nRegistro del empleado {i+1}:")
    nombre = input("Nombre: ")
    departamento = input("Departamento:")
    while True:
        try:
            salario = float(input("Salario mensual: "))
            break
        except ValueError:
            print("Salario invalido.")
    tipo = input("Tipo de empleado (G = gerente, D = desarrollador): ").strip().upper()

    nuevo_empleado = None
    if tipo == 'G':
        while True:
            try:
                bonus = float(input("equipo a cargo (numero empleados):"))
                break
            except ValueError:
                print("Bonus invalido.")
        nuevo_empleado = Gerente(nombre,departamento,salario,bonus)
    elif tipo == 'D':
        lenguaje = input("Lenguaje de programacion principal: ")
        nuevo_empleado =  Desarrollador(nombre,departamento,salario,lenguaje)
    else:
        print("Tipo de empleado invalido. Se omitira este registro.")
        continue
    personal_empresa.append(nuevo_empleado)

print(f"\n\nResumen de empleados registrados ({len(personal_empresa)}):")

for empleado in personal_empresa:
    print(empleado)
