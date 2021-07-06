#Ejemplo aplicado 2 ALL - ANY
uids = ['B1CD102354' , 'B1CDEF2354' , 'ab6F6ñ.']

for uid in uids:
    cond = list()

    #Por lo menos dos letras mayusculas en el alfabeto inglés
    cond.append(len(list(filter(lambda x : x.isupper() , list(uid)))) >= 2)
    print(cond)

    #Por lo menos tiene tres digitos
    cond.append(len(list(filter(lambda x : x.isdigit() , list(uid)))) >= 3)
    print(cond)

    #Solo digitos alfanuméricos
    cond.append(len(list(filter(lambda x : not(x.isalnum()) , list(uid)))) == 0)
    print(cond)

    #No existan repetidos los caracteres
    cond.append(len(uid) == len(set(uid)))
    print(cond)

    #Tener longitud exacta de 10 caracteres
    cond.append(len(uid) == 10)
    print(cond)

    print('Valido' if all(cond)
    else 'Inválido'
    )

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#Listas comprensibles
#Cree una lista con cuadrados de los números, de dos en dos, del 4 al 30, divisibles por 3
mi_lista = []
for x in range(4 , 31 , 2):
    if x % 3 == 0:
        mi_lista.append(x**2)
print(mi_lista)

#Este ejercicio se puede hacer en una sola linea
mi_lista = [x**2 for x in range(4 , 31 , 2) if x % 3 == 0]
print(mi_lista)

#Cree un diccionario en el que las llaves sean una tupla entre el número 3 a 10 y su respectivo cubo
#Y donde los valores sean las listas con los cuadrados de los números de dos en dos, entre el 4 y el 30
#Que son divisbles enteros con el primer elmento de su llave correspondiente

mi_diccionario = dict()
for x in range (3 , 11):
    mi_diccionario[(x , x**3)] = []
    for y in range(4 , 31 , 2):
        if y % x == 0:
            mi_diccionario[(x , x**3)].append(y**2)

print(mi_diccionario)


#Ahora haga el ejercicio anterior en una sola linea
mi_dict = {(y , y**3) : [x**2 for x in range(4 , 31 , 2) if x % y == 0] for y in range (3 , 11)}
print('\n' , mi_dict)

#La siguiente linea sirve para validar si los dos diccionarios tienen los mismos valores
respuesta = all(list(map(lambda x : x[0] == x[1] , list(zip(mi_diccionario.values() , mi_dict.values())))))
print(respuesta)

#Buscar un valor en los dos diccionarios
valor = 324
respuesta = any(list(map(lambda x : valor in x[0] or valor in x[1] , list(zip(mi_diccionario.values() , mi_dict.values())))))
print(respuesta)

#Otro ejercicio lista de comprension
listavocales = ['A' , 'E' , 'I' , 'O' , 'U']
listanombres = ['Juan' , 'Alejandro' , 'Fernando' , 'Rene' , 'Uriel' , 'Angel' , 'Omar' , 'Maria' , 'Ana' , 'Fredy' , 'Elias']
listanueva = [nom for nom in listanombres if nom[0] in listavocales]
print(listanueva)

#Con el anterior ejemplo nos ahorramos estas lineas de código
lista = list()
for nombre in listanombres:
    if nombre[0] in listavocales:
        lista.append(nombre)

print(lista)