class Animales:
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas
    def sonido(self):
        print("aaah")

class Conejo(Animales):
    def sonido2(self):
        print("sniff sniff")
    def caract(self):
        print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas} patas")

class Ornito(Animales):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas)
        self.pico=pico 
    def sonido3(self):
        print("grrr grrr")
    def caract(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es color {self.color}, tiene {self.patas} patas y su pico mide{self.pico}")

class Dinosaurio(Animales):
    especie = "Tiranosaurio"
    def sonido4(self):
        print("roar roar")
    print(f"Mi dinosaurio se llama {self.nombre}, es de la especie {self.especie}, es color {self.color} y tiene {self.patas} patas")



