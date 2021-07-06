# Reto 2 - Clasificación de síntomas para diagnóstico de enfermedades

#(1) - Crear un diccionario que permita la entrada de un conjunto de datos
'''
Método A
Se pensó en esta forma que permita introducir los valores con INPUT pero no funcionó porque no se le dió la orden de qué introducir
#paciente = dict(id_diagnostico = input() , diag_ta = input() , diag_pa = input() , diag_do = input() , diag_dg = input() , diag_ca = input())

El siguiente si funciono
paciente = dict(id_1 = input("Ingrese el id paciente: "))
print(paciente)
'''

'''
Método B
Craer variables con INPUT para luego agregarlas al diccionario
id_1 = input("Ingrese el id paciente: ")
paciente = dict(id_1 = id_1)
print(paciente)
'''

'''
Método C es el más fácil porque es crear el diccionario con las variables predefinidas e irlas cambiando
paciente = dict(id_diagnostico = 'd-001' , diag_ta = 'Si' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'Si' , diag_ca = 'Si')
'''

#Diccionario con el método A (facilmente remplazable luego por el método C)
paciente = dict(id_diagnostico = input('Identificador diagnostico nuevo paciente: ') , #Ingreso de los parametros de entrada en diccionario con los mismos nombres dados
                diag_ta = input('Síntoma temperatura alta (‘Si’ / ‘No’): ') , #Parametro 1 para diagnóstico
                diag_pa = input('Síntoma presión alta (‘Si’ / ‘No’): ') , #Parametro 2 para diagnóstico
                diag_do = input('Síntoma dolor oído (‘Si’ / ‘No’): ') , #Parametro 3 para diagnóstico
                diag_dg = input('Síntoma dolor de garganta (‘Si’ / ‘No’): ') , #Parametro 4 para diagnóstico
                diag_ca = input('Síntoma cansancio (‘Si’ / ‘No’): ')) #Parametro 5 para diagnóstico

#(2) - Creación de función que sería un árbol de decisión en CASCADA + ANIDADO
'''
'''
#Se probó una función aparte que dá correcto
a = 1
b = 2
c = 3

def eva1(a , b , c):
    if(a == 1):
        if(b == 2):
            if(c == 3):
                return('A + B + C')
    else:
        return('WOM')

eva2 = eva1(1 , 2 , 3)
print(eva2)
'''
'''
def diagSintoma(paciente : dict) -> dict:
    if(paciente['diag_ta'] == 'Si'):
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_ca'] == 'Si'):
                        return('Covid 19') #1Si + 2Si + 3Si + 4Si + 5Si
                    else:
                        return('Presencia de síntomas a') #1Si + 2Si + 3Si + 4Si + 5No
                else:
                    return('Presencia de síntomas b') #1Si + 2Si + 3Si + 4No
            else:
                return('Presencia de síntomas c') #1Si + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'No'):
                if(paciente['diag_dg'] == 'No'):
                    return('Presencia de síntomas f') #1Si + 2No + 3No + 4No
                else:
                    if(paciente['diag_ca'] == 'No'):
                        return('Presencia de síntomas e') #1Si + 2No + 3No + 4Si + 5No
                    else:
                        return('Gripa') #1Si + 2No + 3No + 4Si + 5Si
            else:
                return('Presencia de síntomas d') #1Si + 2No + 3Si
    else:
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_ca'] == 'Si'):
                        return('Presencia de síntomas g') #1No + 2Si + 3Si + 4Si + 5Si
                    else:
                        return('Otitis') #1No + 2Si + 3Si + 4Si + 5No
                else:
                    return('Presencia de síntomas h') #1No + 2Si + 3Si + 4No
            else:
                return('Presencia de síntomas i') #1No + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'Si' or paciente['diag_dg'] == 'Si' or paciente['diag_ca'] == 'Si'):
                return('Presencia de síntomas j') #1No + 2No + (3Si o 4Si o 5Si)
            else:
                return('No tiene síntomas')
    pass

#Parámetros a evaluar
paciente = dict(id_diagnostico = 'd-001' , diag_ta = 'No' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'No' , diag_ca = 'No')

#Pasandolos en la función para tener el 'RESULTADO'
res_eva = diagSintoma(paciente)

#Buscar el 'estado' con una función
def f():
    if(res_eva == 'Presencia de síntomas j' or res_eva == 'No tiene síntomas'):
        return(False)
    else:
        return(True)

#Evaluar la función
est_eva = f()

#Agregar los resultados a un diccionario
salida = dict(id_diagnostico = paciente['id_diagnostico'] , resultado = res_eva , estado = est_eva)
print(salida)


#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

def result_enf(paciente : dict) -> dict:
    if(paciente['diag_ta'] == 'Si'):
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_dc'] == 'Si'):
                        return('Covid 19') #1Si + 2Si + 3Si + 4Si + 5Si
                    else:
                        return('Presencia de síntomas') #1Si + 2Si + 3Si + 4Si + 5No
                else:
                    return('Presencia de síntomas') #1Si + 2Si + 3Si + 4No
            else:
                return('Presencia de síntomas') #1Si + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'No'):
                if(paciente['diag_dg'] == 'No'):
                    return('Presencia de síntomas') #1Si + 2No + 3No + 4No
                else:
                    if(paciente['diag_dc'] == 'No'):
                        return('Presencia de síntomas') #1Si + 2No + 3No + 4Si + 5No
                    else:
                        return('Gripa') #1Si + 2No + 3No + 4Si + 5Si
            else:
                return('Presencia de síntomas') #1Si + 2No + 3Si
    else:
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_dc'] == 'Si'):
                        return('Presencia de síntomas') #1No + 2Si + 3Si + 4Si + 5Si
                    else:
                        return('Otitis') #1No + 2Si + 3Si + 4Si + 5No
                else:
                    return('Presencia de síntomas') #1No + 2Si + 3Si + 4No
            else:
                return('Presencia de síntomas') #1No + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'Si' or paciente['diag_dg'] == 'Si' or paciente['diag_dc'] == 'Si'):
                return('Presencia de síntomas') #1No + 2No + (3Si o 4Si o 5Si)
            else:
                return('No tiene síntomas')
    pass

def estad_pn():
    if(result_enf(paciente) == 'Presencia de síntomas' or result_enf(paciente) == 'No tiene síntomas'):
        return(False)
    else:
        return(True)

def diagSintoma(paciente : dict) -> dict:
    salida = dict(id_diagnostico = paciente['id_diagnostico'] , resultado = result_enf(paciente) , estado = estad_pn())
    return(salida)

paciente = dict(id_diagnostico = 'd-001' , diag_ta = 'Si' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'Si' , diag_dc = 'Si')
print(diagSintoma(paciente))

paciente = dict(id_diagnostico = 'd-002' , diag_ta = 'Si' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'No' , diag_dc = 'No')
print(diagSintoma(paciente))

paciente = dict(id_diagnostico = 'd-003' , diag_ta = 'No' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'No' , diag_dc = 'No')
print(diagSintoma(paciente))

paciente = dict(id_diagnostico = 'd-004' , diag_ta = 'Si' , diag_pa = 'No' , diag_do = 'No' , diag_dg = 'Si' , diag_dc = 'Si')
print(diagSintoma(paciente))

print(diagSintoma({'id_diagnostico':'d-001','diag_ta':'Si','diag_pa':'No','diag_do':'No','diag_dg':'Si','diag_dc':'Si'}))

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------RESPUESTA CORRECTA----------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------


#Se crea una sola función
#En los return no debe lanzar un STR sino un DICT con los valores establecidos en el enunciado
#El parámetro diag_ca está mal escrito ya que lo valida como diag_dc

def diagSintoma(paciente : dict) -> dict:
    if(paciente['diag_ta'] == 'Si'):
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_dc'] == 'Si'):
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Covid 19' , estado = True)) #1Si + 2Si + 3Si + 4Si + 5Si
                    else:
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2Si + 3Si + 4Si + 5No
                else:
                    return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2Si + 3Si + 4No
            else:
                return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'No'):
                if(paciente['diag_dg'] == 'No'):
                    return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2No + 3No + 4No
                else:
                    if(paciente['diag_dc'] == 'No'):
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2No + 3No + 4Si + 5No
                    else:
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Gripa' , estado = True)) #1Si + 2No + 3No + 4Si + 5Si
            else:
                return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1Si + 2No + 3Si
    else:
        if(paciente['diag_pa'] == 'Si'):
            if(paciente['diag_do'] == 'Si'):
                if(paciente['diag_dg'] == 'Si'):
                    if(paciente['diag_dc'] == 'Si'):
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1No + 2Si + 3Si + 4Si + 5Si
                    else:
                        return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Otitis' , estado = True)) #1No + 2Si + 3Si + 4Si + 5No
                else:
                    return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1No + 2Si + 3Si + 4No
            else:
                return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1No + 2Si + 3No
        else:
            if(paciente['diag_do'] == 'Si' or paciente['diag_dg'] == 'Si' or paciente['diag_dc'] == 'Si'):
                return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'Presencia de síntomas' , estado = False)) #1No + 2No + (3Si o 4Si o 5Si)
            else:
                return(dict(id_diagnostico = paciente['id_diagnostico'] , resultado = 'No tiene síntomas' , estado = False)) #1No + 2No + 3No + 4No + 5No
    pass

print(diagSintoma({'id_diagnostico':'d-001','diag_ta':'Si','diag_pa':'No','diag_do':'No','diag_dg':'Si','diag_dc':'Si'}))
print(diagSintoma({'id_diagnostico':'d-001','diag_ta':'Si','diag_pa':'Si','diag_do':'Si','diag_dg':'Si','diag_dc':'Si'}))