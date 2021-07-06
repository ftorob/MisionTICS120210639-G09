import numpy as np

#Tipos de datos
a = np.array([1 , 2])
print(a.dtype) #Entero 32

b = np.array([1.0 , 2.0])
print(b.dtype) #Float 64

c = np.array([1 , 2] , dtype = np.float64)
print(c) #Forzar un entero a que sea FLOAT

d = np.array([1 , 2] , dtype = np.str0)
print(d) #Forzar un entero a que sea string

#MATEMÁTICAS de matrices
x = np.array([[1 , 2] , [3 , 4]] , dtype = np.float64)
y = np.array([[5 , 6] , [7 , 8]] , dtype = np.float64)

print(x + y) #Está sumando las columnas
print(np.add(x , y)) #Igual suma pero con función

print(x - y) #Resta de las columnas
print(np.subtract(x , y)) #Igual resta pero con función

print(x * y) #Multuplicación de las matrices
print(np.multiply(x , y)) #Igual multiplicar con función

print(x / y) #División de matrices
print(np.divide(x , y)) #Igual dividir pero con función

print(np.sqrt(x)) #Raiz cuadrada de X


#Función DOT
x = np.array([[1 , 2] , [3 , 4]])
y = np.array([[5 , 6] , [7 , 8]])

v = np.array([9 , 10])
w = np.array([11 , 12])

print(v.dot(w)) #Multiplicó y luego sumó los valores para dar 219
print(np.dot(v , w)) 

print(x.dot(v)) #Multuplica (1*9)+(10*2) = 29
print(y.dot(v)) #Multiplica (9*5)+(10*6) = 105
print(x.dot(y))

#BROADCASTING
x = np.array([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] , [10 , 11 , 12]])
y = np.array([1 , 0 , 1])
z = np.empty_like(x)

print(x)
print(y)
print(z)

for i in range(4):
    z[i , :] = x[i , :] + y
print (z)

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

#LIBRERIA PANDAS
#Para instalar pandas escriba en el terminal 'pip install pandas'
#Los dos componentes principales son SERIES (es una columna)  & DATAFRAMES (tabla multidimensional conformada por una colección de series)

import pandas as pd
ventas = pd.Series([15 , 21 , 12] , index = ['Ene' , 'Feb' , 'Mar'])
print(ventas)
print(ventas[0]) #Buscar por posición
print(ventas['Ene']) #Buscar por nombre de etiquetas
print(ventas.dtype) #Tipo de dato

print(ventas.index)
print(ventas.values)

ventas.name = 'Ventas 2021'
ventas.index.name = 'Meses'
print(ventas)

print(ventas.axes)
print(ventas.shape)

#DATAFRAMES
datos = { 
    'manzanas' : [3 , 2 , 0 , 1],
    'naranjas' : [0 , 3 , 7 , 2]
}

compras = pd.DataFrame(datos , index = ['Juni' , 'Roberto' , 'Lily' , 'David']) #Indice o etiqueta de las FILAS
print(compras)
print(compras.index)
print(compras.values)
print(compras.columns) #Indice o etiqueta de las COLUMNAS

compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'
print(compras)

s = pd.Series([7 , 5 , 6])
print(s)

s = pd.Series([7 , 5 , 6] , index = ['Ene' , 'Feb' , 'Mar'])
print(s)