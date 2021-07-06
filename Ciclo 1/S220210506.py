'''
Negación ¬ NOT
Conjunción ^ AND
Disyunción v OR
Sentencias o Proposiones P Q R S
'''


'''
Pasar el curso de programación
P = tiene al menos 3.0 e nota
Q = asistió al 80% de las clases sincrónicas
'''
# pass = (P ^ Q) --> (V ^ V)



'''
Recibir el subsidio de transporte
P = gana menos de dos salarios mínimos
Q = vive en el sitio de trabajo
R = la empresa suministra transporte completo
S = no vive cerca del lugar de trabajo
'''
# subs = (P ^ ¬Q ^ ¬R ^ S) --> (V ^ V ^ V ^ V)



'''
¿Un año es bisiesto?
P = divisible por 4 
Q = no divisible por 100 pero
R = divisible por 400
'''
# bisi = P ^ (Q v R) --> V ^ (V v V)


# Para crear un condicional se usa IF
if(1 > 2):
    print("La condición P es VERDADERA")
else:
    print("La condición P es FALSA")

# Para saber si la hora es PM o AM (mutuamente excluyentes) son condiciones de tipo SIMPLE (no es necesario definir la condición falsa)
hora_día = 20
if(hora_día >= 12):
    hora_día = hora_día - 12
    print(str(hora_día) + " PM")
else:
    print(str(hora_día) + " AM")

# Hacer una decisión en SECUENCIA (no es relevante el SINO) al clasificar un número como + - 0
var_num = float(input("Ingrese un número : ")) #INPUT sirve para que la persona ingrese un número
if(var_num > 0):
    print("El número es positivo")

if(var_num < 0):
    print("El número es negativo")

if(var_num == 0): # == Hace referencia a si es igual (uno solo no basta)
    print("El número es igual a cero")

# Hacer una decisión en CASCADA con IF --- ELSE
var_num = float(input("Ingrese un número : "))
var_num = int(var_num)

if(var_num <= 9):
    print("El número tiene un solo digito")
else:
    if((var_num >= 10) and (var_num <= 99)):
        print("El número tiene dos digitos")
    else:
        if((var_num >= 100) and (var_num <= 999)):
            print("El número tiene tres digitos")
        else:
            if((var_num >= 1000) and (var_num <= 9999)):
                print("El número tiene cuatro digitos")
            else:
                print("El número tiene más de cuatro digitos :)")
    print("Terminó")

#___________________________________________________________________________________
#___________________________________________________________________________________
#_________________EJERCICIOS TEORÍA_________________________________________________

#Parte A
'''
P: Hoy está haciendo frío
Q: Hoy es lunes
R: Hoy es un día de hacer deporte

1) Q ∨ R = F + V = True
2) ¬ P ∧ ¬ R = V + F = False
3) Q ∧ Q = F + F = False
4) Q ∧ ¬ Q = F + V = False
5) P ∧ (Q ∨ R) = F + (F + V) = F + V = False
6) (P ∧ Q) ∨ R = (F + F) + V = F + V = True
7) (P ∧ ¬ R) ∨ (¬ P ∧ R) = (F + F) + (V + V) = F + V = True
'''

#Parte B
'''
P: Hoy es martes
Q: Hoy está haciendo calor
R: Hoy es un día e fiesta

8) ¬P
9) ¬P ∨ P
10) P ∨ Q ∨ R
11) ¬P ∧ ¬R
'''
#Parte C

'''
12) Q ∧ Q --> Q
13) Q ∧ ¬ Q --> Q
14) Q ∧ Verdadero --> Q
15) Q ∧ Falso ---> ¬Q
16) Q ∨ Verdadero ---> Q
17) Q ∨ Falso --> Q ∨ ¬Q
18) ¬ Q ∧ ¬ Q --> ¬Q
19) ¬ Q ∨ ¬ Q --> Q ∨ ¬Q
20) ¬(Q ∨ P) --> ¬Q ∨ ¬P
21) ¬(Q ∧ P) --> ¬Q ∧ ¬P
22) (P ∧ Q) ∨ (P ∧ R) --> P ∧ (Q ∨ R)
----A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)
----A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)
'''