nterm = 8

n1 = 0
n2 = 1
cont = 0

# verifica si los numeros ingresados son validos
if nterm <= 0:
   print("Ingresa un numero entero positivo")
elif nterm == 1:
   print("La secuencia fibonacci de",nterm,"termino seria:")
   print(n1)
else:
   print("La secuencia de ",nterm," terminos es:")
   while cont < nterm:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       cont += 1