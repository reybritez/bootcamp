#print(2+2)
#print("Hola World! ") #Aca digo hola Mundo xd
#print("Que queres prro?") #Esto es para keonda
#print("2" * 2)
#print("Nabo " * 10) #Acá Digo Nabo 10 veces
#print("Que pasa si digo +" + " H  o l a? ") #Acá estaba al  dope nomas
################
#VARIABLES
#a = (2*2) #Primera Variable
#b = (a+8) #Suma de la primera + otro valor
#print(a+b) #Print xd
#print ("Hola, el valor de A es:", a, "Y de B:",b)
#########
#EJERCICIO 1 - Crear una variable nombre y una variable edad con sus nombres y edades e imprimir "Hola, me llamo x y Tengo x Años"
#nombre = "Steven Rey"
#edad = 22
#print("Hola, me llamo",nombre,"y tengo",edad,"años")

#Ejercicio 1.1 - Crear una variable hobby con tu pasatiempo e imprimir. 
#pasatiempo = "joder las bolas"
#print("Hola, me llamo",nombre,"y tengo",edad,"años, y mi pasatiempo es",pasatiempo)

#LISTAS
#lista_vacia = []
#listax = [1,2,3,5]
#print(lista_vacia)
#print(listax)
#lista_datos = ["Steven"]
#print(lista_datos)
#print(listax[3])
#alumnos = ["Joseciito", "Mulan", lista_datos, "Marce"]
#nro_alumno = 2
#print(alumnos[nro_alumno]) #Lista con variables 
#columna1 = 10
#columna2 = 7
#holi = [columna1,columna2]
#numero = ((2+3*holi[1])*6)
#Ejercicio 2 - Crear una lista datos en el que en el primer lugar esté tu nombre y en la segunda posición esté tu edad
#datos = ["Steven", 22, "tu hermana"]
#print("Hola, me llamo",datos[0],"y tengo",datos[1],"años. Y tengo",datos[3],"por ciento de batería")

## CAJA DE CAJAS = LISTAS.
#datos[1] = 20 #cambio la variiable de datos en la posición 1. 
#print(datos[1])
#print(datos)
#datos.append("Kiondawe")
#print(datos)
#datos.insert(4, "Jahechami")
#print(datos)
#datos = ["Steven", 22]

#Ejericicio 2.1 - Agregar una profesión y un hobby a la lista de datos previamente creada. 
#datos.append("de todo un poco")
#datos.append("joder las bolas")
#print(datos)
#print("Hola mi nombre es",datos[0],", tengo",datos[1],",soy",datos[2],"y me gusta",datos[3])
#datos.pop()
#print(datos)

#Funcion len() = lenght
#print(datos)
#dimension = len(datos)
#print(dimension)

#Ejercio 3 - Obtener la dimensiión de la lista datos e imprimir: "La lista Datos tiene x Elementos"
#print(datos)
#dimension = len(datos)
#print("La lista Datos tiene:",dimension,"elementos")

#Ejercicio 3.1 - Imprimir el ultimo elemento de una lista que no sabemos 
# cuantos elementos tiene
#datos1 = [1,3,5,7,7,8,9,10,2,5,7,9,0,7,677,63,23,423,1,21,31,5,13,631,3,423,2,2231,229,30]
#ult= (len(datos1)-1)
#print("El ultimo elemento de la lista es:", datos1[ult])
#datos1.append(918)
#ult= (len(datos1)-1)
#print("El ultimo elemento de la lista es:", datos1[ult])

#Imprimir el elemento del medio de una lista que no sabemos cuantos elementos tiene:
#med = int(len(datos1)/2)
#print("El numero del medio es:", datos1[med])

#Imprimir la recta en 3 partes iguales y encontrar los puntos de corte.
#partir = int(len(datos1)/3)
#print(partir)
#punto1 = datos1[0-1]
#punto2 = datos1[punto1+partir-1]
#punto3 = datos1[punto1+punto2-1]
#punto4 = datos1[punto3+punto2-1]
#print("Los puntos de corte son:",datos1[punto1],datos1[punto2],datos1[punto3],datos1[punto4])

############# BUCLES O CICLOS O ITERACIONES ##########

#lista_temas = ["variables", "listas", "tipos de datos"]

#for concepto in lista_temas:
 #   print("Hoy aprendí", concepto)

 #   print("Que gusto!")
#print("Esto es lo que aprendí hoy")

#for variable_for in lista_o_rango:
    #bloque que se repite
#bloque que no se repite

#Ejercicio 4- Recorrer una lista e imprimir en cada ciclo el valor del elemento 
# Con 3 signos de admiración.

#lista_larga = ["variables", "listas", "tipos de datos", "bucles"]
#lista_corta = ["Que onda", "Que hay"]

#for concepto in lista_larga:
#    print("Hoy aprendí",concepto,"!!!")
#    for pepito in lista_corta:
#            print("Holi",pepito)
#print("FIN!!!")

#for laverdad in range(100):
#    print("Hola", laverdad)

#Ejercicio 5 - Imprimir los numeros del 1 al 100 usando for y a range.

#for loquevimos in range(1,101):
#    print ("Algo Numero",loquevimos)
#print("FIN!!!")

#Ejerciicio 5.1 - Impriimir el resultado de la suma de los numeros del 1 al 10
sumatoria= 0
for varia in range(1,11):
    sumatoria = sumatoria + varia
print("La sumatoria total es de:",sumatoria)