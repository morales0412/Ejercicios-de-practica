class ReservaError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class sala:
    contador_id = 1

    def __init__(self, nombre, capacidad, ocupada=False):
        self.id = sala.contador_id
        self.nombre = nombre
        self.capacidad = capacidad
        self.ocupada = ocupada
        sala.contador_id += 1

    def __str__(self):
        return f"{self.id} - {self.nombre} - capacidad: {self.capacidad} - {'ocupada' if self.ocupada else 'disponible'}"


class Reserva:
    def __init__(self, usuario, id_sala, confirmada):
        self.usuario = usuario
        self.id_sala = id_sala
        self.confirmada = confirmada

    def confirmacion(self):
        self.confirmada = True
        return self

    def __str__(self):
        return f"Reserva de {self.usuario} para la sala {self.id_sala} - {'confirmada' if self.confirmada else 'pendiente'}"


nombres_salas = ["Privada A", "Meeting Room", "Open Space", "Phone Booth"]
capacidades = [4, 10, 20, 1]

salas = [
    sala(nombre, capacidad) for nombre, capacidad in zip(nombres_salas, capacidades)
]

reservas = []


validacion_ocupacional = all(disponible.ocupada for disponible in salas)
print(validacion_ocupacional)

if validacion_ocupacional:
    print("Coworking lleno")
else:
    while True:
        desear_reservar = input("¿Desea reservar una sala? (s/n): ").lower().strip()
        if desear_reservar not in ["s", "n"]:
            print("Opcion no valida. ")
            continue
        if desear_reservar == "n":
            print("Saliendo del sistema de reservas.")
            break
        usuario = input("Ingrese su nombre de usuario: ").strip()
        print("Salas disponibles: ")
        for sala in salas:
            if not sala.ocupada:
                print(f"{sala}")
        try:
            seleccion = (
                input("Ingrese el nombre de la sala que desea reservar: ")
                .strip()
                .lower()
            )
            sala_seleccionada = next(
                (sala for sala in salas if sala.nombre.lower() == seleccion), None
            )
            if sala_seleccionada is None:
                raise ReservaError("La sala seleccionada no existe.")
            if sala_seleccionada.ocupada:
                raise ReservaError("La sala seleccionada ya está ocupada.")
            sala_seleccionada.ocupada = True
            reserva = Reserva(usuario, sala_seleccionada.id, confirmada=True)
            reservas.append(reserva)

            print(f"Reserva confirmada: {reserva}")
        except ReservaError as e:
            print(f"Error en la reserva - {e.mensaje}")


while True:
    respuesta = (
        input("¿Desea pasar a confirmada todas las reservas pendientes? (s/n): ")
        .lower()
        .strip()
    )
    if respuesta not in ["s", "n"]:
        print("Opcion no valida.")
        continue
    if respuesta == "n":
        print("Saliendo del sistema de confirmacion.")
        break
    if all(reserva.confirmada for reserva in reservas):
        print("No hay reservas pendientes para confirmar.")
        break
    reservas = list(map(lambda r: r.confirmacion(), reservas))
    print("Todas las reservas pendientes han sido confirmadas.")

salas_pequeñas = list(filter(lambda s: s.capacidad < 5, salas))
print("Salas pequeñas disponibles: ")

for i, sala in enumerate(salas_pequeñas, start=1):
    print(f"{i}. {sala}")
