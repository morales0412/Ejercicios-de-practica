class MontoInvalidoError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


transacciones = [
    {"id": 1, "monto": 100.50, "moneda": "USD", "estado": "completado"},
    {
        "id": 2,
        "monto": -50.00,
        "moneda": "USD",
        "estado": "completado",
    },
    {
        "id": 3,
        "monto": 200.00,
        "moneda": "COP",
        "estado": "pendiente",
    },
    {"id": 4, "monto": 1500.00, "moneda": "COP", "estado": "completado"},
    {"id": 5, "monto": 300.00, "moneda": "USD", "estado": "completado"},
]


def procesar_pagos(lista_transacciones):
    totales_monedas = {}
    for transaccion in lista_transacciones:
        try:
            if transaccion["estado"] != "completado":
                continue

            if transaccion["monto"] <= 0:
                raise MontoInvalidoError(f"Monto inválido en ID {transaccion['id']}")

            moneda = transaccion["moneda"]
            totales_monedas[moneda] = (
                totales_monedas.get(moneda, 0) + transaccion["monto"]
            )

        except MontoInvalidoError as e:
            print(f"Saltando transacción: {e}")

    return totales_monedas


if __name__ == "__main__":
    totales = procesar_pagos(transacciones)
    print(f"Totales por moneda: {totales}")
    hola = {}
    print(hola.get("nose", 0))
    print(hola)
