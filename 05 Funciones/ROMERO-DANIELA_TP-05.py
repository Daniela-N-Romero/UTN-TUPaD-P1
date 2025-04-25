import utils
#modularize, y dividi el programa. La mayoria de la lógica está en utils.py

#PROGRAMA PRINCIPAL

#saludo al mundo
utils.imprimir_hola_mundo()

#saludo a un usuario
utils.saludar_usuario()

#solicito la informacion personal del usuario
utils.informacion_personal()

#calculo el area y perimetro de un circulo
utils.calcular_area_perimetro_circulo()

#convierto segundos a horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = utils.segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")

#calculo la tabla de multiplicar de un numero
numero = int(input("Ingrese un numero para hacer su tabla de multiplicar: "))
utils.tabla_multiplicar(numero)

#ejecuto operaciones basicas    
utils.operaciones_basicas()
utils.operaciones_basicas2() #esta es una que genere con ayuda de IA

#función para calcular IMC
utils.calcular_imc()

#funcion para convertir celcius a fahrenheit
utils.celsius_a_farenheit(32)

#funcion para calcular promedio 
utils.calcular_promedio(2,3,6)
utils.calcular_promedio2(10, 20, 30, 40, 50) #esta es extra. Puede tomar cualquier cantidad de numeros y promediarlos


