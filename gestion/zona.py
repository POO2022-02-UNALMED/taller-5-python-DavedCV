from typing_extensions import Self
from gestion.Zoologico import Zoloogico


class Zona:

    def __init__(self, nombre):
        self._nombre = nombre
        self._animales = []

    def agregarAnimales(self, animal):
        animal._zona = self
        self._animales.append(animal)

    @classmethod
    def cantidadAnimales(cls):
        return len(cls.animales)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales