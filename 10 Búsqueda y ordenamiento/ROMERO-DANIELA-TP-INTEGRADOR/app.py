import time
import random
import sys

#Aumentamos el límite de recursión para evitar RecursionError en pruebas grandes
sys.setrecursionlimit(10000)

# Algoritmos de ordenamiento
# Burbuja, Selección, Inserción, Quicksort

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def seleccion(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento mínimo
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# Algoritmos de búsqueda
## Lineal, Binaria

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):  
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

#funciones para el programa principal
# Generar una lista aleatoria de números enteros
def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Función para calcular el tiempo de ejecución de una función
def calcular_tiempo(funcion):
    inicio = time.time()
    funcion() 
    fin = time.time()
    duracion_ms = (fin - inicio) * 1000  # Convertir a milisegundos
    return duracion_ms

# Funciones para elegir el algoritmo de ordenamiento y búsqueda
def elegir_ordenamiento(datos):
        print("¿Qué método de ordenamiento deseas usar? (ingresa el número)")
        print("1. Burbuja")     
        print("2. Selección")
        print("3. Inserción")
        print("4. Quicksort")
        input_ordenamiento = int(input("Ingrese el número del método: "))
        match input_ordenamiento:
            case 1:
                print("Usando el método de ordenamiento Burbuja")
                return calcular_tiempo(lambda: burbuja(datos)), "Burbuja"
            case 2:
                print("Usando el método de ordenamiento Selección")
                return calcular_tiempo(lambda: seleccion(datos)), "Selección"   
            case 3:
                print("Usando el método de ordenamiento Inserción")
                return calcular_tiempo(lambda: insercion(datos)), "Inserción"         
            case 4:
                print("Usando el método de ordenamiento Quicksort")
                return calcular_tiempo(lambda: quicksort(datos)), "Quicksort"
            case _:
                print("Método no válido, se usará burbuja por defecto")
        
def elegir_busqueda(datos):
    print("¿Qué método de búsqueda deseas usar? (ingresa el número)")
    print("1. Lineal")
    print("2. Binaria")
    input_busqueda = int(input("Ingrese el número del método: "))
    elemento_buscado = int(input("Ingrese el elemento a buscar: "))
    match input_busqueda:
        case 1:
            print("Usando el método de búsqueda Lineal")
            return calcular_tiempo(lambda: busqueda_lineal(datos, elemento_buscado)), "Lineal"
        case 2:
            print("Usando el método de búsqueda Binaria. Si no se hizo antes, la lista se ordena para realizarla.")
            datos_ordenados= quicksort(datos.copy())
            return calcular_tiempo(lambda: busqueda_binaria(datos_ordenados, elemento_buscado)), "Binaria"
        case _:
            print("Método no válido, se usará búsqueda lineal por defecto")

#programa principal

def probar_algoritmos():
    print("Bienvenido a la prueba de algoritmos")
    cantidad = int(input("Ingrese la cantidad aproximada de datos a procesar: "))
    datos = generate_random_list(cantidad)  
    ordenamiento = input("¿Deseas ordenarlos? Y/N ").lower()
    tiempo_ordenamiento = 0
    tiempo_busqueda = 0
    tipo_busqueda = "ninguno"
    tipo_ordenamiento = "ninguno"
    if ordenamiento == 'y':
        tiempo_ordenamiento, tipo_ordenamiento = elegir_ordenamiento(datos)
    else: 
        print("No se eligio ordenar los datos.")
    busqueda = input("¿Deseas probar un algoritmo de busqueda? Y/N ").lower()
    if busqueda == 'y':
        tiempo_busqueda, tipo_busqueda = elegir_busqueda(datos)
    else:
        print("No se eligio buscar un elemento en los datos.")    
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.4f} ms, tipo: {tipo_ordenamiento}")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.4f} ms, tipo: {tipo_busqueda}")


#ejecutar el programa principal
probar_algoritmos()
