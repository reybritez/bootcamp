#Clase: Una receta para crear un objeto. 
#Para la programacion Orientada a Objetos.
#En este caso habra que definir la Clase de Objeto y luego veremos k pedo

class Persona:
    edad = 0 
    ojos = 2
    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("Hola, naci, me llamo: ", self.mi_nombre)
    
    def cumple(self):
        self.edad = self.edad + 1

    def altura(self, la_altura):
        self.mi_altura = la_altura
        print("Hi, que onda we. Mi nombre es:",self.mi_nombre, "y mido: ",self.mi_altura)
        
        
        
pepe = Persona("Pepito")
pepa = Persona("Pepita")


print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)
pepe.altura(180)