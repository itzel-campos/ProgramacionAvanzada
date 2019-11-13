#poder crear una clase derivada de una clase base
class Persona: 
    nombre=""
    apellidos=""
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
    def muestraInfo(self):
        print("Clase Base")
        print(self.nombre)
        print(self.apellidos)

class Estudiante(Persona):
    aniograduacion=0
    def muestraInfo(self):
        print("Clase Derivada")
        print(self.nombre)
        print(self.apellidos)
        print(self.aniograduacion)
    def derivadoInfo(self):
        print(self.aniograduacion)
