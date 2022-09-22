from functools import reduce


class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        zona._zoologico = self
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return reduce(lambda acumulador, zona: acumulador+zona.cantidadAnimales(), self._zonas)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def setZona(self,zona):
        self._zonas = zona
    
    def getZona(self):
        return self._zonas
