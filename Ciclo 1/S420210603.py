#Función REDUCE --> Reduce los elementos de una colección a un único resultado
#Se puede ver esta función como un acumulador (guarda diferentes valores) vs contador (va de uno en uno o dos en dos)
# Obtener la suma de elementos de la lista
#Forma manual
lista = [1,2,3,4,5,6,7,8,9,10]
acumulador = 0

for elemento in lista:
    acumulador += elemento

print(acumulador)

#Con la función
from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10]

def funcion_acumular (acumulador = 0 , elemento = 0):
    return acumulador + elemento

resultado = reduce(funcion_acumular , lista)
print(type(resultado))
print(resultado)

#Con LAMBDA
resultado = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , lista)
print(resultado)

# Ahora con STR
lista = ['Python' , 'Java' , 'Ruby' , 'Elixir']
resultado = reduce(lambda acumulador = '' , elemento = '' : acumulador + ' - ' + elemento , lista)
print(resultado)

# Quitar la primera letra de la palabra y concatenar
lista = ['Python' , 'Java' , 'Ruby' , 'Elixir']
nueva_lista = list(map(lambda ele : ele[1:] , lista))
resultado = reduce(lambda acumulador = '' , elemento = '' : acumulador + ' - ' + elemento , nueva_lista)
print(resultado)

#Suma items + 15
lista = [1,2,3,4,5,6,7,8,9,10]
resultado = reduce(lambda acumulador = 0 , elemento = 0 : acumulador + elemento , lista , 15)
print(resultado)

#Función ZIP --> Une dos listas en una tupla
nombres = ['Raul' , 'Pedro' , 'Sofia']
apellidos = ['Lopez Briega' , 'Perez' , 'Gonzales']
nombre_completo = list(zip(nombres , apellidos))
print(nombre_completo)

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

#Función ALL --> Se debe cumpir que todas las condiciones sean verdaderas para obtener un True
print('Respuestas ALL')
print(all([True , True , True]))
print(all([True , False , True]))
print(all([False , False , False]))
print(all([])) #--> True


#Función ANY --> Con una condición verdadera es suficiente para obtener True
print('Respuestas de ANY')
print(any([True , True , True]))
print(any([True , False , True]))
print(any([False , False , False]))
print(any([])) #--> False

#Ejemplo aplicado 1
info = [int(input()) , input().split(' ')]
print(info)

print('True'
if all(list(map(lambda x : x > 0 , list(map(int , info[1])))))
and
any(list(map(lambda x : x[0] == x[1] or x[0] == '5' , list(zip(info[1] , list(map(lambda x : x[-1 : (len(x)+1)*-1:-1 , 
info[1]])))))))
else 'False'
)