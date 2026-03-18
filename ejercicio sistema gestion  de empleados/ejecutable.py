from empleadoFullTime import EmpleadoFullTime
from empleadoFreeLance import EmpleadoFreeLance
from empresa import Empresa

def menu():
    mi_empresa = Empresa()
    
    while True:
        print("\n--- MENU DE GESTION DE EMPRESA ---")
        print("1. Registrar Empleado Full Time")
        print("2. Registrar Empleado Freelance")
        print("3. Ejecutar Nomina (Pagar a todos)")
        print("4. Buscar Empleado por ID")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opcion: ")

        try:
            if opcion == "1":
                id_e = int(input("ID: "))
                nom = input("Nombre: ")
                cor = input("Correo: ")
                sal = float(input("Salario Mensual: "))
                
                nuevo = EmpleadoFullTime(id_e, nom, cor, sal)
                mi_empresa.agregar_empleado(nuevo)

            elif opcion == "2":
                id_e = int(input("ID: "))
                nom = input("Nombre: ")
                cor = input("Correo: ")
                tar = float(input("Tarifa por hora: "))
                hrs = int(input("Horas trabajadas: "))
                
                nuevo = EmpleadoFreeLance(id_e, nom, cor, tar, hrs)
                mi_empresa.agregar_empleado(nuevo)

            elif opcion == "3":
                print("\n--- Procesando Pagos ---")
                mi_empresa.ejecutar_pago()

            elif opcion == "4":
                id_b = int(input("Ingrese el ID a buscar: "))
                emp = mi_empresa.buscar_empleado(id_b)
                if emp:
                    print(f"Resultado: {emp}")
                    print(f"Historial: {emp.obtener_historial_pagos()}")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            
            else:
                print("Opcion no valida.")

        except ValueError as e:
            print(f"\nERROR DE DATOS: {e}. Intente de nuevo.")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}")

if __name__ == "__main__":
    menu()