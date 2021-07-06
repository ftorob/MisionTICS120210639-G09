#Manejo de archivos EXCEL
#Crear un archivo EXCEL
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

datos = {
    'first_name' : ['Sigrid' , 'Joe' , 'Theodoric' , 'Kennedy' , 'Beatrix' , 'Olimpia'],
    'last_name' : ['Mannock' , 'Hinners' , 'Rivers' , 'Donell' , 'Parlett' , 'Guenther'],
    'edad' : [27 , 31 , 36 , 53 , 48 , 36],
    'montos_1' : [7.17 , 1.90 , 1.11 , 1.41 , 6.69 , 4.62],
    'montos_2' : [8.06 , '?' ,  5.90 , '?' , '?' , 7.48]
}

df = pd.DataFrame(datos , columns = ['first_name' , 'last_name' , 'edad' , 'montos_1' , 'montos_2'])
print(df)

#Se debe installar el paquete 'p'ip install openpyxl' para leer el archivo Excel
ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210614.xlsx' #Muy importante la r para asegurar que sea un path valido
df.to_excel(ruta , sheet_name = 'Salario') #Sheet_name cambia el nombre de la hoja

#Para leer el archivo de Excel
df = pd.read_excel(ruta)
print(df)

df = pd.read_excel(ruta , header=None) #No hay cabecera
print(df)

df = pd.read_excel(ruta , skiprows=1) #Skiprow selecciona la FILA1 como la cabecera
print(df)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Manejo de archivo .TXT

datos = ['Linea 1' , 'Linea 2' , 'Linea 3' , 'Linea 4' , 'Linea 5']
ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210615.txt' #No olvidar cambiar la extensión

fichero = open(ruta , 'w' ) #Abre un archivo TXT 'w --> escribir ||| r --> Leer ||| a --> añadir contenido al existente'
for linea in datos: #Ciclo for para escribir en el fichero
    fichero.write(linea) #Lineas de arriba
    fichero.write('\n') #Enter entre cada linea
fichero.close() #Cerrar TXT


#Otras formas del anterior ejemplo es:
'''
#Método A
fichero = open(ruta , 'w' ) #Abre un archivo TXT
for linea in datos: #Ciclo for para escribir en el fichero
    print(linea , file = fichero) #--> Resume dos lineas
    fichero.close() #Cerrar TXT
'''

'''
#Método B
fichero = open(ruta , 'w)
fivero.writelines("%s\n" % s for s in datos)
fichero.close()
'''

# Lectura de archivos TXT de una vez
fichero = open(ruta , 'r')
linea = fichero.readlines()
fichero.close()
print(linea)

#Lectura de archivos TXT linea a linea
fichero = open(ruta , 'r')
linea = []

for lin in fichero:
    linea.append(lin)
fichero.close()

print(linea)

#Eliminar el \n en cada linea
linea1 = [s.rstrip('\n') for s in linea]
print(linea1)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Manejo de archivo .JSON
#Intercambio de datos basado en texto
# Permite que un dato tengas más datos dentro algo que no permite CSV

import json

datos = dict() #Diccionario vacio

datos['clientes'] = [] #Lista del contenido de un valor del diccionario

datos['clientes'].append(
    {
        'first_name' : 'Sigrid',
        'last_name' : 'Manock',
        'age' : 7,
        'amount' : 7.17
    }
)

datos['clientes'].append(
    {
        'first_name' : 'Joe',
        'last_name' : 'Hinners',
        'age' : 31,
        'amount' : [1.90 , 5.5]
    }
)

datos['clientes'].append(
    {
        'first_name' : 'Theodoric',
        'last_name' : 'Rivers',
        'age' : 36,
        'amount' : 1.11
    }
)

ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S520210615.json' #No olvidar cambiar la extensión a JSON
with open(ruta , 'w') as file:
    json.dump(datos , file , indent = 4)

#Lectura de archivos JSON
with open(ruta) as file:
    data = json.load(file)

    for client in data['clientes']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Análisis de datos - Gráficas
# Se debe instalar la libreria MATPLOTLIB.PYPLOT --> 'pip install matplotlib'
# Se debe importar la libreria --> import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        'name' : ['jhon' , 'mary' , 'peter' , 'jeff' , 'bill' , 'lisa' , 'jose'],
        'age' : [23 , 78 , 22 , 19 , 45 , 33 , 20],
        'gender' : ['M' , 'F' , 'M' , 'M', 'M' , 'F' , 'M'],
        'state' : ['california' , 'dc' , 'california' , 'dc' , 'california' , 'texas' , 'texas'],
        'num_children' : [2 , 0 , 0 , 3 , 2 , 1 , 4],
        'num_pets' : [5 , 1 , 0 , 5 , 2 , 2 , 3]
    }
)

print(df.head()) #Así solo selecciona las primeras cuatro columnas de la tabla)

df.plot(kind = 'scatter' , x = 'num_children' , y = 'num_pets' , color = 'red')
plt.show()

df.plot(kind = 'bar' , x = 'name' , y = 'age' , color = 'blue')
plt.show()

ax = plt.gca()
df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)
plt.show()

print(type(df.groupby('state')['name'].nunique()))
df.groupby('state')['name'].nunique().plot(kind='bar')
plt.show()

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Ejercicio similar al reto 5

def ejemplolink(ar : str) -> dict:
    import pandas as pd
    if ar.split('.')[1] != 'csv':
        print('Extensión Invalida')
    
    try:
        df = pd.read_csv(ar)
    except:
        print('Error al cargar archivo')

    for columna in df.columns: #Se hace para visualizar el nombre de todas las columnas que hay en el archivo
        print(columna)

    df_filtrar = df.query('TOTAL_ACTIVOS_2018 > 34000000')
    df_domicilio = df_filtrar[['TOTAL_ACTIVOS_2018' , 'DEPARTAMENTO_DOMICILIO']]

    d_promedio = df_domicilio.groupby("DEPARTAMENTO_DOMICILIO" , as_index = False).mean()
    d_mediana = df_domicilio.groupby("DEPARTAMENTO_DOMICILIO" , as_index = False).median()
    d_totales = df_domicilio.groupby("DEPARTAMENTO_DOMICILIO" , as_index = False).count()


    d_datos = pd.merge(d_promedio , d_mediana , on = "DEPARTAMENTO_DOMICILIO")
    d_datos = pd.merge(d_datos , d_totales , on = "DEPARTAMENTO_DOMICILIO")
    d_datos.columns = ['Dpto Domicilio' , 'Promedio' , 'Mediana' , 'Total']

    print(d_datos)


#El archivo S510000615_1.csv se descargo de DATOS.GOV --> 1000 EMPRESAS MÁS GRANDES DE COLOMBIA
#ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S510000615.json' #Invalida la extensión
#ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S510000615_1.csv' #Invalido el nombre del archivo
ruta = r'c:/Users/FERNANDO TORO/Documents/MisionTic2022/S510000615.csv' #Correcto
ejemplolink(ruta)
