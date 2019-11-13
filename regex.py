#para poder importar la clase hecha
# Librería para gestionar la entrada de los datos de la clase Contacto
import re
#para poder importar la clase hecha
from  nombredearchivo import nombredeclase

#Para poder validar las expresiones regulares
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt) #poder encontrar las similitud en los argumentos
    return bool(coincidencia)

# Expresiones regulares para cada campo.
telefonoRegEx="^[0-9]{10}$" #La coincidencia que tiene que encontrar en lo que introduzca el usuario
nombreRegEx="^[A-Z]+(([',. -][A-Z ])?[A-Z]*)*$"
entidadValida=True

# Pregunta de teléfono.
_telefono=""
telefono=0
datoValido=False
while True:
    _telefono=input("Teléfono:")
    if RegEx(_telefono,telefonoRegEx):
        telefono=int(_telefono)
        datoValido=True
        break
    else:
        print("Se requieren 10 dígitos como número")
        datoValido=False
    entidadValida=(entidadValida & datoValido)
