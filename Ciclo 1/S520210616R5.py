#Desarrollo RETO 5 --> Esquema base de la función
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd
    import matplotlib.pyplot as plt

    if rt_archivo.split('.')[3] != 'csv':
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(r'C:\Users\FERNANDO TORO\Documents\MisionTic2022\Pruebas Saber 11 2020A.csv') #No lo lee online
    except:
        print('Error al leer el archivo de datos.')

    for columna in df.columns:
        print(columna)
    
    df_filtro = df.query('punt_matematicas >= 65 <= 90')
    print(df_filtro)

    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    print(df_departamento)

    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    print(d_promedio)

    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    print(d_mediana)
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()
    print(d_totales)

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    print(d_datos1)
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    print(d_datos2)
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']
    print(d_datos2)

    out1 = d_datos2.to_csv(r'C:\Users\FERNANDO TORO\Documents\MisionTic2022\S520210616R5.csv')
    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
infoIcfes(ruta)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> No toma el link online entonces se trabajó con un documento local y un promedio errado
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5
    import matplotlib.pyplot as plt #Validación 5

    if rt_archivo.split('.')[3] != 'csv': #Validación 1
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(r'C:\Users\FERNANDO TORO\Documents\MisionTic2022\Pruebas Saber 11 2020A.csv') #No lo lee online
    except:
        print('Error al leer el archivo de datos.') #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65 <= 90') #Validación 3 No funciona
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']
    print(d_datos2)

    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
infoIcfes(ruta)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> Consulta tutor SANTIAGO GIRALDO
#Falta corrección de lo ONLINE
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5
    import matplotlib.pyplot as plt #Validación 5

    if rt_archivo[-3:] != 'csv': #Validación 1
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(rt_archivo) #No lo lee online
    except:
        return 'Error al leer el archivo de datos.' #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_filtro = df_filtro.query('punt_matematicas <= 90') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']

    #return {'Departamento': {departamento_residencia}, 'Promedio': {df_promedio }, 'Mediana': {df_mediana}, 'Total Puntuación': {df_totales}}   

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
print(infoIcfes(ruta))

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> Función Para corregir
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5
    import matplotlib.pyplot as plt #Validación 5

    if rt_archivo.split('.')[3] != 'csv': #Validación 1
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(r'C:\Users\FERNANDO TORO\Documents\MisionTic2022\Pruebas Saber 11 2020A.csv') #No lo lee online
    except:
        print('Error al leer el archivo de datos.') #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_filtro = df_filtro.query('punt_matematicas <= 90') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']
    print(d_datos2)

    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
infoIcfes(ruta)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> Solucionado el filtro y la salida a DICT
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5
    import matplotlib.pyplot as plt #Validación 5

    if rt_archivo[-3:] != 'csv': #Validación 1
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(r'C:\Users\FERNANDO TORO\Documents\MisionTic2022\Pruebas Saber 11 2020A.csv') #No lo lee online
    except:
        print('Error al leer el archivo de datos.') #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65 & punt_matematicas <= 90') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']
    
    return d_datos2.to_dict()
    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
print(infoIcfes(ruta))

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> Solucionado el filtro y la salida a DICT
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5
    import matplotlib.pyplot as plt #Validación 5

    if rt_archivo[-3:] != 'csv': #Validación 1
        print('Extensión inválida.')
    
    try:
        df = pd.read_csv(rt_archivo) #No lo lee online
    except:
        print('Error al leer el archivo de datos.') #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65 & punt_matematicas <= 90') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntuación']
    
    return d_datos2.to_dict()
    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
print(infoIcfes(ruta))

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Desarrollo RETO 5 --> ENCODING -MATPLOT +PUNTACION
def infoIcfes(rt_archivo : str) -> dict:
    import pandas as pd #Validación 5

    if rt_archivo[-3:] != 'csv': #Validación 1
        return 'Extensión inválida.'
    
    try:
        df = pd.read_csv(rt_archivo , encoding = 'latin-1') #No lo lee online
    except:
        return 'Error al leer el archivo de datos.' #Validación 2
    
    df_filtro = df.query('punt_matematicas >= 65 & punt_matematicas <= 90') #Validación 3 --> Un estudiante de Caldas con 100 no se elimina
    df_departamento = df_filtro[['punt_matematicas' , 'departamento_residencia']]
    
    d_promedio = df_departamento.groupby('departamento_residencia' , as_index = False).mean()
    d_mediana = df_departamento.groupby('departamento_residencia' , as_index = False).median()
    d_totales = df_departamento.groupby('departamento_residencia' , as_index = False).count()

    d_datos1 = pd.merge(d_promedio , d_mediana , on = 'departamento_residencia')
    d_datos2 = pd.merge(d_datos1 , d_totales , on = 'departamento_residencia')
    d_datos2.columns = ['Departamento' , 'Promedio' , 'Mediana' , 'Total Puntación']
    
    return d_datos2.to_dict()
    pass

ruta = (r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-39/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv')
print(infoIcfes(ruta))