#poder alamcenar datos en una lista
#se importan las clases hechas
from definirclase import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter
# Función para mostrar los elementos que tiene la lisa de ejemplo.
def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.telefono==telabuscar):
            coincidencia=True
            break
    return coincidencia

# Se declara una lista que almacenará objetos. Inicia sin elementos.
# Muestra los elementos de la lista.
Contactos = []
CuantosElementosHay()

# Se agregan varios objetos a la lista.
Contactos.append(Contacto(1234567890,"Felipe Ramirez","feli.rmz@hotmail.com"))
CuantosElementosHay()

# Barrido secuencial.
for contacto in Contactos:#se muestran los datos uno por uno 
    print("------------------------------------------")
    print(contacto.telefono)
    print(contacto.nombre)
    print(contacto.correo)

# Ordenamiento.
Contactos.sort(key=attrgetter("telefono"),reverse=False)

print("Ordenado")
# Barrido secuencial.
for contacto in Contactos:#Se muestran los datos de la clave
    print("------------------------------------------")
    print(contacto.telefono)
    print(contacto.nombre)