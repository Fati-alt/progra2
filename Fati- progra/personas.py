#Clase padre
class Humano:
    def __init__(self,nombre,edad,genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero

    def caract(self):
        print(f"Hola mi nombre es {self.nombre} tengo {self.edad} y soy {self.genero}")

    def saludo(self):
        print("Hola soy humano")

class Programador(Humano):
    def saludo2(self):
        print("Hola soy un programador")

class Ingeniero(Humano):
    def __init__(self, nombre, edad, genero,telefono):
        super().__init__(nombre, edad, genero) #atributo extra
        self.telefono=telefono
    def saludo(self):
        print("Hola soy ingeniero")
    def caract(self):
        print(f"Hola mi nombre es {self.nombre} tengo {self.edad} y soy {self.genero} y mi numero es {self.telefono}")
