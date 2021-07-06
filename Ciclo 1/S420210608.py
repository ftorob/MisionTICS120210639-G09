#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Intalación de la libreria NUMPY
# Escriba en el terminal de Python "pip install numpy" --> Se procederá a la descarga y ejecución automática en PYTHON
# Para saber si está instalado y verificar la versión damos 'python -m pip --version'
#Cerrar el programa y volverlo a abrir para empezar a utilizarlo

import numpy as np #Importar la libreria numpy para poder trabajar matrices
a = np.array([34 , 25  ,7])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

#Crear una matriz de dos dimensiones
b = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
print(b.shape)
print(b[0 , 0] , b[0 , 1] , b[0 , 2] , b[1 , 0])

#Crear una matriz con posiciones en ceros de 3 x 3
matriz = np.zeros((3,3))
print(matriz)

#Crear una matriz con posiciones en unos de 2 X 3 (2 Filas  - 3 Columnas)
b_one = np.ones((2,3))
print(b_one)

#Crear una matriz constante con un parametro establecido
c_full = np.full((5 , 5) , 8) #Filas - Columnas - Parametro que queramos (1,2,3,4,5,6,7,a,b)
print(c_full)

#Craer una matriz definida
d = np.eye(4)
print(d)

#Crear una matriz llena de valores aleatorios
e = np.random.random((2 , 2))
print(e)

#Indexación de matrices
a = np.array([[1 , 2 , 3] , [5 , 6 , 7] , [9 , 10 , 11]])
print(a)

b = a[:2 , 1:3] #--> Sacar 2 - 3 ||| 6 - 7
print(b)

c = a[1:3 , 1:3] #--> Sacar 6 - 7 ||| 10 - 11
print(c)

d = np.fliplr(a) #Invierte el orden de los elementos del ARRAY
print(d)
print(d[0 , 1]) #--> Extraer el 2
print(d[2 , 1]) #--> Extraer el 10

a[0 , 0] = 77 #Mute el valor sobre la matriz original en la posición 0,0
print(a)

#Crear una matriz de 3 filas con cauatro columnas
a = np.array([[1 , 2 , 3 , 4] , [5 , 6 , 7 , 8] , [9 , 10 , 11 , 12]])
print(a)

row_1 = a[1,:]
print(row_1)
row_2 = a[1:2 , :]
print(row_2)
print(row_1 , row_1.shape)
print(row_2 , row_2.shape)

col_1 = a[:,1]
print(col_1 , col_1.shape)  
col_2 = a[: , 1 : 2]
print(col_2 , col_2.shape)

#INDEXACIÓN DE MATRICES DE ENTEROS
#Array de tris dimensiones (filas) + 2 elementos (columnas)
a = np.array([[1 , 2] , [3 , 4] , [5 , 6]])
print(a)
print(a.shape) #.shape me dice cuantas filas y columnas tengo
print(a[[0,1,2] , [0,1,0]]) #El primer grupo de [Filas] y segundo grupo [Columnas] que al unirlas dan las posiciones en el array
print([a[0 , 0] , a[1 , 1] , a[2 , 0]]) #Extrae lo mismo que la anterior

#INDICES
a = np.array([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] , [10 , 11 , 12]]) #Va a ser la matriz
print(a)

b = np.array([0 , 2 , 0 , 1]) #Va a ser los indices
print(b)

print(a[np.arange(4) , b]) #Se une a - b para obtener otra matriz --> a va de 1 a 4 y el indice de b selecciona el elemento

#Ahora vamos a mutar la matriz sumando a las posiciones del subindice b con +10
a[np.arange(4) , b] += 10
print(a)

#Indexación de matriz booleana
a = np.array([[1 , 2] , [3 , 4] , [5 , 6]])
print(a)

bool_idx = (a > 2) #Evalua la condición del array y arroja FALSE/TRUE
print(bool_idx)
print(a[bool_idx]) #Devuelve los elementos que cumplen esa condición
print(a[a > 2]) #Obtiene el mismo resultado de un array de arreglo 1