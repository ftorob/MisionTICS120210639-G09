#PROGRAMACIÓN FUNCIONAL
#Envoltura de funciones en python
def suma(val1 = 0,  val2 = 1):
    return val1 + val2
#clc = suma(10, 12)
#print(clc)

#Asignar una funcuón a una variable
funcion_suma = suma

def operacion(funcion , val1 = 0 , val2 = 0):
    return funcion(val1 , val2)

#Enviar como parametro una función
resultado = operacion(funcion_suma , 10 , 18)
print(resultado)

def crear_funcion(operador):
    if operador == '+':
        def suma(val1 = 0 , val2 = 0):
            return val1 + val2
        return suma
    elif operador == '-':
        def resta(val1 = 0 , val2 = 0):
            return val1 - val2
        return resta

    elif operador == '*':
        def multiplicar(val1 = 0 , val2 = 0):
            return val1 * val2
        return multiplicar
    elif operador == '/':
        def dividir(val1 = 0 , val2 = 0):
            return val1 / val2
        return dividir

def operacion(funcion, val1 = 0 , val2 = 0):
    return funcion(val1 , val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,14,35)
print(resultado)

funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta,10,5)
print(resultado)

funcion_multiplicar = crear_funcion('*')
resultado = operacion(funcion_multiplicar,8,8)
print(resultado)

funcion_dividir = crear_funcion('/')
resultado = operacion(funcion_dividir,121,11)
print(resultado)

#Función LAMBDA --> Argumentos : cuerpo de la función
sumar = lambda val1 = 0 , val2 = 0 : val1 + val2
operaciones = lambda operaciones , var1 = 0 , var2 = 0 : operaciones(var1 , var2)

resultado = operaciones(sumar , 10 , 18)
print(resultado)

sin_parametros = lambda : True #LAMBDA sin parámetros
print(sin_parametros() == True)

con_valores = lambda val , val1 = 0 , val2 = 0 : val + val1 + val2
resultado = con_valores(3 , 45 , 59)
print(resultado)

con_asterisco = lambda *args : args[0]
resultado = con_asterisco('a')
print(resultado)

con_asterisco = lambda *args : args[-1] #El * nos genera una lista
resultado = con_asterisco(1,2,3,4,5)
print(resultado)

con_asterisco = lambda *args : args[5] #El * nos genera una lista
lista = [1,2,3,4,5,6,7,8]
resultado = con_asterisco(*lista) #Debe colocarse el * para poder leerlo
print(resultado)

def suma(*variable_args):
    return variable_args[0] + variable_args[-1]

tupla = (1,2,3,4,5,6,7,8,9)
print(suma(*tupla))

con_doble_asterisco = lambda **kwargs : kwargs['b'] #El ** genera un diccionario
dicc = {'a' : 1 , 'b' : 15}
resultado = con_doble_asterisco(**dicc)
print(resultado)

resultado = lambda **kwargs : sum(kwargs.values())
print(resultado(**dicc))

print((lambda **kwargs : sum(kwargs.values()))(a = 1, b = 3 , c = 5))

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#FUNCIÓN MAP --> Aplica una función a un conjunto de datos
def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
resultado = list(map(cuadrado , lista))
print(lista)
print(resultado)

resultado_1 = list(map(lambda elemento : elemento * elemento , lista)) #Convertir a función LAMBDA
print(resultado_1)

#POTENCIA CON MAP
#Importar pow
from math import pow

numero = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
potencia = [3 , 2 , 4 , 3 , 2 , 4 , 3 , 2 , 4]

resultado = list(map(pow , numero , potencia))
print(resultado)

#FACTORIAL con MAP

def factorial (numero = 0):
    contador = 2
    resultado = 1
    while contador <= numero:
        resultado = resultado * contador
        contador += 1
    return resultado

numero_2 = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
resultado = list(map(factorial,numero_2))
print(resultado)

#FUNCION FILTER --> Filtra por condiciones
def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5 , 2 , 6 , 8 , 10 , 7 , 77 , 55 , 2 , 1 , 30 , 4 , 2 , 3)
print('Número de elementos de la tupla original' , len(tupla))
resultado = tuple(filter(mayor_a_cinco , tupla))
print('Número de elementos de la tupla filtrada: ' , len(resultado))
print(resultado)

resultado = tuple(filter(lambda elemento : elemento > 5 , tupla)) #Convertir a LAMBDA
print(resultado)

#Obtener números pares
items = (0,1,2,3,4,5,6,7,8,9,10)
pares = list()
for i in items:
    if i % 2 == 0:
        pares.append(i)
print(pares)


pares = list()
for i in range(101):
    if i % 2 == 0:
        pares.append(i)
print(pares)

#Obtener números impares
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
resultado = tuple(filter(lambda elemento : elemento % 2 != 0 , tupla)) #Función LAMBDA
print(resultado)