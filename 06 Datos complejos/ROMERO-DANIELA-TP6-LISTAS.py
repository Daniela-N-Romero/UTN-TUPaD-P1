#TP 6 - Listas

#EJERCICIO 1
multiplos_de_4 = list(range(0,101,4))
multiplos_de_4.remove(0)
print(f"Los multiplos de 4 son: {multiplos_de_4}")

#EJERCICIO 2
nombres = ["Laura", "Daniela", "Joaquin", "Lucas", "Sofia"]
print(f"El nombre en la penúltima posición es: {nombres[-2]}")
print(f"El nombre en la penúltima posición es: {nombres[3]}")

#EJERCICIO 3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(f"Los elementos de la lista ahora son: {lista_vacia}")

#EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(f"Los animales ahora son: {animales}")

#EJERCICIO 5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(f"Los numeros ahora son: {numeros}")
#El programa crea una lista con números.
#Luego elimina el numero mayor de la lista 
#Por último, imprime la lista modificada.

#EJERCICIO 6
numeros = list(range(10,31,5))
print(f"Los numeros son: {numeros}")
print(f"Los primeros dos numeros son: {numeros[0:2]}")

#EJERCICIO 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "chronos"
autos[2] = "focus"
print(f"Los autos ahora son: {autos}")

#EJERCICIO 8
dobles = []
for i in range(5,16,5):
    dobles.append(i*2)
print(f"Los dobles son: {dobles}")

#EJERCICIO 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan") 
print(f"Las compras ahora son: {compras}") 

#EJERCICIO 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(f"Los elementos de la lista anidada son: {lista_anidada}")
print(f"lista_anidada[0]: {lista_anidada[0]}") 
print(f"lista_anidada[1]: {lista_anidada[1]}")
print(f"lista_anidada[2][0]: {lista_anidada[2][0]}")
print(f"lista_anidada[2][1]: {lista_anidada[2][1]}")
print(f"lista_anidada[2][2]: {lista_anidada[2][2]}")
print(f"lista_anidada[3]: {lista_anidada[3]}")
