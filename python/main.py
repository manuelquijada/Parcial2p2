from modelos import Motocicleta, Automovil

servicios = [
    Motocicleta("Carlos", "M001", 10, 2.00),
    Automovil("Ana", "A001", 10, 3.00),
    Motocicleta("Luis", "M002", 15, 2.00),
    Automovil("Marta", "A002", 15, 3.00)
]

for servicio in servicios:
    servicio.mostrar_resumen()
