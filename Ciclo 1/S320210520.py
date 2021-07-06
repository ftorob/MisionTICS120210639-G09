#Sentencias utilitarias
#BREAK sirve para romper el ciclo con alguna condición
var = 10
while var > 0:
    print('Valor de la variable' , var)
    var = var - 1
    if var == 5:
        break

#CONTINUE sirve para continuar si se llega a cumplir una condición
var = 10
while var > 0:
    var = var - 1
    if var == 5: #Con esta condición se omite el cinco al cumplirse
        continue #Continua ejecutando el ciclo hasta finalziar
    print('El valor de la variable es ' , var)

#CICLOS FOR
#No necesita declarar una variable inicial
for x in range(0,5): #0 es la posición inicial - 5 es la posicicón final - x es el contador automático
    print('Estamos en la iteración:' , x)

#Además se puede personalizar el for
for y in range(0 , 10 , 2): #Corre el ciclo de 2 en 2
    print('Estamos en la iteración:' , y)

#Se puede hacer en reversa y agregar un salto de linea
for z in range(10 , 0 , -2): 
    print('Estamos en la iteración:' , z , '\n')

#For con palabras
oracion = 'Mery entiende muy bien python'
frase = oracion.split() #Aquí se puede indicar cual es el separador como ' ' o ',' o '.' para saber donde cortar las palabras
print('La oración a analizar es' , oracion)

for palabra in range(len(frase)):
    print('La palabra' , frase[palabra] , 'está en la posición' , palabra)

#For con diccionario uno
datos_basicos = {
    'nombres' : 'Fernando',
    'apellidos' : 'Toro',
    'cedula' : '1019102077',
    'fecha_nacimiento' : '15/11/1994',
    'lugar_nacimiento' : 'Villeta',
    'nacionalidad' : 'Colombiana',
    'estado_civil' : 'unión libre'
}

parametros = datos_basicos.keys() #Imprime los parametros o espacios del diccionario
print(parametros)

valores = datos_basicos.values() #Imprime los valores del diccionario
print(valores)

datos = datos_basicos.items() #Imprime una lista de tuplas con los valores
print(datos)

for clave_1 , valor_1 in datos: #Imprime el formato que le dimos a los datos ||| PARAMETROS , VALORES en la LISTA
    print(clave_1 , ':' , valor_1)

for clave_1 in datos_basicos.items(): #Imprime tuplas
    print(clave_1)

#For con diccionario dos
frutas = {
    'fresa' : 'roja',
    'limon' : 'verde',
    'papaya' : 'naranja',
    'manzana' : 'amarillo',
    'guayaba' : 'rosa'
}

for llaves in frutas:
    print(llaves , 'es de color' , frutas[llaves])

#FOR + ELSE
db_connection = '127.0.0.1' , '5432' , 'root' , 'nomina' #Esto es una tupla sin parentesis
print(db_connection)

for parametro in db_connection:
    print(parametro)
else:
    print('el comando de postgreSQL es: $ psql -h {} -p {} -u {} -d {}'.format(db_connection[0] , db_connection[1] , db_connection[2] , db_connection[3]))

#REPRESENTADO RELACIONES EN LISTAS
#Listas PARALELAS

nombres = list() #Es igual a nombres = []
edades = list()

for x in range(5):
    nombre = input('¿Cuál es su nombre?: ')
    nombres.append(nombre)
    edad = int(input('¿Cuál es su edad: '))
    edades.append(edad)

print(nombres)
print(edades)

print('Los nombres de las personas mayores de edad son')
for x in range(5):
    if edades[x] >= 18:
        print('Nombre' , nombres[x])