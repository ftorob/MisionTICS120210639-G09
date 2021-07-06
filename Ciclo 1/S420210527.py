#CONVERSIÓN DE CONTENEDORES

#CADENAS A LISTAS
cadena = 'grupo 39'
lista = list(cadena)
print(lista)

#CADENA A TUPLAS
cadena_1 = 'hola'
cadena_2 = 'adios'
num = 15
tupla_1 = tuple(cadena_1)
tupla_g = (tupla_1 , num , tuple(cadena_2))
print(tupla_g)

#CADENAS A CONJUNTOS
cadena_3 = 'hhhoooolaaaaaaaaa'
conjunto = set(cadena_3)
print(conjunto)

cadena_4 = '9876666663363633328322121'
conjunto = set(cadena_4)
conjunto_0 = set()
for x in conjunto:
    num = conjunto_0.add(int(x))
print(conjunto_0)

#LISTAS A CADENAS
#Método A
lista = ['h' , 'o' , 'l' , 'a' , 1 , (1 , 2 , 3)]
try:
    cadena = ''.join(lista) #JOIN permite concatenar
    #cadena = 'ftb'.join(lista)
    print(cadena)
except:
    print('No se puede concatenar un entero en un string')

#Método B
convertir_cadena = ''
try:
    for x in lista:
        convertir_cadena = convertir_cadena + x
    print(convertir_cadena)
except:
    print('No se puede concatenar un entero en un string')

#Método C
convertir_cadena = ''
for x in lista:
   convertir_cadena = convertir_cadena + str(x)
print(convertir_cadena)

#LISTAS A TUPLAS
lista = ['h' , 'o' , 'l' , 'a' , 123]
tupla = tuple(lista)
print(tupla)

#LISTAS A CONJUNTOS
lista = ['h' , 'o' , 'l' , 'a' , 1 , 2 , 3 , 1 , 1 , 2]
conjunto = set(lista)
print(conjunto)

#TUPLAS A CADENA
tupla = ('h' , 'o' , 'l' , 'a')
union = ''.join(tupla)
print(union)

#TUPLAS A LISTAS
tupla_2 = ('hola' , 123 , 'mundo')
lista = list(tupla_2)
print(lista)

#TUPLAS A CONJUNTOS
tupla_3 = ('hola' , 111 , 'mundo' , 'hola')
conjunto = set(tupla_3)
conjunto.add(15)
print(conjunto)