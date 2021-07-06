'''
 1A - El objetivo es generar un reporte final de notas que tenga la siguiente estructura
 1B - El estudiante {nombre} obtuvo las siguientes notas: matemáticas: {nota}, física: {nota} y química {nota}

 2A - Desarrollar un algoritmo en el cual se tenga en cuenta el porcentaje de peso en la nota final de las calificaciones individuales
 2B - Se podría desarrollar de dos formas:
       *** (Nm1 * 0.25) + (Nm2 * 0.25)
       *** ((Nm1 + Nm2)/2) * 0.5

3A - Desarrollar una prueba para verificar el planteamiento y corregir en caso que sea necesario
'''

# OPCIÓN A - FALLIDA AL SER TRES FUNCIONES SEPARADAS Y EN EL VALIDADOR SOLO PERMITIA UNA

'''
# Las entradas de las notas se crearan mediante la declaración de una variable de tipo DICTIONARY
var_est = {'nombre':'Ricardo', #Nombre del alumno
            'mq1' : '75', #Nota quiz 1 matemáticas
            'mq2' : '60', #Nota quiz 2 matemáticas
            'mp1' : '80', #Nota parcial 1 matemáticas
            'fq1' : '75', #Nota quiz 1 física
            'fq2' : '60', #Nota quiz 2 física
            'fq3' : '60', #Nota quiz 3 física
            'fp1' : '80', #Nota parcial 1 física
            'qt1' : '75', #Nota trabajo 1 química
            'qt2' : '60', #Nota trabajo 2 química
            'qq1' : '60', #Nota quiz 1 química
            'qq2' : '80', #Nota quiz 2 química
            'qp1' : '50', #Nota parcial 1 química
}

# Ahora se debe crear tres funciones para sacar la definitiva de las materias del estudiantes
def est_mat(notam : dict): #Nota final matemáicas por ponderación
    final = int(notam['mq1']) * 0.25 + int(notam['mq2']) * 0.25 + int(notam['mp1']) * 0.50
    final = round(final,2)
    return final

def est_fis(notaf : dict): #Nota final física por ponderación
    final = ((sum((int(notaf['fq1']) , int(notaf['fq2']) , int(notaf['fq3']))) / 3) * 0.45) + int((notaf['fp1']))*0.55
    final = round(final,2)
    return final

def est_qui(notaq : dict): #Nota final química por ponderación
    final = (sum((int(notaq['qt1']) , int(notaq['qt2']))) / 2) * 0.30 + (sum((int(notaq['qq1']) , int(notaq['qq2']))) / 2) * 0.20 + int(notaq['qp1']) * 0.50
    final = round(final,2)
    return final

#print(est_mat(var_est))
#print(est_fis(var_est))
#print(est_qui(var_est))

# Concatenar los string con los cálculos de las variables para resolver el problema
#print("El estudiante {} obtuvo las siguientes notas:\n Matemácticas --> ({})\n Física --------> ({})\n Química -------> ({})".format(var_est['nombre'] , est_mat(var_est) , est_fis(var_est) , est_qui(var_est)))

#print("El estudiante {} obtuvo las siguientes notas: matamáticas: {}, física {}, química {}".format(var_est['nombre'] , est_mat(var_est) , est_fis(var_est) , est_qui(var_est)))

def calcularNotas(notam : dict):
    return("El estudiante {} obtuvo las siguientes notas: matamáticas: {}, física {}, química {}".format(var_est['nombre'] , est_mat(var_est) , est_fis(var_est) , est_qui(var_est)))


# Salida exacta al texto del reto
#print("El estudiante {} obtuvo las siguientes notas: matamáticas: {}, física {}, química {}".format(var_est['nombre'] , est_mat(var_est) , est_fis(var_est) , est_qui(var_est)))

#print(calcularNotas({"nombre": "Ricardo","mqui1":75,"mqui2":60,"mpar1":80,"fqui1":75,"fqui2":60,"fqui3":60,"fpar1":80,"qtra1":75,"qtra2":60,"qqui1":60,"qqui2":80,"qpar1":50}))
'''


#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------


# OPCIÓN B - Una sola función realiza todo
# Las entradas de las notas se crearan mediante la declaración de una variable de tipo DICTIONARY
estudiante = {'nombre':'Ricardo', #Nombre del alumno
            'mqui1' : '75', #Nota quiz 1 matemáticas
            'mqui2' : '60', #Nota quiz 2 matemáticas
            'mpar1' : '80', #Nota parcial 1 matemáticas
            'fqui1' : '75', #Nota quiz 1 física
            'fqui2' : '60', #Nota quiz 2 física
            'fqui3' : '60', #Nota quiz 3 física
            'fpar1' : '80', #Nota parcial 1 física
            'qtra1' : '75', #Nota trabajo 1 química
            'qtra2' : '60', #Nota trabajo 2 química
            'qqui1' : '60', #Nota quiz 1 química
            'qqui2' : '80', #Nota quiz 2 química
            'qpar1' : '50', #Nota parcial 1 química
}

def calcularNotas(estudiante : dict) -> str: #Todos los calculos dentro de la misma función
    mfinal = round((int(estudiante['mqui1'])* 0.25 + int(estudiante['mqui2']) * 0.25 + int(estudiante['mpar1']) * 0.50),2) #Cálculo matemáticas
    ffinal = round((((sum((int(estudiante['fqui1']) , int(estudiante['fqui2']) , int(estudiante['fqui3']))) / 3) * 0.45) + int((estudiante['fpar1']))*0.55),2) #Cálculo física
    qfinal = round(((sum((int(estudiante['qtra1']) , int(estudiante['qtra2']))) / 2) * 0.30 + (sum((int(estudiante['qqui1']) , int(estudiante['qqui2']))) / 2) * 0.20 + int(estudiante['qpar1']) * 0.50),2) #Cálculo química
    return "El estudiante " + estudiante['nombre'] + " obtuvo las siguientes notas: matamáticas: " + str(mfinal) + ", física " + str(ffinal) + ", química " + str(qfinal) #Concatenar la oración para validación con los resultados de los calculos anteriores y aquí es donde ya está la respuesta cuando se valide
    pass #No hacer nada en caso que no funcione

print(calcularNotas({"nombre": "Ricardo","mqui1":75,"mqui2":60,"mpar1":80,"fqui1":75,"fqui2":60,"fqui3":60,"fpar1":80,"qtra1":75,"qtra2":60,"qqui1":60,"qqui2":80,"qpar1":50})) #Orden que da la plataforma para validar lo realizado