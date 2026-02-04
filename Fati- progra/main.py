from personas import *

humano1=Humano("Maria", 17, "Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero)
humano1.caract()
humano1.saludo() #los metodos terminan con parentesis

programador1=Programador("Juan",21,"Masculino")
print(programador1.nombre)
print(programador1.edad)
print(programador1.genero)
programador1.caract()
programador1.saludo() 
programador1.saludo2() 

inge1=Ingeniero("Mario", 22,"Masculino", 222678)
print(inge1.nombre)
print(inge1.edad)
print(inge1.genero)
print(inge1.telefono)
inge1.caract()
inge1.saludo()