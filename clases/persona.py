#Clase: Una receta para crear un objeto. 
#Para la programacion Orientada a Objetos.
#En este caso habra que definir la Clase de Objeto y luego veremos k pedo

# class Persona: # Creamos la clase Persona, como una "Plantilla"
#     edad = 0 #Atributo de la clase o propiedad del objeto que vamos a crear
#     def __init__(self, un_nombre): #__init__ es el metodo contstructor
#                                     #metodo --> funciones dentro de una clase
#         self.mi_nombre = un_nombre
#         print("Hola, naci, me llamo: ", self.mi_nombre) #usamos self para referirnos al objeto mismo
    
#     def cumple(self): #cumple es un metodo de la clase persona que aumenta 
#         self.edad = self.edad + 1 # la propiedad edad en 1.

#     def altura(self, la_altura): 
#         self.mi_altura = la_altura
#         print("Hi, que onda we. Mi nombre es:",self.mi_nombre, "y mido: ",self.mi_altura)
#         if self.mi_altura > 170 and self.mi_altura<190:
#             print("todo bien kpe")
#         elif self.mi_altura > 150 and self.mi_altura<169:
#             print("Casi entraste en el rango")
#         elif self.mi_altura >= 190 and self.mi_altura<200:
#             print("jue sos re alto")

# pepe = Persona("Pepito") #Pepe un Objeto de la Clase Persona
# pepa = Persona("Pepita") #Pepa una Objeta de la Clase Persona

# pepe.cumple()
# print(pepe.edad)
# pepe.altura(191)

## Ej. Agregar un metodo a la clase Persona que asigne una nacionalidad y
# otro metodo saludar que imprima "Hola Soy ____ y mi nacionalidad es ____" 
# Anhadi a este method el INDICE DE MASA CORPORAL XD
class Saludar:
    nationality= "Paraguaya"
    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("Holi, soy:",self.mi_nombre,"Y soy de nacionalidad:",self.nationality)
#    def crecimiento(self, una_altura):
#        self.altura = una_altura + self.mi_altura
#        print("Creci",una_altura,"cm, y mi altura nueva es:",self.altura)
    def calculo_imc(self, un_peso, una_altura):
        self.peso = un_peso
        self.altura = una_altura
        imc = (self.peso) / ((self.altura)*(self.altura)) 
        print(imc)
        if imc < 18.5: 
            print("Tu peso es insuficiente")
        elif imc >= 18.5 and imc <= 24.5:
            print("Tu peso es Normal")
        elif imc > 24.5 and imc < 50:
            print("tas gordito bro")

        
pepe = Saludar("Pepe")
pepe.calculo_imc(70,1.70)
marta = Saludar("Marta")
marta.calculo_imc(80,1.60)
maiki = Saludar("Maiki")
maiki.calculo_imc(70,1.80)

#pepe.crecimiento(30)
#marta.crecimiento(10)
#maiki.crecimiento(30)

