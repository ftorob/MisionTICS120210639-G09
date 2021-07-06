#Manejo de archivos .CSV (Coma Separated Values)
import pandas as pd

datos = {
    'first_name' : ['Sigrid' , 'Joe' , 'Theodoric' , 'Kennedy' , 'Beatrix' , 'Olimpia'],
    'last_name' : ['Mannock' , 'Hinners' , 'Rivers' , 'Donell' , 'Parlett' , 'Guenther'],
    'edad' : [27 , 31 , 36 , 53 , 48 , 36],
    'montos_1' : [7.17 , 1.90 , 1.11 , 1.41 , 6.69 , 4.62],
    'montos_2' : [8.06 , '?' ,  5.90 , '?' , '?' , 7.48]
}

var = pd.DataFrame(datos)
print(var)

var.to_csv('c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.csv') #Guardar como archivo CSV y colocar extensión .csv
#var.to_csv('c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.csv' , sep = ';' , header = None) #Puedo configurar para separar por ; en lugar de ,
# El header es para saber si la primera fila es encabezado de etiquetas o no

#Lecturas de archivo CSV
df = pd.read_csv('c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.csv',
    skiprows = 1 , #Asignar un número de fila como cabecera
    names = ['Id' , 'First Name' , 'Last Name' , 'Edad' , 'Salario #1' , 'Salario #2'], #Cambia nombre etiquetas
    na_values = '?') #El ? es reemplazado por NaN
print(df)
print(type(df))
print(df['Salario #2'][2]) #--> Ubucar un dato (5.9) dentro de la tabla

df = pd.read_csv('c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.csv',
    skiprows = 1 , #Asignar un número de fila como cabecera
    names = ['Id' , 'First Name' , 'Last Name' , 'Edad' , 'Salario #1' , 'Salario #2'], #Cambia nombre etiquetas
    na_values = '?', #El ? es reemplazado por NaN
    index_col = 'Id') #Asigna la columna indice para que no quede repetida
print(df)

df = pd.read_csv('c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.csv',
    skiprows = 1 , #Asignar un número de fila como cabecera
    names = ['Id' , 'First Name' , 'Last Name' , 'Edad' , 'Salario #1' , 'Salario #2'], #Cambia nombre etiquetas
    na_values = '?', #El ? es reemplazado por NaN
    index_col = ['First Name' , 'Last Name']) #Asigna la columna First Name & Last Name como indices de las columnas
print(df)
