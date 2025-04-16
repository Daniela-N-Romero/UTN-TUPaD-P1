#funcion para imprimir "Hola Mundo"

def imprimir_hola_mundo():
    print("Hola Mundo!")

#funcion para saludar con un nombre de usuario

def saludar_usuario():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Hola {nombre}!")

#funiciones para solcitar informacion de un usuario e imprimirla

#solicito un dato al usuario mediante un input y lo devuelvo
def solicitar_dato_usuario(dato):
    informacion = input(f"Ingrese su {dato}: ")
    return informacion

#solicito varios datos al usuario y los devuelvo
def solicitar_informacion_personal():
    nombre = solicitar_dato_usuario("nombre")
    apellido = solicitar_dato_usuario("apellido")
    edad = solicitar_dato_usuario("edad")
    direccion = solicitar_dato_usuario("dirección")
    return nombre, apellido, edad, direccion

#imprimo la informacion del usuario
def informacion_personal():
    nombre, apellido, edad, direccion = solicitar_informacion_personal()
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {direccion}.")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#funciones para calcular el area y perimetro de un circulo
from math import pi

def calcular_area_circulo(radio):
    area = round(pi * radio ** 2,2)
    return area

def calcular_perimetro_circulo(radio):  
    perimetro = round(2 * pi * radio,2)
    return perimetro
    
#funcion que llama a las dos anteriores y devuelve un string con el area y perimetro del circulo
def calcular_area_perimetro_circulo():
    radio = float(input("Ingrese el radio del circulo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del circulo es {area} y el perimetro es {perimetro}.")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#función para calcular cuantas horas son un total de segundos

def segundos_a_horas(segundos):
    horas = round(segundos / 3600,2)
    return horas

#funcion para calcular la tabla de multiplicar de un numero

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#función para operaciones basicas

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")    
    return (suma, resta, multiplicacion, division)


#Con ayuda de inteligencia artificial realizo una funcion que hace lo mismo que la anterior pero con un for y eval
def operaciones_basicas2(a,b):
    operaciones = ["+","-","*","/"]
    for i in operaciones:
        resultado = eval(f"{a} {i} {b}")
        print(f"{a} {i} {b} = {resultado}")

#EXTRA: otra forma de hacer la funcion operaciones basicas si solo querés hacer una
#solicito dos numeros y una operación
def solicitar_operacion():
    parametros = ["el primer número", "el segundo número", "el simbolo de la operacion (+, -, *, /)"]
    for i in range(len(parametros)):
        parametros[i] = input(f"Ingrese {parametros[i]}: ")
    return parametros

#realizo las operaciones
def operacion_entre_numeros(a, b, operacion):
    a = int(a)
    b = int(b)
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b if b != 0 else "Error (división por cero)"
    else:
        return "Operación inválida"
    
#llamo a la funcion que hace solicit ay hace cualquier operacion entre dos numeros
def calcular_operacion():
    a, b, operacion = solicitar_operacion()
    resultado = operacion_entre_numeros(a, b, operacion)
    print(f"El resultado de la operación {a}{operacion}{b} es: {resultado}")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#función para calcular IMC
def calcular_imc():
    peso = float(solicitar_dato_usuario("peso en kg"))
    altura = float(solicitar_dato_usuario("altura en metros"))
    imc = round(peso / (altura ** 2), 2)
    print(f"Con un peso de {peso} kg y una altura de {altura}m., su IMC es: {imc}")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#función para convertir celcius a farenheit
def celsius_a_farenheit(celsius):
    #aca podria usar tambien otra vez la funcion que cree de solicitar_dato_usuario, pero quise variar un poco
    farenheit = round((celsius * 9/5) + 32,2)
    print(f"{celsius}°C en Farenheit son {farenheit}°F")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#función para calcular el promedio de 3 numeros
def calcular_promedio(num1, num2, num3):
    promedio = round((num1 + num2 + num3) / 3, 2)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla

#otra opcion mas escalable
def calcular_promedio2(*numeros):
    suma = sum(numeros)
    promedio = round(suma / len(numeros), 2)
    print(f"El promedio de los números ingresados es: {promedio}")
    #no retorno nada porque el ejercicio solo solicitaba mostrar en pantalla