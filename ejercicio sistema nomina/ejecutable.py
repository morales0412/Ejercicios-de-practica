from empresa import Empresa
from empleado_fijo import EmpleadoFijo
from empleado_comision import EmpleadoComision

empresa = Empresa()

def main():
    while True:
        print("\nMenu")
        print("1. Agregar empleado")
        print("2. Mostrar nomina")
        print("3. Suma nomina")
        print("4. Buscar empleado")
        print("5. Eliminar empleado")
        print("6. Salir")

        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion < 1 or opcion > 6:
                    print("Opcion no valida")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un numero valido")
        if opcion == 1:
            nombre = input("Ingrese el nombre del empleado: ")
            id = input("Ingrese el id del empleado:")
            while True:
                try:
                    tipo = int(input("Ingrese el tipo de empleado (1. Fijo, 2. Comision): "))
                    if tipo < 1 or tipo > 2:
                        print("Opcion no valida")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un numero valido")
            if tipo == 1:
                while True:
                    try:
                        sueldo_mensual = float(input("Ingrese el sueldo mensual: "))
                        if sueldo_mensual < 0:
                            print("Por favor ingrese un numero positivo")
                            continue
                        break
                    except ValueError:
                        print("Por favor ingrese un numero valido")
                empleado = EmpleadoFijo(nombre,id,sueldo_mensual)
                empresa.agregar_empleado(empleado)
                print("El empleado ha sido agregado")