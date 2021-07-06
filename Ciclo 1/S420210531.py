#CONJUNTO A CADENA
conjunto = {'h' , 'o' , 'l' , 'a'}
cadena = ''.join(conjunto)
print(cadena)

#CONJUNTO A TUPLA
conjunto = {'h' , 'o' , 'l' , 'a'}
tupla = tuple(conjunto)
print(tupla)

#CONJUNTO A LISTA
conjunto = {'h' , 'o' , 'l' , 'a'}
lista = list(conjunto)
print(lista)

#CONVERSIÓN A DICCIONARIOS
# CADENA A DICCIONARIO
cadena = 'hola'
diccionario = dict()

#Método A
for k , x in enumerate(cadena):
    diccionario[k] = cadena[k]
print(diccionario)

#Método B
for k in range(len(cadena)):
    diccionario[k] = cadena[k]
print(diccionario)

#Método C
dic_str = dict(zip(range(len(cadena)),cadena))
print(dic_str)

#LISTAS A DICCIONARIOS
lista = ['a' , 'm' , 'o' , 'r']
dic_lista = dict(zip(range(len(lista)) , lista))
print(dic_lista)

#TUPLA A DICCIONARIO
tupla = ('c' , 'a' , 's' , 'a')
dic_tupla = dict(zip(range(len(tupla)) , tupla))
print(dic_tupla)

#CONJUNTO A DICCIONARIO
conjunto = {'c' , 'o' , 'm' , 'a'}
dic_conjunto = dict(zip(range(len(conjunto)) , conjunto))
print(dic_conjunto)

dic_conjunto = dict(zip(conjunto , range(len(conjunto)))) #Inversión de llaves y values
print(dic_conjunto)

#DICCIONARIO A CADENAS
diccionario = {0: 'h', 1: 'o', 2: 'l', 3: 'a'}
cadena_1 = ''.join(diccionario.values())
print(cadena_1)
cadena_1 = ''.join(str(diccionario.keys()))
print(cadena_1)
cadena_1 = ''.join(str(diccionario.items()))
print(cadena_1)

#DICCIONARIO A TUPLAS
diccionario = {0: 'h', 1: 'o', 2: 'l', 3: 'a'}
tupla_key = tuple(diccionario.keys())
print(tupla_key)
tupla_value = tuple(diccionario.values())
print(tupla_value)
tupla_item = tuple(diccionario.items())
print(tupla_item)

#DICCIONARIO A LISTAS
diccionario = {0: 'h', 1: 'o', 2: 'l', 3: 'a'}
lista_key = list(diccionario.keys())
print(lista_key)
lista_value = list(diccionario.values())
print(lista_value)
lista_item = list(diccionario.items())
print(lista_item)

#DICCIONARIO A CONJUNTOS
diccionario = {0: 'h', 3: 'o', 1: 'l', 4: 'a' , 2: 'h'}
conjunto_key = set(diccionario.keys())
print(conjunto_key)
conjunto_value = set(diccionario.values())
print(conjunto_value)
conjunto_item = set(diccionario.items())
print(conjunto_item)

conjunto_2 = {(3, 'o'), (1, 'l'), (0, 'h'), (4, 'a'), (2, 'h'), (0, 'h'), (4, 'a')} #Evalua las subtuplas como elementos individuales completos y los compara entre si
print(conjunto_2)

#FUNCIÓN ZIP con listas paralelas
numero = [1, 2 , 3 , 4 , 5 , 6 , 7]
letra = {'uno' , 'dos' , 'tres' , 'cuatro' , 'cinco' , 'seis'} #Coge la lista más corta para generar el diccionario

resultado_dic = dict(zip(numero , letra))
print(resultado_dic)

resultado_tup = tuple(zip(numero , letra))
print(resultado_tup)

