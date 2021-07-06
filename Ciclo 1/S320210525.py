diccionarioEstudiantes = {
    'E3454fdf' : {
        'nombres' : 'Laura',
        'apellidos' : 'Jaramillo',
        'acudientes' : [
            {
                'Acudiente' : 'Andrea',
                'suplente' : 'Juan'
            }
        ],
        'promedio' : 5.0
    },
    'Egg56dfg' : {
        'nombres' : 'Samir',
        'apellidos' : 'Gomez',
        'acudientes' : [
            {
                'Acudiente' : 'Alejandro',
                'suplente' : 'Sofia'
            }    
        ],
        'promedio' : 4.0
    },
    'FHT43523' : {
        'nombres' : 'Sara',
        'apellidos' : 'Cabrera',
        'acudientes' : [
            {
                'Acudiente' : 'Carlos',
                'suplente' : 'Amparo'
            }    
        ],
        'promedio' : 5.0
    },
    'Z4edkdf' : {
        'nombres' : 'Iván',
        'apellidos' : 'Arcila',
        'acudientes' : [
            {
                'Acudiente' : 'Esposa',
                'suplente' : ''
            }
        ],
        'promedio' : 3.0
    }
}

print(diccionarioEstudiantes)

for pos , dat in diccionarioEstudiantes.items():
    #print(pos) #Imprime el ID del estudiante
    #print(dat) #Imprime los datos de los diccionarios
    #print(dat['nombres']) #Imprime los nombres de los subdiccionarios
    print(dat['acudientes']) #Imprime una lista de los diciconarios de los acudientes

'''
#Forma A --> Obtener solo los suplentes
for pos , dat in diccionarioEstudiantes.items():
    for acud in range(len(dat['acudientes'])):
        print('Suplentes : ' , dat['acudientes'][0]['suplente'])
'''
'''
#Forma B --> Obtener solo los suplentes
for pos , dat in diccionarioEstudiantes.items():
    for pos2 , dat2 in enumerate(dat['acudientes']):
        print('Suplentes : ' , dat['acudientes'][0]['suplente'])
'''

#Forma C --> Obtener solo los suplentes
for pos , dat in diccionarioEstudiantes.items():
    acudientes = dat['acudientes']
    for acud in range(len(acudientes)):
        print('Suplentes: ' , acudientes[acud]['suplente'])


#Mostrar ID con promedios mayores de 4 y eliminar los inferiores
nuevosEstudiantes = diccionarioEstudiantes.copy()

for idestudiantes , info in nuevosEstudiantes.items():
    promedio = info['promedio']
    if promedio > 4:
        print(info['nombres'] , ' ' , info['apellidos'])
    else:
        diccionarioEstudiantes.pop(idestudiantes)
    
print(diccionarioEstudiantes)

#Los acudientes ahora estarán en forma de lista
diccionarioEstudiantes2 = {
    'E3454fdf' : {
        'nombres' : 'Laura',
        'apellidos' : 'Jaramillo',
        'acudientes' : ['Andrea' , 'Juan'],
        'promedio' : 5.0
    },
    'Egg56dfg' : {
        'nombres' : 'Samir',
        'apellidos' : 'Gomez',
        'acudientes' : ['Alejandro' , 'Sofia'],
        'promedio' : 4.0
    },
    'FHT43523' : {
        'nombres' : 'Sara',
        'apellidos' : 'Cabrera',
        'acudientes' : ['Carlos', 'Amparo'],
        'promedio' : 5.0
    },
    'Z4edkdf' : {
        'nombres' : 'Iván',
        'apellidos' : 'Arcila',
        'acudientes' : ['Esposa', ''],
        'promedio' : 3.0
    }
}

print(diccionarioEstudiantes2)

nuevo_dict = diccionarioEstudiantes2.copy()

for id_estudiante , info in nuevo_dict.items():
    #print(info['acudientes'])
    for x in range(len(info['acudientes'])):
        print(info['acudientes'][x])

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#Ejercicio CRUD ||| CREATE-READ-UPDATE-DELETE |||

# Primero se crea un diccionario
tareas = {
    '01' : {
        'descripcion' : 'ir a mercar',
        'estado' : 'pendiente',
        'tiempo' : 60
    },
    '02' : {
        'descripcion' : 'estudiar',
        'estado' : 'pendiente',
        'tiempo' : 180
    },
    '03' : {
        'descripcion' : 'hacer ejercicio',
        'estado' : 'pendiente',
        'tiempo' : 50
    }
}

#CREATE (interfaz básica)
def create(tareas , identificador , nuevatarea):
    tareas[identificador] = nuevatarea
    return tareas

def createTarea(t):
    print('\n -> Adicionar la tarea')

    identificador = str(input('Ingrese el identificador de la tarea: '))
    descripcion = str(input('Ingrese la descripción de la tarea: '))
    estado = str(input('Ingrese el estado de la tarea: '))
    tiempo = str(input('Ingres el tiempo de realización de la tarea: '))

    tareasNuevas = {
        'descripcion' : descripcion,
        'estado' : estado,
        'tiempo' : tiempo
    }

    tareas = create(t , identificador , tareasNuevas)

def read(tareas):
    for identificador , tarea in tareas.items():
        print(identificador, ' - ' , end='')
        for nombre_atributo , atributo in tarea.items():
            print(atributo , ' , ' , end='')

def estaElemento(identificador , tareas):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

def update(tareas):
    identificador = str(input('Ingrese el identificador de la tarea para modificar: ')) #Solicitar al usuario el identificador

    if estaElemento (identificador , tareas): #Revisar si se encuentra el elemento solicitado --> Proceder a actualizar
        nuevaDescripcion = str(input('Nueva descripción: ')) #Modificar los campos de interes
        if nuevaDescripcion:
            tareas[identificador]['descripcion'] = nuevaDescripcion
        nuevoEstado = str(input('Nuevo estado: '))
        if nuevoEstado:
            tareas[identificador]['estado'] = nuevoEstado
        nuevoTiempo = input('Nuevo tiempo: ')
        if nuevoTiempo:
            tareas[identificador]['tiempo'] = nuevoTiempo
    else:
        print('No ha sido encontrada la tarea!')

def delete(tareas):
    identificador = str(input('Ingrese el identificador de la tarea a eliminar: ')) #Solicitar al usuario el identificador

    conjuntoIdentificadores = set(tareas.keys()) #Extraer de la base de datos (contenedor) los identificadores
    if identificador in conjuntoIdentificadores: #Revisar si se encuentra el elemento solicitado
        tareas.pop(identificador) #Proceder a eliminar
    else:
        print('No ha sido encontrada la tarea para eliminar')

opcion = 0
while opcion != 5:
    print('---Aplicación del CRUD tareas pendientes---\n')
    print(' 1: Agregar Tarea \n')
    print(' 2: Consultar Tarea \n')
    print(' 3: Actualizar Tarea \n')
    print(' 4: Eliminar Tarea \n')
    print(' 5: Salir\n')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        createTarea(tareas)
    elif opcion == 2:
        read(tareas)
    elif opcion == 3:
        update(tareas)
    elif opcion == 4:
        delete(tareas)
        
print(tareas)