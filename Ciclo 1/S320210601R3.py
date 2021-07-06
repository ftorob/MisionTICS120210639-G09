'''
#Creación del diccionario Número 1
creditos = {
    '2015020192098' : {
        'nombres' : 'Juan',
        'apellidos' : 'Arias Ruiz',
        'est_credito' : 'Activo',
        'credito' : [
            {
                'id_credito' : 'C0192098',
                'cuotas' : 24,
                'valor' : 3066936.00,
                'interes' : 0.020,
                'cuo_vencidas' : 8,
                'cuo_pagadas' : 10
            }
        ]
    }
}
print(creditos)
'''


#Creación del diccionario Número 2
creditos = {
    '2018015647382':{
        'nombres' : 'Luis Antonio',
        'apellidos' : 'Lopez Rueda',
        'est_credito' : 'Activo',
        'credito' : [
            {
                'id_credito' : 'C0013453',
                'cuotas' : 60,
                'valor' : 87558500,
                'interes' : 0.020,
                'cuo_vencidas' : 30,
                'cuo_pagadas' : 7
            }
        ]
    },
    '2019041209845' : {
        'nombres' : 'Elias',
        'apellidos' : 'Diaz Lopez',
        'est_credito' : 'Activo',
        'credito' : [
            {
                'id_credito' : 'C033551',
                'cuotas' : 3,
                'valor' : 87558,
                'interes' : 0.020,
                'cuo_vencidas' : 1,
                'cuo_pagadas' : 2
            }
        ]
    }
}
#print(creditos)


'''
#Se crea una función que recrea la simulación de las cuotas de la tablas
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            print(total_credito)
            total_cuotas = credito[val]['cuotas']
            print(total_cuotas)
            num_cuota = 0
            while num_cuota < total_cuotas:
                num_cuota = num_cuota + 1
                print(num_cuota)
                vlr_cuota = total_credito/total_cuotas * num_cuota
                print(vlr_cuota)
                vlr_saldo = total_credito - vlr_cuota
                print(vlr_saldo)
                vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                print(vlr_interes)
                vlr_pagar = vlr_cuota + vlr_interes
                print(vlr_pagar)

            
        #total = credito[val]['cuotas'] * credito[val]['cuo_pagadas']
        #print(total)
        #print('El valor del credito es: ' , credito[val]['valor'])
        #print(credito[val]['cuotas'])
        #print(credito[val]['cuo_pagadas'])
'''

'''
# Sacar los datos del ciclo o hacer calculo para cumplirlo
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            print(total_credito)
            total_cuotas = credito[val]['cuotas']
            print(total_cuotas)
            cuotas_pagadas = credito[val]['cuo_pagadas']
            print(cuotas_pagadas)
            cuotas_mora = credito[val]['cuo_vencidas']
            print(cuotas_mora)
            num_cuota = 0
            while num_cuota < total_cuotas:
                num_cuota = num_cuota + 1
                print(num_cuota)
                vlr_cuota = total_credito/total_cuotas * num_cuota
                print(vlr_cuota)
                vlr_saldo = total_credito - vlr_cuota
                print(vlr_saldo)
                vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                print(vlr_interes)
                vlr_pagar = total_credito/total_cuotas + vlr_interes
                print(vlr_pagar)
                if num_cuota == cuotas_pagadas:
                    break
'''
'''
#Suma de los totales a pagar de acuerdo al número de cuotas pagadas --> TOTPAGADAS (solo lee el primer diccionario)
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        print(pos)
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            total_cuotas = credito[val]['cuotas']
            cuotas_pagadas = credito[val]['cuo_pagadas']
            cuotas_mora = credito[val]['cuo_vencidas']
            cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
            
            totpagados = 0
            num_cuota = 0
            while num_cuota < cuotas_pagadas:
                num_cuota = num_cuota + 1
                vlr_cuota = total_credito/total_cuotas * num_cuota
                vlr_saldo = total_credito - vlr_cuota
                vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                vlr_pagar = total_credito/total_cuotas + vlr_interes
                totpagados += vlr_pagar
            return round(totpagados , 2)
print(calcularInforme(creditos))

#Suma de los totales en MORA --> TOTVENCIDOS (solo lee el primer diccionario)
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            total_cuotas = credito[val]['cuotas']
            cuotas_pagadas = credito[val]['cuo_pagadas']
            cuotas_mora = credito[val]['cuo_vencidas']
            
            totvencidos = 0
            num_cuota = cuotas_pagadas
            while num_cuota < cuotas_pagadas + cuotas_mora:
                num_cuota = num_cuota + 1
                vlr_cuota = total_credito/total_cuotas * num_cuota
                vlr_saldo = total_credito - vlr_cuota
                vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                vlr_pagar = total_credito/total_cuotas + vlr_interes
                totvencidos += vlr_pagar
            return round(totvencidos , 2)
print(calcularInforme(creditos))

# Suma de los totales de las cuotas elaboradas --> TOTELABORADOS (solo lee el primer diccionario)
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            total_cuotas = credito[val]['cuotas']
            cuotas_pagadas = credito[val]['cuo_pagadas']
            cuotas_mora = credito[val]['cuo_vencidas']
            cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
            
            totalaborados = 0
            num_cuota = cuotas_pagadas + cuotas_mora
            while num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                num_cuota = num_cuota + 1
                vlr_cuota = total_credito/total_cuotas * num_cuota
                vlr_saldo = total_credito - vlr_cuota
                vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                vlr_pagar = total_credito/total_cuotas + vlr_interes
                totalaborados += vlr_pagar
            return round(totalaborados , 2)
print(calcularInforme(creditos))

#Aquí lee los dos diccionarios cuando no está con el WHILE
def calcularInforme(creditos : dict) -> list:
    for pos , dat in creditos.items():
        print(dat['credito'])
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            print(total_credito)
            total_cuotas = credito[val]['cuotas']
            print(total_cuotas)
            cuotas_pagadas = credito[val]['cuo_pagadas']
            print(cuotas_pagadas)
            cuotas_mora = credito[val]['cuo_vencidas']
            print(cuotas_mora)
            cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
            print(cuotas_elaboradas)
calcularInforme(creditos)
'''
'''
#Función realizada en tutoria 08/06/2021
def calcularInforme(creditos : dict) -> list:

    totpagados = 0
    totvencidos = 0
    totelaborados = 0

    for pos , dat in creditos.items():
        print(pos)
        credito = dat['credito']
        for val in range(len(credito)):
            total_credito = credito[val]['valor']
            total_cuotas = credito[val]['cuotas']
            cuotas_pagadas = credito[val]['cuo_pagadas']
            cuotas_mora = credito[val]['cuo_vencidas']
            cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
            vlr_cuota = total_credito/total_cuotas

            num_cuota = 0
            vlr_saldo = total_credito
            while num_cuota < total_cuotas:
                vlr_interes = vlr_saldo * credito[val]['interes']
                vlr_saldo = vlr_saldo - vlr_cuota
                vlr_pagar = vlr_cuota + vlr_interes
                if num_cuota < cuotas_pagadas:
                    totpagados += vlr_pagar
                if num_cuota >= cuotas_pagadas and num_cuota < cuotas_pagadas + cuotas_mora:
                    totvencidos += vlr_pagar
                if num_cuota >= cuotas_pagadas + cuotas_mora and num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                    totelaborados += vlr_pagar
                num_cuota = num_cuota + 1
    return (totpagados , totvencidos , totelaborados)

print(calcularInforme(creditos))

#Función reestructurada con Eduardo el 08/06/2021
def calcularInforme(creditos : dict) -> list:

    totpagados = 0
    totvencidos = 0
    totalaborados = 0

    for pos , dat in creditos.items():
        #id = pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2] (Aquí me hace la lectura de los dos diccionarios)
        print(id)
        credito = dat['credito']
        for val in range(len(credito)):
            if dat['est_credito'] == 'Pagado':
                pass
            else:
                total_credito = credito[val]['valor']
                total_cuotas = credito[val]['cuotas']
                cuotas_pagadas = credito[val]['cuo_pagadas']
                cuotas_mora = credito[val]['cuo_vencidas']
                cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
                
                num_cuota = 0
                while num_cuota < cuotas_pagadas:
                    num_cuota = num_cuota + 1
                    vlr_cuota = total_credito/total_cuotas * num_cuota
                    vlr_saldo = total_credito - vlr_cuota
                    vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                    vlr_pagar = total_credito/total_cuotas + vlr_interes
                    totpagados += vlr_pagar
                else:
                    num_cuota = cuotas_pagadas
                    while num_cuota < cuotas_pagadas + cuotas_mora:
                        num_cuota = num_cuota + 1
                        vlr_cuota = total_credito/total_cuotas * num_cuota
                        vlr_saldo = total_credito - vlr_cuota
                        vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                        vlr_pagar = total_credito/total_cuotas + vlr_interes
                        totvencidos += vlr_pagar
                    else:
                        num_cuota = cuotas_pagadas + cuotas_mora
                        while num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                            num_cuota = num_cuota + 1
                            vlr_cuota = total_credito/total_cuotas * num_cuota
                            vlr_saldo = total_credito - vlr_cuota
                            vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                            vlr_pagar = total_credito/total_cuotas + vlr_interes
                            totalaborados += vlr_pagar
    #lista = [id,(round(totpagados,2) , round(totvencidos,2) , round(totalaborados,2))] #Aquí no me los retorna
    lista = [pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2],(round(totpagados,2) , round(totvencidos,2) , round(totalaborados,2))]
    return(lista)

print(calcularInforme(creditos))
'''

'''
#Función donde se unen en un str pero tiene el problema de no correr el diccionario 1 al no haber sino un elemento en la lista
def calcularInforme(creditos : dict) -> list:

    totpagados = 0
    totvencidos = 0
    totalaborados = 0
    otro = list()

    for pos , dat in creditos.items():
        otro.append(pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2])
        credito = dat['credito']
        for val in range(len(credito)):
            if dat['est_credito'] == 'Pagado':
                pass
            else:
                total_credito = credito[val]['valor']
                total_cuotas = credito[val]['cuotas']
                cuotas_pagadas = credito[val]['cuo_pagadas']
                cuotas_mora = credito[val]['cuo_vencidas']
                cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
                
                num_cuota = 0
                while num_cuota < cuotas_pagadas:
                    num_cuota = num_cuota + 1
                    vlr_cuota = total_credito/total_cuotas * num_cuota
                    vlr_saldo = total_credito - vlr_cuota
                    vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                    vlr_pagar = total_credito/total_cuotas + vlr_interes
                    totpagados += vlr_pagar
                else:
                    num_cuota = cuotas_pagadas
                    while num_cuota < cuotas_pagadas + cuotas_mora:
                        num_cuota = num_cuota + 1
                        vlr_cuota = total_credito/total_cuotas * num_cuota
                        vlr_saldo = total_credito - vlr_cuota
                        vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                        vlr_pagar = total_credito/total_cuotas + vlr_interes
                        totvencidos += vlr_pagar
                    else:
                        num_cuota = cuotas_pagadas + cuotas_mora
                        while num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                            num_cuota = num_cuota + 1
                            vlr_cuota = total_credito/total_cuotas * num_cuota
                            vlr_saldo = total_credito - vlr_cuota
                            vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                            vlr_pagar = total_credito/total_cuotas + vlr_interes
                            totalaborados += vlr_pagar
    lista = [str(otro[0] + ':' + otro[1]),(round(totpagados,2) , round(totvencidos,2) , round(totalaborados,2))]
    return(lista)


print(calcularInforme(creditos))
'''
'''
#Función para ingresar al validador ---> Falla con las pruebas ocultas al dejar el ID_del cliente con estado 'Pagado'
def calcularInforme(creditos : dict) -> list:

    nuevo_credito = creditos.copy()
    totpagados = 0
    totvencidos = 0
    totalaborados = 0
    otro = list()

    for pos , dat in creditos.items():
        otro.append(pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2])
        credito = dat['credito']
        for val in range(len(credito)):
            if dat['est_credito'] !='Pagado':
                total_credito = credito[val]['valor']
                total_cuotas = credito[val]['cuotas']
                cuotas_pagadas = credito[val]['cuo_pagadas']
                cuotas_mora = credito[val]['cuo_vencidas']
                cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
                
                num_cuota = 0
                while num_cuota < cuotas_pagadas:
                    num_cuota = num_cuota + 1
                    vlr_cuota = total_credito/total_cuotas * num_cuota
                    vlr_saldo = total_credito - vlr_cuota
                    vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                    vlr_pagar = total_credito/total_cuotas + vlr_interes
                    totpagados += vlr_pagar
                else:
                    num_cuota = cuotas_pagadas
                    while num_cuota < cuotas_pagadas + cuotas_mora:
                        num_cuota = num_cuota + 1
                        vlr_cuota = total_credito/total_cuotas * num_cuota
                        vlr_saldo = total_credito - vlr_cuota
                        vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                        vlr_pagar = total_credito/total_cuotas + vlr_interes
                        totvencidos += vlr_pagar
                    else:
                        num_cuota = cuotas_pagadas + cuotas_mora
                        while num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                            num_cuota = num_cuota + 1
                            vlr_cuota = total_credito/total_cuotas * num_cuota
                            vlr_saldo = total_credito - vlr_cuota
                            vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                            vlr_pagar = total_credito/total_cuotas + vlr_interes
                            totalaborados += vlr_pagar
            else:
                nuevo_credito.pop(pos)

    lista = [':'.join(otro),(round(totpagados,2) , round(totvencidos,2) , round(totalaborados,2))]
    return(lista)

print(calcularInforme(creditos))
'''

#Función WHILE - ELSE planteada para el VALIDADOR --> CORRECTO :):):):):):):):):):):):):):)
def calcularInforme(creditos : dict) -> list:

    totpagados = 0
    totvencidos = 0
    totalaborados = 0
    otro = list()

    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            if dat['est_credito'] !='Pagado':
                otro.append(pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2])
                total_credito = credito[val]['valor']
                total_cuotas = credito[val]['cuotas']
                cuotas_pagadas = credito[val]['cuo_pagadas']
                cuotas_mora = credito[val]['cuo_vencidas']
                cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
                
                num_cuota = 0
                while num_cuota < cuotas_pagadas:
                    num_cuota = num_cuota + 1
                    vlr_cuota = total_credito/total_cuotas * num_cuota
                    vlr_saldo = total_credito - vlr_cuota
                    vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                    vlr_pagar = total_credito/total_cuotas + vlr_interes
                    totpagados += vlr_pagar
                else:
                    num_cuota = cuotas_pagadas
                    while num_cuota < cuotas_pagadas + cuotas_mora:
                        num_cuota = num_cuota + 1
                        vlr_cuota = total_credito/total_cuotas * num_cuota
                        vlr_saldo = total_credito - vlr_cuota
                        vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                        vlr_pagar = total_credito/total_cuotas + vlr_interes
                        totvencidos += vlr_pagar
                    else:
                        num_cuota = cuotas_pagadas + cuotas_mora
                        while num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                            num_cuota = num_cuota + 1
                            vlr_cuota = total_credito/total_cuotas * num_cuota
                            vlr_saldo = total_credito - vlr_cuota
                            vlr_interes = (vlr_saldo + total_credito/total_cuotas) * credito[val]['interes']
                            vlr_pagar = total_credito/total_cuotas + vlr_interes
                            totalaborados += vlr_pagar

    lista = [':'.join(otro),(round(totpagados,2) , round(totvencidos,2) , round(totalaborados,2))]
    return(lista)

print(calcularInforme(creditos))

#Función WHILE - IF Santiago ---> CORRECTO
def calcularInforme(creditos : dict) -> list:
    
    totpagados = 0
    totvencidos = 0
    totelaborados = 0
    otro = list()

    for pos , dat in creditos.items():
        credito = dat['credito']
        for val in range(len(credito)):
            if dat['est_credito'] !='Pagado':
                otro.append(pos + ':' + dat['nombres'][0:2] + ':' + dat['apellidos'][0:2])
                total_credito = credito[val]['valor']
                total_cuotas = credito[val]['cuotas']
                cuotas_pagadas = credito[val]['cuo_pagadas']
                cuotas_mora = credito[val]['cuo_vencidas']
                cuotas_elaboradas = total_cuotas - cuotas_pagadas - cuotas_mora
                vlr_cuota = total_credito/total_cuotas

                num_cuota = 0
                vlr_saldo = total_credito
                while num_cuota < total_cuotas:
                    vlr_interes = vlr_saldo * credito[val]['interes']
                    vlr_saldo = vlr_saldo - vlr_cuota
                    vlr_pagar = vlr_cuota + vlr_interes
                    if num_cuota < cuotas_pagadas:
                        totpagados += vlr_pagar
                    if num_cuota >= cuotas_pagadas and num_cuota < cuotas_pagadas + cuotas_mora:
                        totvencidos += vlr_pagar
                    if num_cuota >= cuotas_pagadas + cuotas_mora and num_cuota < cuotas_pagadas + cuotas_mora + cuotas_elaboradas:
                        totelaborados += vlr_pagar
                    num_cuota = num_cuota + 1

    lista = [':'.join(otro),(round(totpagados,2) , round(totvencidos,2) , round(totelaborados,2))]
    return(lista)

print(calcularInforme(creditos))

