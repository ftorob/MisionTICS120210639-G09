#MÉTODOS DE LISTAS
#APPEND para agregar más items a la lista
version_phone = [2.5 , 3.6 , 4 , 5]
version_phone.append(6)
print(version_phone)

version_phone += [8]
print(version_phone)

#COUNT permite saber cuantas veces está un item en una lista
print(version_phone.count(4))

#EXTEND agrega al final de la cadena un itema
version_phone.extend([15])
version_phone.extend(range(10 , 14))
print(version_phone)

#INDEX ubica la posición de un item dentro de la lista
print(version_phone.index(5))
try: #Intentar probar y añadir mensaje personalziado en caso de error
    print(version_phone.index(5 , 5)) #La misma busqueda pero desde la posición 10 --> ValueError: 5 is not in list
except:
    print('El número no se encuentra en la lista')

#INSERT permite colocar un item en una posición determinada
version_phone.insert(2 , 1)
version_phone.insert(3 , 2)
version_phone.insert(4 , 3)
print(version_phone)

#POP elimina un item de la lista
version_phone.pop(6)
print(version_phone)

#REMOVE elimina el item definido que primero aparezca en la lista
version_phone.remove(1)
print(version_phone)

#REVERSE invierte el orden de una lista
version_phone.reverse()
print(version_phone)

#SORT permite ordenar los elementos de una lista
version_phone.sort() #Orden ascendente
print(version_phone)

version_phone.sort(reverse = True) #Orden descendente
print(version_phone)

#TUPLAS son inmutables --> es una lista de valores separadas por comas
t = 'a' , 'b' , 'c' , 'd' , 'e' #Sin parentesis
print(t)
print(type(t))

t = ('Esto es una cadena' , 'a' , 'b' , 'c' , 'd' , 'e') #Con parentesis
print(t)
print(type(t))

t1 = ('a' , )
print(type(t1)) #Es una tupla al tener la coma

t2 = ('a')
print(type(t2)) #Es un str al estar sin coma

t = tuple()
print(t) #Es una tupla vacia
print(type(t)) #Crear tupla con TUPLE

t = tuple('lupines') #Convierte la palabra en letras :OOOOOOOOOOOO
print(t)
print(t[3 : 5]) #Extrae solo IN
print(t[3 : 6]) #Extrae INE

#t[0] = '5' #Las tuplas son inmutables

#COMPARANDO TUPLAS por posiciones
print((0 , 1 , 2000) < (0 , 3 , 4)) #Verdadero
print((0 , 2000 , 1) < (0 , 3 , 4)) #Falso
print((0 , 3 , 1) < (0 , 3 , 4)) #Verdadero

#ORDENANDO cadena de texto
txt = 'but soft what light windows break in'
palabras = txt.split() #Se crea una lista con las palabras que forman el texto
print(palabras)

#CICLOS --> FOR ||| IN
l = list()

for subcadena in palabras:
    l.append((len(subcadena) , subcadena))

print(l)

l.sort(reverse = True)
print(l)

res = list()

for longitud , palabra in l:
    res.append(palabra)

print(res)
print(type(res))

#El mismo ejercicio anterior pero ahora agregando otro parámetro a evaluar
l = list()

for subcadena in palabras:
    l.append((len(subcadena) , subcadena , subcadena[ : 1]))

print(l)

l.sort(reverse = True)
print(l)

res = list()
res_num = list()

for longitud , palabra , letra in l:
    res.append(palabra)
    res_num.append(longitud)

print(res)
print(res_num)
print(type(res))


#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------CONTINUA LISTAS-------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

#Iterar sobre la cadena de caracteres
vocales = 'aeiou'
for letra in 'fernando':
    if letra in vocales:
        print(letra)

#Iterar sobre una lista
mensaje = 'Hola, como estás tu?'
mensaje.split()

for palabra in mensaje.split():
    print(palabra)

#Iterar sobre dos secuencias
preguntas = ['nombre' , 'objetivo' , 'sistema operativo']
respuestas = ['Leonardo' , 'aprender Python y Plone' , 'Linux']

for pregunta , respuesta in zip(preguntas , respuestas):
    print('¿Cuál es tu {0}? , La respuesta es : {1}'.format(pregunta , respuesta))

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------CONTINUA TUPLAS-------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

#Asignación de tuplas
adrr = 'ftorob@unal.edu.co'
user , domain = adrr.split('@')
print(user)
print(domain)

#Diccionarios & tuplas
d = {'a' : 10 , 'b' : 1 , 'c' : 22}
t = list(d.items())
print(t)

t.sort
print(t)

#MÉTODOS
#COUNT
#INDEX

#CONVERTIR A TUPLAS
# TUPLA SIMPLE
tu = 12345 , 45321 , 'hola!'
print(tu)

#Tupla anidada
ot = tu , (1 , 2 , 3)
print(ot)

#Asignar valores de tupla en variables
x , y , z = tu
print(x)
print(y)
print(z)

#Cuidar el seguimiento del número de la númeración
tecnologias = ('zope' , 'plone' , 'pyramid')
for i in range(len(tecnologias)):
    print(i , tecnologias[i])
