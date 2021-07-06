'''
Operaciones aritméticas +-*/%//
Operaciones lógicas AND OR NOT
Operaciones relacionales < == (is) > <= >= --> Diferente != (is not)
Operaciones alfanumericas
'''

# Mezclar todos los operadores
var_num = 5
if var_num % 2 == 0 or var_num % 3 == 0:
    print("Correcto")
else:
    print("Incorrecto")

# Determinar si un número es par o impar
var_num = 11
if var_num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Determinar si un número es primo (Debería ser dividiendo por todos los números) No se resolvió AQUÍ
var_num = 8
if var_num % var_num == 0:
    print("El número es primo")
else:
    print("El número no es primo")

# Usar la función TRY/EXCEPT para arrojar un mensaje predefinido en caso de un error
# Calculadora de °F a °C
temp_f = input("Ingrese la temperatura en grados Fahrenheit: ")
try:
    fahr = float(temp_f)
    celsius = (fahr - 32) * 5/9
    print(celsius)
except:
    print("Ingrese un número de nuevo: ")

# Pasamos ahora a diccionarios
# Diccionario vacio
dicc = {}

# Diccionario con valores
diccionario = {'total' : 115.15} #Ingresa un valor
print(diccionario)

otrodiccionario = {'Nombre' : 'Fernando' , 'Apellido' : 'Toro'} #Ingresa dos valores
print(otrodiccionario)

diccionario = {'total' : 55 , 'descuento' : True , 'subtotal' : "15"} #Ingresa valores de diferente tipo
print(diccionario)

diccionario = {'nombre' : 5 + 2 , 'telefono' : 3213387734 , 'edad' : 38 , 'ciudad' : 'pereira'} #Ingresa operaciones en los valores
print(diccionario)

diccionario = dict(total = 55 , descuento = True , subtotal = 15) # Ingresa un diccionario con la función DICT
print(diccionario)

diccionario = {'total' : 55 , 10 : 'curso python' , 2.0 : True} # Los campos también pueden ser otro tipo de datos
print(diccionario)

# Tener un diccionario dentro de otro deccionario
usuario = { #primer diccionario
    'nombre' : 'Carlos' ,
    'edad' : 22 ,
    'curso' : 'curso de python' ,
    'skill' : { #segundo diccionario
        'programacion' : True ,
        'base_de_datos' : True
    },
    'n_medallas' : 10
}

print(usuario)
print(usuario['curso'])
print(usuario['skill'])
print(usuario['skill']['programacion'])

# Agregar o modificar los espacios de un diccionario
nuevo = dict()
nuevo['marca'] = 'mazda'
print(nuevo)

nuevo['marcas'] = 'audi'
print(nuevo)

nuevo['marca'] = 'lamborgini'
print(nuevo)

# Obtener todos los valores con método KEYS/VALUES
nuevo_dicc = {'Eduardo' : 1 , 'Fernando' : 2 , 'Uriel' : 3 , 'Rafael' : 4}
print(nuevo_dicc.keys()) #Arroja todos los espacios de almacenamiento de datos
print(nuevo_dicc.values()) #Arroja todos los valores del diccionario

#print(nuevo_dicc.clear()) #Método CLEAR - Limpia el diccionario borrando todo

otro_dicc = nuevo_dicc.copy() # Método COPY - Copia la información de un diccionario a otro
print(otro_dicc)

#Usar método FROMKEYS a partir de una tupla para crear un diccionario
secuencia = ('python' , 'zope' , 'plone')
version = dict.fromkeys(secuencia) #Sino se coloca otro argumento aparecerá NONE
print(version)
version = dict.fromkeys(secuencia , 1.0) #Si coloco un argumento me aparecerá el mismo para los tres espacios
print(version)

#Usar método GET para mostrar un valor del diccionario
print(version.get('zope')) #Extrae 1.0 del zope

#Usar método ITEMS
print(version.items()) #Arroja los item/valor en forma de tuplas

#Usar método POP para remover un par
version.pop('zope')
print(version)

#Agregar un diccionario a otro con método UPDATES
versiones = dict(python = 39 , zope = 3.5 , plone = 5.1)
print(versiones)
version_adic = dict(django = 4.0)
print(version_adic)
versiones.update(version_adic)
print(versiones)

#Cantidad de espacios del diccionario función LEN
print(len(versiones))

#Otra forma de remover un par con DEL
del versiones['zope']
print(versiones)

#____________________________________________________________________________________________________________
#____________________________________________________________________________________________________________
#_____________________________________CLASE DE STRING TEÓRICA________________________________________________

#Indices o posiciones
fruta = 'fresa' #P0:f - P1:r - P2:e P3:s P4:a (INDICE debe ser un número entero)
letra = fruta[0] #Extrae la letra de la posición cero
print(letra) #--> F
print(fruta[1]) #--> R

#Len
fruta = 'banana'
print(len(fruta))

longitud = len(fruta) #Logitud cadena de texto
ultima_letra = fruta[longitud - 1] #Ubica la longitud - 1 (si se deja solo da error teniendo en cuenta que la posición 6 no existe)
print(ultima_letra) #Última letra es a

print(fruta[-6]) #Indices negativos ubican en retroceso P-1:a - P-2:n - P-3:a - P-4:n - P-5:a - P-6:b

#Rebanadas o trozos de texto
s = "Monty Python"

print(s[0:5])
print(s[6:11]) #El operador devuelve la parte de la cadena del "n-ésimo" carácter "m-ésimo" al carácter, incluyendo el primero pero excluyendo el último [n,m).

fruta = 'banana'
print(fruta[:3]) #BAN
print(fruta[3:]) #ANA
print(fruta[3:3]) #''
print(fruta[:]) #banana

#Los STR son inmutables (no se pueden cambiar una cadena existente --> Lo máximo es crear una nueva pero como variante)

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

#Operador IN (da verdadero si la cadena 1 está en la cadena 2 --> se parece a un BUSCAR en Excel)
print('a' in 'banana')
print('ola' in 'banana')
print('ana' in 'banana')

#Comparación de strings
palabra = 'fresa'
if palabra == 'fresa':
    print('La palabra es FRESA')

palabra = 'fresa'
if palabra < 'banana':
    print('La palabra ' + palabra + ' está antes de banana')
elif palabra > 'banana':
    print('La palabra ' + palabra + ' está despues de banana')
else:
    print('La palabra ' + palabra + ' es banana') #Las mayusculas vienen primero que las minisculas (Fresa != fresa)
    
#MÉTODOS es lo que se le pone a una cadena despues del punto cap.upper para que realice una acción en lugar de definir una FUNCIÓN
palabra = 'banana'
palabra_nueva = palabra.upper() # UPPER sirve para convertir en MAYUS la palabra. Estos parentesis vacios indican que no se ingresa ningún parametro
print(palabra_nueva)

index = palabra.find('a') #FIND sirve para buscar dentro de un str
print(index) #Letra a en palabra
print(palabra.find('na')) #Silaba  na en palabra
print(palabra.find('na' , 3)) #Silaba na en palabra a partir de la tercera posición empieza a buscar

linea = '   co lom bia       '
print(linea.strip()) #STRIP elimina espacios en blanco antes y despues del str

linea = 'Qué tengas un buen día'
print(linea.startswith('Qué')) #STARSWITH valida que empiece una frase con una palabra determinada TRUE
print(linea.startswith('qué')) #False al ser minuscula
print(linea.lower().startswith('qué')) #Forzar para que se vuelva minuscula y coincida (validación)

#Analizar los string
palabra = 'De stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008'
longitud = len(palabra) #Longitud de la cadena de texto (no me sirvió para nada)
inicio = palabra.find('@') #Posición en que inicia @
extrae = palabra[inicio + 2 : inicio + 11] #A partir de esa posición ubico el inicio y final de corte
print(extrae)

palabra = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
inicio = palabra.find('@') #ubica el inicio
fin = palabra.find(' ', inicio) #ubica el final
extrae = palabra[inicio + 1 : fin] #extrae el pedazo
print(extrae)

#Operador de formatos
camellos = 42
print('%d' %camellos) 
print('He visto %a cammellos' %camellos) #Permite ingresar el dato de una variable como formato y no como variable

#Carecteres especiales
# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
cadena = "Hola\nMundo"  
print(cadena)

# Saldrá una única línea en pantalla y la \ y la n será visibles como caracteres normales.
cadena2 = r"Hola\nMundo"
print(cadena2)

#Contar número de veces --> COUNT
cadena = "un uno, un dos, un tres"
print(cadena.count("un"))        # Saca 4, hay 4 "un" en cadena.
print(cadena.count("un",10))     # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
print(cadena.count("un",0,10))   # Saca 3, hay 3 "un" entre la posición 0 y la 10.

#Remplazar caracter en cadena de texto REPLACE
cadena = "un uno, un dos, un tres"
print(cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
print(cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"

#FORMAT() para construir cadenas de texto
# saca "El valor es 12
print("El valor es {}".format(12))

# saca "El valor es 12.3456
print("El valor es {}".format(12.3456))

# Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# y así sucesivamente.
# saca "Los valores son 1, 2 y 3"
print("Los valores son {}, {} y {}".format(1,2,3))

# Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# {0} es el primer parámetro de format.
# saca "Los valores son 3, 2 y 1"
print("Los valores son {2}, {1} y {0}".format(1,2,3))

# saca "2 y 1"
print ("{pepe} y {juan}".format(juan=1, pepe=2))

#Concatenar
mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

#Multiplicar cadena de texto
mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a + mensaje2b)

#Añadir sucesivamente texto a una misma cadena
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)