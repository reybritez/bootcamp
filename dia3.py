##REPASO GENERAL DE LOS TEMAS DEL DIA 2.-Listas etc.
# Imprimir lista de compras para el super
#ingredientes = ["harina","levadura", "sal", "azucar","agua"]
#def compra_super(ingre_pan, nombre): #Definimos los parametros que va a recibir
#    print("Lista de compras de:",nombre) #print de uno de los parametros
#    print("___________________")
#    for x in ingre_pan: #usamos otro paramentro
#        print(x)
#compra_super(ingredientes,"Pan") #mandamos parametros a la funcion

#ing_salsa = ["azucar", "sal", "cebolla", "tomatito", "oregano"] 
#compra_super(ing_salsa, "Salsa")#mandamos parametros a la funcion

#### CONDICIONALES ####
# == igual
# > mayor que
# < menor que
# >= mayor o igual
# <= menor o igual
# != distinto de 

#a = 5
#b = 1

#if a > b:
#    print("Si, es mayor a 3")
#else:
#    print("No lo es.")

#nota = 60

#if nota >= 60:
#    print("Lo lograste!!")
#else:
#    print("Hule ya :(")

#Ejercicios. Crea una funcion que reciba como parámetro una nota de 1 al 100
# e imprima si pasaste o te aplazaste.

#def notita(valor_nota):
#    if valor_nota > 60:
#        print("Bieen, pasaste")
#    else:
#        if valor_nota == 60:
#           print("Bajón, casi lo hiciste")
#        else:
#            print("noup. no pasaste")

#notita(40)
#a=12

#if a > 5 and a < 10:
#    print("A es mayor a 5 y menor que 10")
#else:
#    print("No lo es")

#edad = 5

#if edad > 2 and edad <= 5:
#    print("Deberias estar en Pre/escolar")
#else:
#    if edad >= 6 and edad < 13:
#        print("Deberias estar primaria")
#    else:
#        if edad >= 14 and edad < 18:
#            print("Deberias estar en secundaria o bachiller")
#        else: 
#            if edad >= 19:
#                print("Deberias estar en la universidad")

# SIN ANIDAR
#if edad > 18:
#    print("Uni")
#elif edad > 13:
#    print("secu")
#elif edad > 6:
#    print("Primaria")
#else:
#    print("bbdlc")

#Ejercicio 2: Crear una funcion puntaje que reciba como parametro una nota
# del 1 al 100 e imprima que nota sacaste:
# nota <60 ----> 1 
# nota entre 60 y 70 ----> 2
# nota entre 71 y 75 ----> 3
# nota entre 76 y 85 ----> 4
# nota mayor a 85 ----> 5
# nota 100 ---> 5 felicitado bro.



# def puntaje(nota):

#    if nota < 60:
#     print("Sorry bro, no pasaste: NOTA 1")
#    elif nota >= 60 and nota <= 70:
#        print("PASASTE: 2")
#    elif nota >= 71 and nota <= 75:
#        print("PASASTE: 3")
#    elif nota >= 76 and nota <= 85:
#        print("PASASTE: 4")
#    elif nota >= 86 and nota <= 99:
#        print("PASASTE: 5")
#    elif nota == 100:
#        print("5 felicitado bro")

# puntaje(100)

## INPUT ####

# nombre = input("Ingresa tu nombre: ")
# print("Hola,", nombre)

# num1 = int(input("Ingresa el primer numero a sumar: "))
# num2 = int(input("Ingresa el segundo numero: "))

# print("El resultado es: ",num1 + num2)

# Ejercicio. Pedir al usuario que ingrese tres numeros y multiplicarlos 
#entre si, imprimir el resultado. 

#num1 = int(input("Ingresa el primer numero: "))
#num2 = int(input("Ingresa el segundo numero: "))
#num3 = int(input("Ingresa el tercer numero: "))

#multiplicacion = num1 * num2 * num3
#print("El resultado es: ", multiplicacion)

# Ejercicio 2 / Pedir al usuario un numero del 1 al 100 y llamar a la funcion
# que retornaba la nota que creamos hace un rato 
# utilizando el valor ingresado por el usuario.

# numero1 = int(input("Ingresa tu nota de 1 al 100: "))
# def puntaje(nota):

#    if nota < 60:
#     print("Sorry bro, no pasaste: NOTA 1")
#    elif nota >= 60 and nota <= 70:
#        print("PASASTE CON: 2")
#    elif nota >= 71 and nota <= 75:
#        print("PASASTE CON: 3")
#    elif nota >= 76 and nota <= 85:
#        print("PASASTE CON: 4")
#    elif nota >= 86 and nota <= 99:
#        print("PASASTE CON: 5")
#    elif nota == 100:
#        print("5 felicitado bro")
#    else:
#        print("Valor no admitido")
# puntaje(numero1)

# Recibir un año y calcular si es biciesto o no


### BUCLE WHILE = MIENTRAS #### 

# x = 0
# while x != 5:
#     print("Hola, este es un bucle while")
#     x = int(input("Ingresa un numero: "))
#     print("El valor de x es: ")
# print("Termino!")

# CONTADOR A LA INVERSA & Si queres sumar cambiar condicion y numero contador
# contador = 10

# while contador > 0:
#     print("Sigo con el bucle while")
#     contador = contador - 1
#     print("Se repitio", contador, "veces")

# Usando while pedir al usuario 5 ingredientes para hacer una pizza
# y agregar a una lista, al final imprimir la lista.

# lista_ingredientes = []
# contador = 0
# while contador < 5:
#     ingrediente= input("Ingresa tu lista de compras: ")
#     lista_ingredientes.append(ingrediente)
#     contador = contador + 1
# print(lista_ingredientes)

# numero_secreto = 7
# adivino = False

# while adivino == False:
#     apuesta = input("Adivina el numero secreto del 1 al 10: ")
#     if int(apuesta) == numero_secreto:
#         print("GANASTE!!!")
#         adivino = True
#     else:
#         print("Segui participando nde arruinado")

# ejercicio> Crear un juego de adivinar el numero como el de arriba y darle pistas al usuario
# si el numero es mayor o menor al numero a adivinar.
# pista: usar elif. 
# import random
# numero_secreto = random.randint(1,101)
# adivino = False

# while adivino == False:
#     apuesta = int(input("Escribe un numero secreto del 1 al 100: "))
#     if apuesta == numero_secreto:
#         print("GANASTE!!!")
#         adivino = True
#     elif numero_secreto < apuesta:
#         print("El numero que ingresaste es mayor al numero a adivinar. Intentalo de nuevo")
#     elif numero_secreto > apuesta:
#         print("El numero que ingresaste es menor al numero a adivinar. Intentalo de nuevo")
