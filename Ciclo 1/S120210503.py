# Declaramos la variable de tipo ENTERO
var_int = 50

# Declaramos la variable de tipo FLOAT | DOBLE | Flotante o número decimal
var_pi = 3.1416

# Declaramos la variable de tipo CADENA DE TEXTO | STRING
var_str = "Grupo 39"

# Declaramos a variable de tipo buleano FALSO | VERDADERO | 1 | 0
var_boo = False

# corchete crear variable de diccionario {}
var_dict = {"nombre":"juliana" , "apellido":"Correa" , "edad": 19}

# Declaramos una variable de tipo TUPLA | TUPLE
var_tup = (3, 4, 5, 7.8, 10)
print(type(var_tup))

#print(type(var_dict)) para saber el tipo de variable sino se está seguro
'''
print(type(var_int))
print(type(var_pi))
print(type(var_str))
print(type(var_boo))
print(type(var_dict))
'''
#Función DIR (Python tiene una función llamada dir que enumera los métodos disponibles para un objeto.)
cadena = '¡Holi!'
print(dir(cadena))

# Corchete para crear o modificar item del diccionario []
var_dict ["nombre"] = "Fernando"

# agregar nuevo campo al diccionario
var_dict["peso"] = 60

# eliminar un campo del diccionario
var_dict.pop('apellido')

# Imprimir una cadena de texto concatenada con variables
print("El nombre de la persona es " + var_dict['nombre'] + " y tiene " + str(var_dict['edad']) + " años")
print(var_dict)

# hacer la lista vertical
var_dict = {
    "nombre":"juliana" ,
    "apellido":"Correa" ,
    "edad": 19
    }

# f permite agregar variables a un string
print(f"El nombre de la persona es {var_dict['nombre']} y tiene {var_dict['edad']} años")

# se coloca el string y las variables luego con la función FORMAT
print("El nombre de la persona es {} y tiene {} años".format(var_dict['nombre'], var_dict['edad']))

'''
para diccionarios ={}
para listas=[]
para tuplas=()
'''

# Declarar variables FLOAT
var1 = 1.20
print(var1)

# Oligar a que lavariable sea un entero
# Castiar variables de FLOAT o ENTERO (convertir de un dato a otro)
var1 = int(var1)
print(var1)

'''
Errores al declarar variables
- Dejar espacio var 1 = 8
- Usar caracteres especiales var@ = 8
- Usar número al inicio de la variable 1var = 8
- Usar guíon al medio var-1 (incorrecto) vs var_1 (correcto) var-1 = 8
'''

# Declarar tres variables con el mismo valor (Asignación de un solo valor a varias variables)
num_1 = num_2 = num_3 = 200
print(num_3)

# Declarar variables en sentido horizontal (Asignar varios valores a varias variables)
num_x1, num_x2, num_x3 = 10, 85, 4.6
print(num_x3)
print(num_x2)
print(num_x1)


'''
Operadores básicos
+ Suma
- Resta
* Multiplicación
/ División
// División enteros
** Potencia
() Parentesis
'''

nota1 = 3.4
nota2 = 4
nota3 = 2.6
nota4 = 4.7

# Operaciones básicas
var_suma = nota1 + nota2 + nota3 + nota4 #suma
print(var_suma)

var_resta = nota2 - nota4 #resta
print(var_resta)

var_multi = nota2 * nota1 #multiplicación
print(var_multi)

var_divi = nota4 / nota1 #división
print(var_divi)

var_divent = nota4 // nota1 #división entero
print(var_divent)

var_divres = nota4 % nota1 #residuo de la división
print(var_divres)

var_cuadrado = nota2 ** 2 #potencia al cuadrado
print(var_cuadrado)

var_cubico = nota2 ** 3 #potencia al cubo
print(var_cubico)

var_cinco = 2 ** 5 #potencia a la cinco
print(var_cinco)

var_raiz = var_cubico ** (1/2) #raiz cuadrada de un número
print(var_raiz)

# Orden en que ocurren las operaciones PEMDAS (PARENTESIS + EXPONENCIACIÓN + MULTIPLICACIÓN + DIVISIÓN + SUMA + RESTA)

var_PEMDAS = 4 + 7 * 2 ** (5 - 10) / 2
print(var_PEMDAS)

var_PEMDAS2 = 4 + 7 * 2 ** (10 - 5) / 2
print(var_PEMDAS2)

promedio = ((nota1 + nota2 + nota3 + nota4)/4)
print(promedio)
print(round(promedio,2)) # Redonear a dos cifras
print(round(promedio,1)) # Redondear a una cifra

# Ejercicios rápidos

# 1) ¿Que imprime el siguiente programa ?
var_x1 = 43
var_x1 = var_x1 + 1
print(var_x1)

# 2) Calcule el promedio de las siguientes variables
var_a = 10
var_b = 4
var_c = 5.5
var_d = 67

# 3) Calcule el área y perímetro de un cuadrado
var_lado = 38
var_area = var_lado ** 2
var_perimetro = var_lado * 4
print("El área del cuadrado es " + str(var_area) + " m2" + "y su perímetro es de " + str(var_perimetro) + " m.")

var_promejer = (var_a + var_b + var_c + var_d)/4
print("El promedio de esos números es " + str(var_promejer))

# Funciones de Python
promedio_fsum = (sum((nota1, nota2, nota3, nota4))/4)
print(round(promedio_fsum,2))
print(int("2021") + 9) # Conveetir un str a número entero y sumarlo

nota_max = max(nota1, nota2, nota3, nota4) # Máximo de un conjunto de datos
print(nota_max)

nota_min = min(nota1, nota2, nota3, nota4) # Mínimo de un conjunto de datos
print(nota_min)

help(max) # La función HELP me dice como debo construir una función

x = range(5,100)
print(x)
print(len(x))

texto = "QF, QF" #cuenta el número de caracteres de una frase
print(len(texto))

numb = (3, 4, 5, 6, 7) #cuenta el número de números en una lista o rango
x = len(numb)
print(x)