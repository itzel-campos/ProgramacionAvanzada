import json 
from Clasepia import Mascota
from operator import attrgetter
datos=[]
print("Ingrese los datos para el registro de la mascota")
while True:
    codigo = input("Ingresa el codigo de registro ")
    raza = input("¿Que raza es la mascota? ")
    nombre = input("Nombre completo del dueño: ")
    direccion = input("Ingresa la direccion ")
    verificacion= input("¿Haz terminado el registro? (1 es para salir/ 0 para permanecer) ")
    registro = Mascota(codigo, raza, nombre, direccion)
    datos = datos + [registro]
    if verificacion == "1":
        break
    
def MostrarRegistro(x):
    print(x.Codigo)
    print(x.Raza)
    print(x.Nombre)
    print(x.Direccion)
    

for registro in datos:
    MostrarRegistro(registro)
    
datos.sort(key=attrgetter("Codigo"),reverse=False)
def OrdendeRegistro(x):
    print(x.Codigo)
    print(x.Raza)
    print(x.Nombre)
    print(x.Direccion)
   
    
for registro in datos:
    OrdendeRegistro(registro)

        
print("Mascotas")
json_data = json.dumps(datos, default=lambda o: o.__dict__, indent=4)
print(json_data)
    
    
    