from excepciones.excepcion_suscripcion import (
    FondosInsuficienteError,
    UsuarioNoActivoError,
)


class SistemaCobro:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar_usuario(self, usuario_obj, activo=True, **detalles_extra):
        nuevo_registro = {
            "usuario": usuario_obj,
            "activo": activo,
            "info_adicional": detalles_extra,
        }
        self.usuarios_registrados.append(nuevo_registro)

    def ejecutar_cobro_masivo(self, plan_objeto):
        costo_plan = plan_objeto.obtener_costo()

        for registro in self.usuarios_registrados:
            user = registro["usuario"]

            try:
                if not registro["activo"]:
                    raise UsuarioNoActivoError(user._nombre)

                if user._saldo < costo_plan:
                    raise FondosInsuficienteError(user._saldo, costo_plan)

                user._saldo -= costo_plan
                print(f"Cobro exitoso: {user._nombre} | Saldo: ${user._saldo:.2f}")

            except UsuarioNoActivoError as e:
                print(f"Error: {e}")
            except FondosInsuficienteError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {user._nombre} - {e}")
