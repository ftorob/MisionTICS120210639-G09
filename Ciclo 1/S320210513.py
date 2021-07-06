#LISTAS
lista = [1 , 2.5 , 'DevCode' , [7 , 9], 3]
print(lista) #Imprime todos los elementos de la lista
print(lista[0]) #Imprime el elemento de la lista en posición 0
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4]) #Imprime el elemento de la lista en posición 6 (así no hay imprime hasta donde se tenga)
print('Hicimos este cambio -->' , lista[1:4]) #Concatenar con str
print(lista[1:6]) #Imprime de la posición 1 a la 6 (así no exista)
print(lista[1:6:1]) #Imprime de 1 a 6 de uno en uno (2.5 --> 'DevCode --> [7,9] --> 3)
print(lista[1:6:2]) #Imprime de 1 a 6 de dos en dos (2.5 --> [7,9])
print(lista[1:6:3]) #Imprime de 1 a 6 de tres en tres (2.5 --> 3)
print(lista[1:6:4]) #Imprime de 1 a 6 de cuatro en cuatro espacios (2.5) los espacios se pueden ver como las comas
print(lista[3][0]) #Imprime los items de una lista anidada) --> 7

#Crear una lista con variables
nombre = 'Juan' #Objeto inmutable
edad = 15
lista = [nombre , edad] #Objeto inmutable
print(lista)
nombre = 'Jorge'
print(lista) #No se actauliza con el nombre de JORGE porque son objetos inmutables

nombres = ['Ana' , 'Bernardo'] #Primera lista
edades = [13 , 26] #Segunda lista
lista = [nombres , edades] #Une las dos listas en una
print(lista)

# contador = contador + 1
# acumuladores = acumuladores + variable

nombres += ['Cristina'] #El operador += agrega un nuevo item a la lista de nombres
print(lista)

#Función LEN
factura = ['pan' , 'huevos' , 200 , 500]
print(len(factura)) #Cantidad de items de la lista
print(factura[-1]) #Posición de la última a la primera siendo -1 la última letra
#print(factura[7]) #IndexError: list index out of range
print(factura[:7]) #imprime toda la lista
factura[1] = 'carne' #mutar la posiicón de una lista con otro valor
print(factura)