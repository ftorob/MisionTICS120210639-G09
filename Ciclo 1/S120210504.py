# Crear una función que me permita repetir una cadena de texto
def repetirTexto(t : str):
    tex_r = t + " " + t
    print(tex_r)

repetirTexto('Fernando')

# Crear una función sin parametros
def imprimirMen():
    print("I love pharmacy")

# Llamar la función creada
imprimirMen()

# Crear una función que me retorne una cadena de texto
def imprimirMen_r():
    return "Grupo 39"

#Llamar la función de retorno
print(imprimirMen_r())

texto = imprimirMen_r()
print(texto)

# Craer función suma
def suma_ftb(var_a, var_b, var_c):
    resultado = var_a + var_b + var_c
    return resultado #El return es muy importante para devolver el valor a la función ||| sino se coloca el resultado en print será NONE

print(suma_ftb(1, 2, 3))

# Crear función resta
def resta_ftb(var_a, var_b, var_c):
    resultado = var_a - var_b - var_c
    return resultado

print(resta_ftb(20, 10, 5))

# Crear una función que repita varias funciones
def repetirOpe():
    print(suma_ftb(1, 2, 3))
    print(suma_ftb(7, 3, 2))
    print(resta_ftb(5, 1, 1))
    print(resta_ftb(1, 1, 5))

repetirOpe()

# Crear una función que calcule el promedio basado en unas notas, concatenar con texto y arrojar nota con dos cifras decimales
def promedio_est(var_a, var_b, var_c):
    resultado = suma_ftb(var_a, var_b, var_c)/3
    return resultado

nota1 = 2
nota2 = 3
nota3 = 5

mi_resultado = promedio_est(nota1, nota2, nota3)
red_mires = round(mi_resultado,2)
print("El promedio de mi semestre es " + str(red_mires))

# Otra opción para el mismo ejercicio anterior pero está muy amarrado ya que da el resultado de solo tres notas
def promedio_est2(var_a, var_b, var_c):
    resultado = suma_ftb(var_a, var_b, var_c)/3
    resultado = round(resultado,2)
    return "El promedio de mi semestre es " + str(resultado)

nota1 = 5
nota2 = 10
nota3 = 17

mi_resultado = promedio_est2(nota1, nota2, nota3)
print(mi_resultado)

# Ahora para hacer una función que calcule el promedio de todas las notas que yo quiera recurro a listas/tuplas
def calc_prom_ftb(list_notasqf : tuple):
    resultado = (sum(list_notasqf)/len(list_notasqf))
    resultado = round(resultado,2)
    return "El promedio de mi semestre es " + str(resultado)

mis_notas = (3, 4, 5, 6 , 7, 1.5, 2.3)
mi_prom_ftb = calc_prom_ftb(mis_notas)
print(mi_prom_ftb)

# Vamos a utilizar la sentencia PASS - No devuelve ningún valor NONE y no interrumpe el código
# Útil cuando necesito crear una variable pero para usarla y definirla despues
def pti (letra_gen):
    pass

type(pti)
print(pti("f"))

# Función para multiplicar y salida como enteros
def multi_ftb (var_a : int, var_b : int) -> int:
    resultado = var_a * var_b
    return resultado

print(multi_ftb(5.3, 6.4))

# Función para DIVIDIR y salida como STRING
def divi_ftb (var_a, var_b) -> str:
    resultado = str(round(var_a / var_b,2))
    return "El resultado es: " + resultado

print(divi_ftb(12.3, 6.4))

#Incluir un diccionario a la función
# Crear el diccionario con nombre + apellido
mi_nombre = {'dato1':'Fernando' , 'dato2':'Toro'}

# Crear l función del nombre completo
def diccion_ftb (info : dict) -> str:
    resultado = "Mi nombre completo es " + info['dato1'] + " " + info['dato2']
    return resultado
 
print(diccion_ftb(mi_nombre))

# Crear l función del nombre completo
def diccion_ftb (info : dict) -> str:
    return "Mi nombre completo es " + info['dato1'] + " " + info['dato2']
    
print(diccion_ftb(mi_nombre))

# Desarrollo de la guía de funciones básicas
# La función se debe construir antes de llamarla
def repetir_funciones():
    imprime_Cosas()
    imprime_Cosas()
    
def imprime_Cosas():
    print("La clase esta genial")   
    print('Python es lo maximo')
    
repetir_funciones()

# Argumento por posición
def suma(a, b):
    return a - b

print(suma(30, 10))

# Argumentos por nombre
def suma(a, b):
     return a - b

b=30
a=10

print(suma(a, b))

# \n
def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    
resultado = otra_suma(5,6)
print(resultado)

def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2
    
resultado = otra_suma(5,6) 
print(resultado)

# Menos argumentos que los parametros ingresados
def saludar(nombre, apellido, mensaje='Hola', mensaje2='Don'): #Parámetros por omisión
    print(mensaje, mensaje2, nombre, apellido)

saludar('Pepe Grillo','QF', mensaje2='mi estimado') #Keywords como parámetros
