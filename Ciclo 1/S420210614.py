import pandas as pd
import numpy as np

#Ahora vamos a utilizar un diccionario para crear una serie
d = {
    'Ene' : 8,
    'Feb' : 6,
    'Mar' : 7
}

s = pd.Series(d)
print(s)

s = pd.Series(d , index = ['Abr' , 'Mar' , 'Feb' , 'Ene'] , dtype = int)
print(s)

#Ahora vamos a utilizar un escalar
s = pd.Series(7 , index = ['Ene' , 'Feb' , 'Mar'])
print(s)

#Construcción de DataFrames con diccionario
elementos = {
    'Número atómico' : [1 , 6 , 47 , 88],
    'Masa atómica' : [1.008 , 12.011 , 107.87 , 226],
    'Familia' : ['No metal' , 'No metal' , 'Metal' , 'Metal']
}

print(elementos)

tabla_periodica = pd.DataFrame(elementos)
print(tabla_periodica)

tabla_periodica = pd.DataFrame(elementos , index = ['H' , 'C' , 'Ag' , 'Ra'] , columns = ['Familia' , 'Masa atómica' , 'Número atómico'])
print(tabla_periodica)

#Cosntrucción de DataFrames con NUMPY
import pandas as pd
import numpy as np

unidad_datos = np.array([
    [2 , 5 , 3  , 2],
    [4 , 6 , 7 , 2],
    [3 , 2 , 4 , 1]
])

unidades = pd.DataFrame(unidad_datos)
print(unidades)

unidades = pd.DataFrame(unidad_datos , index = ['2015' , '2016' , '2017'] , columns = ['Ag' , 'Au' , 'Cu' , 'Pt'])
print(unidades)

#Ahora construir DataFrame con varios diccionarios
unidad_2015 = {
    'Ag' : 2,
    'Au' : 5,
    'Cu' : 3,
    'Pt' : 2
}

unidad_2016 = {
    'Ag' : 4,
    'Au' : 6,
    'Cu' : 7,
    'Pt' : 2
}

unidad_2017 = {
    'Ag' : 3,
    'Au' : 2,
    'Cu' : 4,
    'Pt' : 1
}

unidades = pd.DataFrame([unidad_2015 , unidad_2016 , unidad_2017] , index = ['2015' , '2016' , '2017'])
print(unidades)

unidades = pd.DataFrame([unidad_2015 , unidad_2016 , unidad_2017] , index = ['2015' , '2016' , '2017'] , columns = ['Ag' , 'Au' , 'Cu' , 'Pt'])
print(unidades)

#Método HEAD
entradas = pd.Series([11 , 18 , 12 , 16 , 9 , 16 , 22 , 28 , 31 , 29 , 30 , 12],
index = ['ene' , 'feb' , 'mar' , 'abr' , 'may' , 'jun' , 'jul' , 'ago' , 'sep' , 'oct' , 'nov' , 'dic'])

print(entradas)

salidas = pd.Series([9 , 26 , 18 , 15 , 6 , 22 , 19 , 25 , 34 , 22 , 21 , 14],
index = ['ene' , 'feb' , 'mar' , 'abr' , 'may' , 'jun' , 'jul' , 'ago' , 'sep' , 'oct' , 'nov' , 'dic'])

print(salidas)

almacen = pd.DataFrame({'entradas' : entradas , 'salidas' : salidas})
almacen['neto'] = almacen.entradas - almacen.salidas
print(almacen)
print(almacen.head(5)) #Trae los cinco primeros valores de la tabla