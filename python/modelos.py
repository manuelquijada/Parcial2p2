class ServicioTransporte:
    def __init__(self, conductor, identificador, distancia, tarifa_base):
        self.conductor = conductor
        self.identificador = identificador
        self.distancia = distancia
        self.tarifa_base = tarifa_base

    def calcular_tarifa(self):
        return self.tarifa_base

    def mostrar_resumen(self):
        print("Conductor:", self.conductor)
        print("Tipo de transporte:", self.__class__.__name__)
        print("Distancia:", self.distancia, "km")
        print("Tarifa: $", round(self.calcular_tarifa(), 2))
        print("----------------------------")


class Motocicleta(ServicioTransporte):
    def calcular_tarifa(self):
        return self.tarifa_base + self.distancia * 0.35


class Automovil(ServicioTransporte):
    def calcular_tarifa(self):
        return self.tarifa_base + self.distancia * 0.60
