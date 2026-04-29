from excepciones.excepcion_suscripcion import (
    FondosInsuficienteError,
    NivelAccesoInvalido,
    UsuarioNoActivoError,
)
from gestion.sistema_cobro import SistemaCobro
from planes.plan_anual import PlanAnual
from planes.plan_mensual import PlanMensual
from usuario.usuario import Usuario


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un numero valido.")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa una opcion valida.")


def pedir_email_valido(mensaje):
    while True:
        email = input(mensaje).strip()
        if Usuario.validar_email(email):
            return email
        print("Ingresa un email valido.")


def pedir_nivel_valido(mensaje):
    niveles_validos = {"basico", "premium", "familiar"}

    while True:
        nivel = input(mensaje).strip()
        if nivel.lower() in niveles_validos:
            return nivel

        print(f"Error: El nivel de acceso {nivel} no es valido.")


def pedir_opcion_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print("Ingresa s o n.")


def mostrar_usuarios(sistema):
    if not sistema.usuarios_registrados:
        print("No hay usuarios registrados.")
        return

    print("\nUsuarios registrados:")
    for indice, registro in enumerate(sistema.usuarios_registrados, start=1):
        usuario = registro["usuario"]
        estado = "Activo" if registro["activo"] else "Inactivo"
        print(f"{indice}. {usuario} | Estado: {estado}")


def registrar_usuario_interactivo(sistema):
    nombre = input("Nombre: ").strip()
    email = pedir_email_valido("Email: ")
    nivel = pedir_nivel_valido("Nivel (basico/premium/familiar): ")
    saldo = pedir_float("Saldo inicial: ")
    activo = pedir_opcion_si_no("¿Activo? (s/n): ")

    usuario = Usuario(nombre, email, nivel, saldo)
    sistema.registrar_usuario(usuario, activo=activo)
    print("Usuario registrado correctamente.")


def cobrar_con_plan_mensual(sistema):
    precio_base = pedir_float("Precio base del plan mensual: ")
    plan = PlanMensual(precio_base)
    sistema.ejecutar_cobro_masivo(plan)


def cobrar_con_plan_anual(sistema):
    precio_base = pedir_float("Precio base mensual del plan anual: ")
    descuento = pedir_float("Descuento (0 a 1): ")
    plan = PlanAnual(precio_base, descuento)
    sistema.ejecutar_cobro_masivo(plan)


def seleccionar_plan_para_cobro(sistema):
    while True:
        print("\nSelecciona el plan a cobrar:")
        print("1. Plan mensual")
        print("2. Plan anual")

        opcion = pedir_entero("Elige una opcion: ")

        if opcion == 1:
            cobrar_con_plan_mensual(sistema)
            return
        if opcion == 2:
            cobrar_con_plan_anual(sistema)
            return

        print("Ese plan no existe. Intenta de nuevo.")


def ejecutar_menu():
    sistema = SistemaCobro()

    while True:
        print("\n=== Sistema de Gestion de Suscripciones ===")
        print("1. Registrar usuario")
        print("2. Ver usuarios registrados")
        print("3. Cobrar plan")
        print("4. Salir")

        opcion = pedir_entero("Elige una opcion: ")

        try:
            if opcion == 1:
                registrar_usuario_interactivo(sistema)
            elif opcion == 2:
                mostrar_usuarios(sistema)
            elif opcion == 3:
                seleccionar_plan_para_cobro(sistema)
            elif opcion == 4:
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")
        except (
            FondosInsuficienteError,
            UsuarioNoActivoError,
            NivelAccesoInvalido,
        ) as error:
            print(f"Error controlado: {error}")


if __name__ == "__main__":
    ejecutar_menu()
