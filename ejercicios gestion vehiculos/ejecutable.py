from coche import Coche
from motocicleta import Motocicleta

coche1 = Coche("Toyota","Corolla",2020,20000,4)
moto1 = Motocicleta("Yamaha","YZF-R3",2021,5000,321)

tipo = input("Ingrese el tipo de vehiculo a arrancar (coche/moto):").strip().lower()

if tipo == "coche":
    print(coche1)
    print(coche1.arrancar())
else:
    print(moto1)
    print(moto1.arrancar())