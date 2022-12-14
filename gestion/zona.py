from gestion.zoologico import Zoologico


class Zona:

    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._animales = []
        self._zoo = zoo

    def agregarAnimales(self, animal):
        animal._zona = self
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
