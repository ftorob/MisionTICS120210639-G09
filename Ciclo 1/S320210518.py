#[1 , 2] --> Listas --> LIST
#(1 , 2) --> Tuplas --> TUPLE
#{'uno' : 1 , 'dos' : 2} --> Diccionarios --> DICT
# {1 , 2 , 3} --> Conjuntos --> SET

#CONJUNTOS
s = {1 , 2 , 3 , 4 , 5}
print(s)

s = {True , 3.14 , None , False , 'Hola Mundo' , (1 , 2)}
print(s)

#s = {[1 , 2]} --> No se puede agregar una lista a un conjunto
#print(s)

s = {} #--> De esta forma se crea automaticamente un diccionario
print(type(s))

s = set() #--> Al configurarlo así aparece SET como tipo de conjunto
print(type(s))

s1 = set([1 , 2 , 3]) #Así se puede ingresar una lista a un conjunto
s2 = set(range(5)) #Así se puede pasar un rango en un conjunto
print(s1)
print(s2)

print(list({1 , 2 , 3})) #Convertir de un conjunto a una LISTA
print(set([1 , 2 , 2 , 3 , 4])) #Convierte una lista en un conjunto. Si hay valor repetido lo unifica o elimina.

c = {1 , 9 , 6 + 1 , 1 , 2 , 5} #Un conjunto permite ordenar y quitar duplicados
print(c)

a = set('hola pythonista') #Elimina las letras repetidas
print(a)

mi_conjunto = {1 , 3 , 2 , 9 , 3 , 1}
print(mi_conjunto)

for numero in mi_conjunto: #Imprime cada número por separado del conjunto
    print(numero)

#MÉTODOS CONJUNTOS
#ADD --> Agregar más elementos al conjunto
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
print(set_mutable1)

set_mutable1.add(22.00001)
print(set_mutable1)

#CLEAR --> Limpiar el conjunto
set_mutable1.clear()
print(set_mutable1)

#COPY --> Copiar un conjunto en otro
set_mutable = set([4.0 , 'carro' , True])
otro_set_mutable = set_mutable.copy()
print(otro_set_mutable)

#DIFFERENCE --> Genera las diferencias que hay de un conjunto a otro
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
print(set_mutable1)
set_mutable2 = set([11 , 5 , 9 , 2 , 4 , 8])
print(set_mutable2)

print(set_mutable1.difference(set_mutable2))
print(set_mutable2.difference(set_mutable1))

a = {1 , 2 , 3 , 4} #Es un ejemplo de lo de arriba
b = {2 , 3}
c = a - b
print(c)

print({1 , 2 , 3} == {3 , 2 , 1}) #Principio de externalidad --> Compara si dos conjuntos son iguales
print({1 , 2 , 3} == {3 , 6 , 1})

#DIFFERENCE_UPDATE --> Actualiza un conjunto con la diferencia que tiene  respecto a otro
proyecto1 = {'python' , 'zope2' , 'ZODB3' , 'pytz'}
print(proyecto1)
proyecto2 = {'python' , 'plone' , 'diazo'}
print(proyecto2)

proyecto1.difference_update(proyecto2)
print(proyecto1)

#DISCARD --> Elimina un elemento del conjunto si está presente
proyecto1.discard('zope2')
print(proyecto1)

#INTERSECTION --> Muestra los valores iguales en dos conjuntos
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
print(set_mutable1)
set_mutable2 = set([11 , 5 , 9 , 2 , 4 , 8])
print(set_mutable2)

print(set_mutable1.intersection(set_mutable2)) #O set_intersection = set_mutable1 & set_mutable2

#INTERSECTION.UPDATE --> Un elemento común a todos los conjuntos
proyecto1 = {'python' , 'zope2' , 'pytz'}
proyecto2 = {'python' , 'plone' , 'diazo' , 'z3c.form'}
proyecto3 = {'python' , 'django' , 'django-filter'}

proyecto1.intersection_update(proyecto2 , proyecto3)
print(proyecto1)

#ISDISJOINT --> Arroja TRUE si entre los dos conjuntos no hay elemntos en común
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
print(set_mutable1)
set_mutable2 = set([11 , 5 , 9 , 2 , 4 , 8])
print(set_mutable2)
print(set_mutable1.isdisjoint(set_mutable2))

#ISSUBSET --> Arroja TRUE si el conjunto evaluado es un subconjunto de otro
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
set_mutable2 = set([11 , 5 , 9 , 2 , 4 , 8])
set_mutable3 = set([11 , 5 , 2 , 4])

print(set_mutable2.issubset(set_mutable1))
print(set_mutable3.issubset(set_mutable1))

#ISSUPERSET --> Arroja TRUE si el conjunto es un supraconjunto del conjunto evaluado
set_mutable1 = set([4 , 3 , 11 , 7 , 5 , 2 , 1 , 4])
set_mutable2 = set([11 , 5 , 9 , 2 , 4 , 8])
set_mutable3 = set([11 , 5 , 2 , 4])

print(set_mutable1.issuperset(set_mutable2))
print(set_mutable1.issuperset(set_mutable3))

#POP --> Remueve aleatoriamente un elemento del conjunto y lo muestra
paquetes = {'python' , 'zope' , 'plone' , 'django'}
print('El valor aleatorio es: ' + paquetes.pop())

#REMOVE --> Remueve un elemento del conjunto
paquetes.remove('django')
print(paquetes)


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#Estructuras Iterativas WHILE ||| FOR
x = 0 #Debo inicializar el valor de una variable
x = x + 1 #Esto es un contador incremental
print(x)

y = 10
y = y - 1 #Esto es un contador de decremento
print(y)

n = 5 #Declarar variable de inicio
while n > 0: #Condición para cumplir --> Bucle
    print(n) #Operación 1 --> Iteración
    n = n - 1 #Operación 2 ---> Variable de iteración
print('Finalizó...') #Acción para finalizar cuando se rompa el ciclo

'''
5! (n) = 1 (resultado) X 2 (número actual) X 3 X 4 X 5
r1 = 1 * 2 = 2 (r2)
r2 = 2 * 3 (2 + 1) = 6 (r3)
r3 = 6 * 4 (3 + 1) = 24 (r4)
r4 = 24 * 5 (4 + 1) = 120 (r5 --> stop)
'''

def factorial(n : int)-> int:
    resultado = 1 #Inicio 1
    numero_actual = 2 #Inicio 2
    while numero_actual <= n: #Condición a cumplir para que cuando se incumpla se tenga un fin (True continua - False para)
        resultado = resultado * numero_actual #Operación 1
        numero_actual += 1 #numero_actual = numero_actual + 1 #Operación 2
        #print(resultado)
    return resultado #Fin

print(factorial(5))

#Hay que evitar hacer ciclos infinitos se traba el terminal calculando números
#i = 1
#while i != 10: #La operación arrojará números infinitos diferentes de 10
#    print(i)
#    i = i + 2
# print('Terminé...')

#Otro ciclo infinito puede suceder por mala indentación
#i = 1
#while 1 < 10:
#    print(1) #Inprime el 1 infinitamente
#i = i + 1
#print('Terminé...')

#Olvidar el avance da ciclo infinito
#i = 1
#while 1 < 10:
#    print(1) #Inprime el 1 infinitamente
#print('Terminé...')

#Bucle WHILE controlado por evento
promedio , total , contar = 0.0 , 0 , 0 #Inicio de todas las variables en cero
print('Introduzca la nota de un estudiante (-1 para salir): ')
nota = int(input()) #Inicio de la primera nota
while nota != -1: #Condición para salir del ciclo y calcular el promedio
    total = total + nota #Suma notas
    contar = contar + 1 #Contador incrmeental en 1
    print('Introduzca la nota de un estudiante (-1 para salir): ') #Agregar otra nota
    nota = int(input()) #Ingresar otra nota
promedio = total/contar #Al salir del ciclo calcula el promedio
print('El promedio de notas de los estudiantes es :' , promedio) #Imprime la nota promedio del estudiante

#Existe también el WHILE + ELSE (la diferencia con el IF + ELSE es que en WHILE el ELSE siempre se va a ejecutar cuando se salga del ciclo es como parte A + parte B)
# Mientras que el ELSE se cumple en IF solo si se viola su condición
promedio , total , contar = 0.0 , 0 , 0 #Inicio de todas las variables en cero
print('Introduzca la nota de un estudiante (-1 para salir): ')
nota = int(input()) #Inicio de la primera nota
while nota != -1: #Condición para salir del ciclo y calcular el promedio
    total = total + nota #Suma notas
    contar = contar + 1 #Contador incrmeental en 1
    print('Introduzca la nota de un estudiante (-1 para salir): ') #Agregar otra nota
    nota = int(input()) #Ingresar otra nota
else:
    promedio = total/contar #Al salir del ciclo calcula el promedio
    print('El promedio de notas de los estudiantes es :' , promedio) #Imprime la nota promedio del estudiante


#-------------------------------------------------------------------------------------------
#-------------------------CONTINUA CONJUNTOS MÉTODOS----------------------------------------
#-------------------------------------------------------------------------------------------

#Diferencia simétrica --> Devuelve los elementos que están en uno u otro conjunto pero no en ambos
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1.symmetric_difference(set_mutable2))

#Union --> Devuleve los elementos de uno y otro conjunto en uno solo
print(set_mutable1.union(set_mutable2)) #--> a = set_mutable1 | set_mutable2 (así se puede representar)



