'''
#Diccionario 1A
lectura = {
    '50100119001' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 1232,
            'lec_actual' : 1304
            }
        ],
        'estrato' : 1,
        'estado' : 'activo'
        },
    '501002190324' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 1203,
            'lec_actual' : 1230
            }
        ],
        'estrato' : 4,
        'estado' : 'activo'
    }
}
print(lectura)


#Diccionario 1B
tarifa = {
    'cargo_basico' : 9850,
    'consumo' : 800.27
}
print(tarifa)
'''

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
'''
#Diccionario 2A
lectura = {
    '50100119001' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 1232,
            'lec_actual' : 1304
            }
        ],
        'estrato' : 1,
        'estado' : 'inactivo'
        }
}
print(lectura)

#Diccionario 2B
tarifa = {
    'cargo_basico' : 10450,
    'consumo' : 1200.40
}
print(tarifa)
'''

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#Diccionario 3A
lectura = {
    '201501001' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 12,
            'lec_actual' : 60
            }
        ],
        'estrato' : 1,
        'estado' : 'activo'
        },
    '201501002' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 2,
            'lec_actual' : 6
            }
        ],
        'estrato' : 2,
        'estado' : 'activo'
    },
    '201501003' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 23,
            'lec_actual' : 43
            }
        ],
        'estrato' : 3,
        'estado' : 'activo'
    },
    '201501004' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 90,
            'lec_actual' : 120
            }
        ],
        'estrato' : 1,
        'estado' : 'activo'
    },
    '201501005' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 1,
            'lec_actual' : 9
            }
        ],
        'estrato' : 1,
        'estado' : 'inactivo'
    },
    '201501006' : {
        'toma_lectura' : [
            {
            'lec_anterior' : 10,
            'lec_actual' : 20
            }
        ],
        'estrato' : 6,
        'estado' : 'activo'
    }
}
print(lectura)

#Diccionario 3B
tarifa = {
    'cargo_basico' : 9850,
    'consumo' : 800.27
}
print(tarifa)

'''
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#Extracción de datos de los diccionarios
for pos , dat in lectura.items():
    print(pos)
    print(dat)
    lecturadic = dat['toma_lectura']
    for val in range(len(lecturadic)):
        a = dat['toma_lectura'][0]['lec_anterior'] #Extrae lectura anterior dictA
        print(a)
        b = dat['toma_lectura'][0]['lec_actual'] #Extrae lectura actual dictA
        print(b)
        c = dat['estrato'] #Extrae el estrato dictA
        print(c)
        d = dat['estado'] #Extrae el estado dictA
        print(d)
        e = tarifa['cargo_basico'] #Extrae el cargo básico dictB
        print(e)
        f = tarifa['consumo'] #Extrae el consumo dictB
        print(f)

#Definición de la función
def inforServicio (lectura : dict , tarifa : dict) -> tuple:
    pass

#Función paso a paso con print de resultados
#Definición de la función
def inforServicio (lectura : dict , tarifa : dict) -> tuple:
    total_consumom3 = list()
    total_subsidio = list()
    total_liquidado = list()
    id = list()

    for pos , dat in lectura.items():
        print(pos)
        print(dat)
        lecturadic = dat['toma_lectura']
        for val in range(len(lecturadic)):
            print(val)
            if dat['estado'] != 'inactivo':
                a = dat['toma_lectura'][0]['lec_anterior'] #Extrae lectura anterior dictA
                print(a)
                b = dat['toma_lectura'][0]['lec_actual'] #Extrae lectura actual dictA
                print(b)
                c = dat['estrato'] #Extrae el estrato dictA
                print(c)
                d = dat['estado'] #Extrae el estado dictA
                print(d)
                e = tarifa['cargo_basico'] #Extrae el cargo básico dictB
                print(e)
                f = tarifa['consumo'] #Extrae el consumo dictB
                print(f)
                g = b - a #Consumo individual en m3
                print(g)
                total_consumom3.append(g)

                if dat['estrato'] == 1:
                    subsidio = (e * 0.45) + (f * g * 0.45)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.55) + ((f * g)*0.55) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 2:
                    subsidio = (e * 0.30) + (f * g * 0.30)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.70) + ((f * g)*0.70) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 3:
                    subsidio = (e * 0.15) + (f * g * 0.15)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.85) + ((f * g)*0.85) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] >= 4 and dat['estrato']  <= 6:
                    subsidio = 0
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 1.55) + ((f * g)*1.55) , 2)
                    total_liquidado.append(liquidado)

                id.append(pos)

    print(total_consumom3)
    print(total_subsidio)
    print(total_liquidado)
    print(id)

    resultado = list(zip(id , total_liquidado))
    print(resultado)


    from functools import reduce
    sumam3 = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_consumom3)
    print(sumam3)
    
    subsidio_gen = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_subsidio)
    print(subsidio_gen)

    tupla = (resultado, round(sumam3 , 2) , round(subsidio_gen , 2))
    print(tupla)

inforServicio(lectura , tarifa)
'''

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

'''
#Definición de la función A --> No arroja los valores al llegar a estado inactivo
def inforServicio (lectura : dict , tarifa : dict) -> tuple:
    total_consumom3 = list()
    total_subsidio = list()
    total_liquidado = list()
    id = list()

    for pos , dat in lectura.items():
        lecturadic = dat['toma_lectura']
        for val in range(len(lecturadic)):
            if dat['estado'] != 'inactivo':
                a = dat['toma_lectura'][0]['lec_anterior'] #Extrae lectura anterior dictA
                b = dat['toma_lectura'][0]['lec_actual'] #Extrae lectura actual dictA
                c = dat['estrato'] #Extrae el estrato dictA
                d = dat['estado'] #Extrae el estado dictA
                e = tarifa['cargo_basico'] #Extrae el cargo básico dictB
                f = tarifa['consumo'] #Extrae el consumo dictB
                g = b - a #Consumo individual en m3
                total_consumom3.append(g)

                if dat['estrato'] == 1:
                    subsidio = (e * 0.45) + (f * g * 0.45)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.55) + ((f * g)*0.55) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 2:
                    subsidio = (e * 0.30) + (f * g * 0.30)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.70) + ((f * g)*0.70) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 3:
                    subsidio = (e * 0.15) + (f * g * 0.15)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.85) + ((f * g)*0.85) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] >= 4 and dat['estrato']  <= 6:
                    subsidio = 0
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 1.55) + ((f * g)*1.55) , 2)
                    total_liquidado.append(liquidado)

                id.append(pos)
            else:
                return 'Sin lecturas'
            pass
 
    resultado = list(zip(id , total_liquidado))

    from functools import reduce
    sumam3 = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_consumom3)
    
    subsidio_gen = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_subsidio)

    tupla = (resultado, round(sumam3 , 2) , round(subsidio_gen , 2))
    return tupla

print(inforServicio(lectura , tarifa))
'''
'''
#Definición de la función ---> Arroja todos los valores --> Probar
def inforServicio (lectura : dict , tarifa : dict) -> tuple:
    total_consumom3 = list()
    total_subsidio = list()
    total_liquidado = list()
    id = list()

    for pos , dat in lectura.items():
        lecturadic = dat['toma_lectura']
        for val in range(len(lecturadic)):
            if dat['estado'] != 'inactivo':
                a = dat['toma_lectura'][0]['lec_anterior'] #Extrae lectura anterior dictA
                b = dat['toma_lectura'][0]['lec_actual'] #Extrae lectura actual dictA
                c = dat['estrato'] #Extrae el estrato dictA
                d = dat['estado'] #Extrae el estado dictA
                e = tarifa['cargo_basico'] #Extrae el cargo básico dictB
                f = tarifa['consumo'] #Extrae el consumo dictB
                g = b - a #Consumo individual en m3
                total_consumom3.append(g)

                if dat['estrato'] == 1:
                    subsidio = (e * 0.45) + (f * g * 0.45)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.55) + ((f * g)*0.55) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 2:
                    subsidio = (e * 0.30) + (f * g * 0.30)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.70) + ((f * g)*0.70) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 3:
                    subsidio = (e * 0.15) + (f * g * 0.15)
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 0.85) + ((f * g)*0.85) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] >= 4 and dat['estrato']  <= 6:
                    subsidio = 0
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 1.55) + ((f * g)*1.55) , 2)
                    total_liquidado.append(liquidado)

                id.append(pos)
            else:
                continue
    pass
 
    resultado = list(zip(id , total_liquidado))

    from functools import reduce
    if len(total_consumom3) > 0:
        sumam3 = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_consumom3)
    else:
        return 'Sin lecturas'
    
    subsidio_gen = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_subsidio)

    tupla = (resultado, round(sumam3 , 2) , round(subsidio_gen , 2))
    return tupla

print(inforServicio(lectura , tarifa))
'''

#Definición de la función ---> Corrección de decimales por resta + round --> PASOOOOOOOOOOOOOOO :)))))))))
def inforServicio (lectura : dict , tarifa : dict) -> tuple:
    total_consumom3 = list()
    total_subsidio = list()
    total_liquidado = list()
    id = list()

    for pos , dat in lectura.items():
        lecturadic = dat['toma_lectura']
        for val in range(len(lecturadic)):
            if dat['estado'] != 'inactivo':
                a = dat['toma_lectura'][0]['lec_anterior'] #Extrae lectura anterior dictA
                b = dat['toma_lectura'][0]['lec_actual'] #Extrae lectura actual dictA
                c = dat['estrato'] #Extrae el estrato dictA
                d = dat['estado'] #Extrae el estado dictA
                e = tarifa['cargo_basico'] #Extrae el cargo básico dictB
                f = tarifa['consumo'] #Extrae el consumo dictB
                g = b - a #Consumo individual en m3
                total_consumom3.append(g)

                if dat['estrato'] == 1:
                    subsidio = round((e * 0.45) + (f * g * 0.45) , 2)
                    total_subsidio.append(subsidio)
                    liquidado = round((e - e * 0.45) + ((g)*(f - f*0.45)) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 2:
                    subsidio = round((e * 0.30) + (f * g * 0.30),2)
                    total_subsidio.append(subsidio)
                    liquidado = round((e - e* 0.30) + ((g)*(f - f*0.30)) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] == 3:
                    subsidio = round((e * 0.15) + (f * g * 0.15) , 2)
                    total_subsidio.append(subsidio)
                    liquidado = round((e - e * 0.15) + ((g)*(f - f*0.15)) , 2)
                    total_liquidado.append(liquidado)
                if dat['estrato'] >= 4 and dat['estrato']  <= 6:
                    subsidio = 0
                    total_subsidio.append(subsidio)
                    liquidado = round((e * 1.55) + ((f * g)*1.55) , 2)
                    total_liquidado.append(liquidado)

                id.append(pos)
            else:
                continue
    pass
 
    resultado = list(zip(id , total_liquidado))

    from functools import reduce
    if len(total_consumom3) > 0:
        sumam3 = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_consumom3)
    else:
        return 'Sin lecturas'
    
    subsidio_gen = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , total_subsidio)

    tupla = (resultado, round(sumam3 , 2) , round(subsidio_gen , 2))
    return tupla

print(inforServicio(lectura , tarifa))