#TP 6 - Listas

#EJERCICIO 1
multiplos_de_4 = list(range(0,101,4))
multiplos_de_4.remove(0)
print(multiplos_de_4)

#EJERCICIO 2
nombres = ["Laura", "Daniela", "Joaquin", "Lucas", "Sofia"]
print(nombres[-1])
print(nombres[4])

#EJERCICIO 3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(lista_vacia)

#EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]
animales[2] = "loro"
animales[-1] = "oso"
print(animales)

#EJERCICIO 5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#El programa elimina el numero mayor de la lista y luego imprime la lista modificada.

#EJERCICIO 6
numeros = list(range(10,31,5))
print(numeros)
print(numeros[0:2])

#EJERCICIO 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "chronos"
autos[2] = "focus"
print(autos)

#EJERCICIO 8

#EJERCICIO 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan") 
print(compras) 