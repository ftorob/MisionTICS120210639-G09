# Hacer el mismo ejercicio anterior pero con IF --- ELIF (funciona con positivos ya que -678 lo pone como un digito --> Se podría validar multiplicando *-1 para validarlo que quede siempre positivo)
var_num = float(input("Ingrese un número : "))
var_num = int(var_num)

if(var_num <= 9):
    print("El número tiene un solo digito")
elif ((var_num >= 10) and (var_num <= 99)):
    print("El número tiene dos digitos")
    print("Terminó")
elif ((var_num >= 100) and (var_num <= 999)):
    print("El número tiene tres digitos")
elif ((var_num >= 1000) and (var_num <= 9999)):
    print("El número tiene cuatro digitos")
else:
    print("El número tiene más de cuatro digitos")
# Un IF puede tener muchos (ELSE + IF ||| ELIF) pero UN solo ELSE

# Ahora vamos a utilizar la función LEN para resumir todo (funciona con positivos -678 lo pone como 4 digitos)
var_num = float(input("Ingrese un número : "))
var_num = int(var_num)

if(len(str(var_num)) == 1): #La función LEN solo sirve con cadenas de texto por esto se agrega el STR
    print("El número tiene un solo digito")
elif(len(str(var_num)) == 2):
    print("El número tiene dos digitos")
elif(len(str(var_num)) == 3):
    print("El número tiene tres digitos")
elif(len(str(var_num)) == 4):
    print("El número tiene cuatro digitos")
else:
    print("El número tiene más de cuatro digitos")


#Vamos a trabajar con DECISIONES ANIDADAS (para solucionar el -678 se multiplica por -1)
def test_num():
    entero = int(input("Ingrese un número : "))
    if(entero == 0):
        return "El número no puede ser cero"
    elif(entero < 0):
        #Varias soluciones -->
        #entero = entero * -1
        #if((len(str(entero)) - 1 == 3)):
        #if((entero <= -100) and (entero >= -999)):
        if((len(str(entero)) == 4)):
            return "El número es negativo y tiene tres digitos"
        else:
            return("El número es negativo y tiene más o menos de tres digitos")
    elif(entero > 0):
        if((len(str(entero)) == 2)):
            return("El número es positivo y tiene dos digitos")
        else:
            return("El número es positivo y tiene más o menos de dos digitos")


print(test_num())