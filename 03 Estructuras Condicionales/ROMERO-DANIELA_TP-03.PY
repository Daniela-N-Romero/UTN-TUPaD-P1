#ACTIVIDADES

#ACTIVIDAD 1

edad = int(input("Ingrese un edad: "))
if edad >= 18:
    print("Es mayor de edad")   

#ACTIVIDAD 2

nota = int(input("Ingrese su nota: "))
#aca se podria mejorar utilizando float como lo dice en las soluciones. 

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#ACTIVIDAD 3

numeroPar = int(input("Ingrese un numero par: "))

if numeroPar % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")

#ACTIVIDAD 4

edad = int(input("Ingrese su edad en años: "))

#En este caso, no vuelvo a verificar cosas como en la segunda "si es mayor o igual a 12" porque ya lo hice antes con la condicion anterior. Si hubiera sido menor, no hubiera llegado a la segunda condicion. Así sucesivamente.

if edad > 0 and edad < 12:
    print("Es niño/a")
elif edad < 18:
    print("Es adolescente")
elif edad < 30:
    print("Es adulto/a joven")
else:    
    print("Es adulto/a")

#ACTIVIDAD 5

password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

#aqui verifico que la contraseña tenga entre 8 y 14 caracteres con la funcion len()
if len(password) >= 8 and len(password) <= 14:     #Otra forma segun las soluciones es: 8 <= len(password) <= 14
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")

#ACTIVIDAD 6

#importo la libreria random para generar numeros aleatorios y las funciones de la libreria statistics para calcular la media, mediana y moda.
from statistics import median, mode, mean
import random

#genero una lista de 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

#guardo los valores de  media, mediana y moda en variables
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#verifico si existe un sesgo positivo, negativo o ninguno.
if media > mediana and mediana > moda:
    print("Existe un sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Existe un sesgo negativo o a la izquierda.")
elif media == moda and moda == mediana:
    print("Sin sesgo")

#ACTIVIDAD 7

texto = input("Ingrese una palabra o frase:")

#utilizo el operador de pertenencia in para verificar si la última letra de la cadena es una vocal en un string con todas las vocales tanto en mayusculas como en minusculas.

#con un condicional ternario imprimo el texto seguido de un signo de admiración si la última letra es una vocal, sino imprimo el texto tal cual.
print(texto + "!" if texto[-1] in "aeiouAEIOU" else texto)

#ACTIVIDAD 8

nombre = input("Ingrese su nombre: ")
print("Indique un número: ¿1,2 o 3?")
print("1. Si quiere su nombre en mayusculas.")
print("2. Si quiere su nombre en minusculas.")
print("3. Si quiere su nombre con la primera letra mayuscula.")
opcion = int(input("Ingrese su opción: "))

#utilizo un condicional if para verificar la opción elegida por el usuario y luego imprimo el nombre en el formato correspondiente.
if opcion == 1:
    print(nombre.upper())   
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    #si el usuario ingresa una opción no válida, imprimo un mensaje de error.
    print("Opción no válida. Por favor, elija 1, 2 o 3.")


#ACTIVIDAD 9

magnitud = int(input("Ingrese la magnitud del terremoto: "))
#aca se podria mejorar utilizando float como lo dice en las soluciones. 

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
elif magnitud >= 7:
    print("Extremo.")

#ACTIVIDAD 10

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

#utilizo una tupla para almacenar el mes y el día ingresados por el usuario.
#este formato me permite comparar las fechas de manera más sencilla.
#saque información de https://es.py4e.com/html3/10-tuples

fecha = (mes, dia)

if hemisferio == "N":
    if (3, 20) <= fecha < (6, 21):
        print("Es primavera")
    elif (6, 21) <= fecha < (9, 23):
        print("Es verano")
    elif (9, 23) <= fecha < (12, 21):
        print("Es otoño")
    else:
        print("Es invierno")

elif hemisferio == "S":
    if (3, 20) <= fecha < (6, 21):
        print("Es otoño")
    elif (6, 21) <= fecha < (9, 23):
        print("Es invierno")
    elif (9, 23) <= fecha < (12, 21):
        print("Es primavera")
    else:
        print("Es verano")

else:
    print("Hemisferio no válido. Ingrese 'N' o 'S'.")