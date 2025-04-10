#TRABAJO PRACTICO N°4
#Estructuras Repetitivas

#Ejercicio 1
#1)	Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
   print(i)

#Ejercicio 2
#2)	Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingrese un número entero: ")
print("La cantidad de dígitos del número ingresado es: ",len(numero))

#Ejercicio 3
#3)	Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
suma = 0

for i in range(num1+1,num2):
    suma += i

print("La suma de los números enteros entre", num1, "y", num2, "es:", suma)

#Ejercicio 4
#4)	Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingrese un número entero (0 para salir): "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para salir): "))

print("La suma total es:", suma)

#Ejercicio 5
#5)	Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numaleatorio = random.randint(0,9)
intento = int(input("Adivina el número entre 0 y 9: "))
intentos = 1

while intento != numaleatorio:
    intentos += 1
    intento = int(input("Incorrecto. Intenta nuevamente: "))

print("¡Felicidades! El número era ", numaleatorio, " y lo adivinaste el número en ", intentos, " intentos.")

#Ejercicio 6
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("METODO 1")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

print("METODO 2")
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7
#7)	Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

if numero > 0:
    # suma de números enteros hasta el numero ingresado exclusivo
    for i in range (1, numero): 
        suma += i

print("La suma total es:", suma)

#Ejercicio 8 
#8)	Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

positivos = 0
negativos = 0
impares = 0
pares = 0

for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    #verifico si es positivo o negativo
    #si es cero no lo cuento como positivo ni negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    #verifico si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

#Ejercicio 9
#9)	Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

from statistics import mean
numeros = []

for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

print("La media de los números ingresados es:", mean(numeros))


#Ejercicio 10
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
numero_invertido = 0

for i in range(len(str(numero))):
    digito = numero % 10 #obtengo el último dígito
    numero_invertido = numero_invertido * 10 + digito #multiplico el número invertido por 10 y le sumo el último dígito
    numero = numero // 10 #elimino el último dígito del número original

print("El número invertido es:", numero_invertido)