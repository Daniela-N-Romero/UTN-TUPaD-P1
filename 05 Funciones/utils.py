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

#función para calcular cuantas horas son un total de segundos

def segundos_a_horas(segundos):
    horas = round(segundos / 3600,2)
    return horas

#funcion para calcular la tabla de multiplicar de un numero

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")