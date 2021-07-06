#LISTAS COMPUESTAS
#Estas son listas simples
notas = [8 , 9 , 7] #Tipo entero
alturas = [1.65 , 1.80 , 1.76] #Tipo float
dias = ['lunes' , 'martes' , 'miercoles'] #Tipo str

#
notas_l =[[4 , 5] , [9 , 7] , [6 , 3]] #Aquí hay tres listas de dos elementos dentro de una lista general

#EJEMPLO 1
lista = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] , [10 , 11 , 12]] #Aquí hay una lista general con cuatro sublistas de tres elementos enteros
print(lista) #Indica toda la lista
print(lista[0]) #Indica la primera lista --> [1 , 2 , 3]
print(lista[0][0]) #Indica el primer elemento de la primera sublista --> 1

for x in range(len(lista[0])):
    print(lista[0][x])

for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])

#EJEMPLO 2
lista_e = [[1 , 2 , 3 , 4 , 5] , [6 , 7 , 8 , 9 ,10]] #Sumar por separado cada lista

for m in range(len(lista_e)):
    resultado = 0
    for n in range(len(lista_e[m])):
        resultado = resultado + lista_e[m][n]
    print(resultado)

#EJEMPLO 3
lista_e = [[1 , 2 , 3 , 4 , 5] , [6 , 7 , 8 , 9 ,10]] #Sumar ahora las dos listas y de el resultado general

resultado = 0
for m in range(len(lista_e)):
    for n in range(len(lista_e[m])):
        resultado = resultado + lista_e[m][n]
print(resultado)

#EJEMPLO 4
lista_1 = [[1] , [1 , 2] , [1 , 2 , 3] , [1 , 2 , 3 , 4] , [1 , 2 , 3 , 4 , 5]] #Suma todas las listas de una vez1

resultado = 0
for m in range(len(lista_1)):
    for n in range(len(lista_1[m])):
        resultado = resultado + lista_1[m][n]
print(resultado)


#EJEMPLO 5
padres = list() #padres = [[] , [] , []]
hijos = list() #hijos = [[] , [] , []]

for k in range (3):
    pa = input('Ingrese el nombre del padre: ')
    ma = input('Ingrese el nombre de la madre: ')
    padres.append([pa , ma])
    cantidad = int(input('Cantidad de hijos en la familia: '))
    hijos.append([])
    for x in range(cantidad):
        hijo = input('Ingrese el nombre del hijo: ')
        hijos[k].append(hijo)

#print(padres)
#print(hijos)

print('Listado de padre, madre e hijos')
for x in range(len(padres)):
    print('Padre: ' , padres[x][0])
    print('Madre: ' , padres[x][1])
    for k in range(len(hijos[x])):
         print('Hijo: ' , hijos[x][k])


print('Listado de padre con la cantidad de hijos')
for x in range(len(padres)):
    print('Padre: ' , padres[x][0])
    print('Hijos: ' , len(hijos[x]))

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#CONTENEDORES
#STRING (CADENAS - ORDENADAS)
cadena = "Este es un atributo "
cadena_nueva = cadena + "nuevo"
print('Flujo: ' , cadena_nueva)
print(cadena[0:4])

#TUPLAS (ORDENADAS)
def calcularCostoArticulo():
    nombreUsuario = 'TripulanteMisionTic2022'
    password = 'pr0gr4m4c10n'
    tuplaCredencialesBD = (nombreUsuario , password) #Tupla
    impuestos = tuplaCredencialesBD

#LISTAS (ORDENADAS)
itinerario = [['Santa Marta' , 1] , ['Cartagena' , 2] , ['San Andrés' , 4]]
itinerario.append(['Providencia' , 2])
itinerario.pop(1)
itinerario[0][1] += 1
itinerario[0] , itinerario[-1] = itinerario[-1] , itinerario[0]

print(itinerario)

#RECORRIDOS
for i in range(len(itinerario)):
    print('Elemento en la posición i: ' , i)
    print(itinerario[i])

for j in itinerario:
    print(j)

for i , datos in enumerate(itinerario): #ME GUSTA ESTE MÉTODO (IMPRIME LA POSICIÓN Y EL COMTENIDO DE LAS LISTAS)
    print('Posición:' , i)
    print(datos)

for i , datos in enumerate(itinerario): #IMPRIME TODOS LOS DATOS INDIVIDUALES
    for k , data in enumerate(itinerario[i]):
        print(data)

#Recorrido conjuntos
gruposCalificados = {'P45' , 'P61' , 'P33' , 'P87'}
print('Grupos calificados es de tipo: ' , type(gruposCalificados))
gruposCalificados.add('P17')
gruposCalificados.add('P17')
gruposCalificados.remove('P45')
print(gruposCalificados)
if 'P17' in gruposCalificados:
    print('P17 ya ha sido calificado')