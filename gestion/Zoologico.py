class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        zonas = []

    def agregarZonas(self, zona):
        zona._zoologico = self
        self.zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales():
        pass

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre