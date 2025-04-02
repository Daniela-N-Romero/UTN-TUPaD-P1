#Práctico 1: Estructuras secuenciales
#Alumna: Daniela Romero
#DNI: 38440237


#actividad 1

print("Hola Mundo!")

#actividad 2

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#actividad 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#actividad 4

radio = float(input("Ingrese el radio de un círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es {area} y el perímetro es {perimetro}.")


#actividad 5

segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"La cantidad de horas equivalentes es {segundos // 3600}")

# actividad 6

numero = int(input("Ingrese un número: "))
print(f"{numero} * 0 = {numero * 0}")
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

#actividad 7

num1 = int(input("Ingrese un número distinto a 0: "))
num2 = int(input("Ingrese otro número distinto a 0: "))
print(f"La suma de {num1} y {num2} es {num1 + num2}")
print(f"La resta de {num1} y {num2} es {num1 - num2}")
print(f"La multiplicación de {num1} y {num2} es {num1 * num2}")
print(f"La división de {num1} y {num2} es {num1 / num2}")

# actividad 8

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
print(f"Su índice de masa corporal es {peso / altura ** 2}")

# actividad 9

celsius = float(input("Ingrese una temperatura en grados Celsius: "))
print(f"La temperatura en grados Fahrenheit es {celsius * 9/5 + 32}")

#actividad 10

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese un tercer número: "))
print(f"El promedio de los tres números es {(num1 + num2 + num3) / 3}")
