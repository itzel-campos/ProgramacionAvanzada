import datetime
#Crear una clase
class Mascota:
    def __init__ (self, Codigo, Raza, Nombre, Direccion, UIValido=False):
        #pylint: disable=unused-argument
        self.Codigo= Codigo
        self.Raza= Raza
        self.Nombre= Nombre
        self.Direccion= Direccion
        self.UIValido= UIValido
        
class Mascotas(Mascota):
    Registro=datetime.datetime.now()