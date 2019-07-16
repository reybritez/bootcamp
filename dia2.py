#Tipo de Dato - Striing/cadena/str de texto.
#"Este es un string"
#Tipo de dato Integer/Entero/int
#105
#Listas
#[] #Lista vacía
#["Steven", 22, "Programador"] #Lista de 3 elementos
#Variables
#nombre = "Steven"
#edad = 22+2-2
#variable_lista = ["Hola", nombre, 99]

#Acceder a un elemento de la lista
#print(variable_lista[0], edad, variable_lista[2])

#Acciones/operaciones sobre listas.
#variable_lista.append("Adentro lo que queres agregar") #Agregar al final de la lista.
#variable_lista.pop() #Eliminar ultimo elemento.
#variable_lista[2] = 50 

#Bucles / Loops / Ciclos
#for loquesea in variable_lista:
#   print("loquesea)´

#NUEVA CLASE ---------- FUNCIONES ##

#def nombre_de_la_funcion(argumenos):
    #lineas de codiigo
#    return

#Crear una funcioni de saludo que salude cada vez que se le llama a la funcion
# pueda motrar un saludo.

#def saludo(quien):
#    print("Hola", quien, "!")

#saludo("Marce")
#saludo("Steven")
#saludo("Stevenciito")

#def suma(num1, num2):
#    resultado = num1 + num2
#    print("Holiwis:", resultado)

#suma(1,5)

# Crear una función resta, que reciba como parámetro dos numeros
# y retorne la resta de esos numeros
# luego llamar a la funcion e iimprimir el resultado

#def resta(n1, n2):
#    operacion = n1 - n2
#    print(operacion)

#resta(10,4)

#def resta2(n3, n4):
#    restita = n3 - n4
#    return restita

#print(resta2(20,10))

# Crear una funcion Saludio2 que reciba como parametro nombre y edad
# e imprima "Hola soy xx y tengo xxx años"
# llamar varias veces a la funcion con distintos valores
# retornar algo es opcional.

#def saludo2(nombre, edad):
#    print("Hola, mi nombre es:",nombre, "y tengo:",edad, "años")

#saludo2("Steven", 22)
#saludo2("Tuhermana", 33)

#def variable3(m3,m4): #hallar multiplicacion
#    return m3*m4

#print("El resultado de la multipicacion es:", variable3(7,4))

#def porcentaje(valor): #hallar el porcentaje de un numero
#    porc = int(valor * 0.3)
#    print("El 30porciento de",valor,"es",porc)

#porcentaje(300)

# ejercicio 3. Crear una función suma_lista que reciba como argumento una lista de numeros
# y retorne la suma de todos los elementos de la lista.

#listita = [1,2,3,4,5]
#listota= [100,5,5]

#def suma_listita(lista):
#    acu=0
#    for x in lista:
#       acu= acu + x
#       print(x)
#    print(acu)

#suma_listita(listita)

#def suma_listota(lista2):
#    acu=0
#    for x in lista2:
#       acu= acu + x
#    print(acu)
    
#suma_listota(listota)

#def suma2(inf):
#    acumulador=0
#    for hola in inf:
#        acumulador=acumulador+hola
#    print(acumulador)

#suma2(sumacita)

#Ejercicio2: Lista al cuadrado.
#Crear una funcion que reciba una lista de numeros como parametros y retorne una lista con los numeros 
#al cuadrado.
#lista_cuadrado(listita) -- [1,4,9,16,25]

#CREAR UNA NUEVA LISTA Y GUARDAR LOS RESULTADOS DEL CUADRADO DE UNA LISTA

cuadradok= [1,2,3,4]

def lista_al_cuadrado(nuevalista):
    a= []
    for temp2 in nuevalista:
       a.append(temp2*temp2)
    return a

resultado_final = lista_al_cuadrado(cuadradok)
print(resultado_final)


##ELIMINAR TO DO DE UNA LISTA

#grupo5 = [1,2,3,4,5,6]

#for j in grupo5:
#    print("Hola:", j)
#for p in range(len(grupo5)):
#    grupo5.pop()
#grupo5.append("P")
#print(grupo5)

# Crear una funcion suma_cuadrado que reciba una lista de numeros
# y retorne el valor de la suma de cada numero al cuadrado. 
# [1,2,3] -- 1+4+9 : 14


listita=[1,2,3,4,5,6,7]

def lista_al_cuadrado(nuevalista):
    cuadrados= []
    for temp2 in nuevalista:
       cuadrados.append(temp2*temp2)
    return cuadrados

resultado_final = lista_al_cuadrado(listita)
print(resultado_final)

def sumadecuadrados(resultado_final):
    sumatoria= 0
    for temporal in resultado_final:
        sumatoria = sumatoria + temporal
    return sumatoria
sumatotal= sumadecuadrados(resultado_final)
print(sumatotal)
