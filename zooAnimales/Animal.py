class Animal:
    
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    def movimiento():
        return ""

    def totalPorTipo():
        return "Mamiferos: #\nAves: \nReptiles: #\nPeces: #\nAnfibios: #"

    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._nombre}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zoo.getNombre()}"

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero
