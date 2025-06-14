#Datos complejos en Python

# Diccionario de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Agregar más frutas al diccionario
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500    
precios_frutas['Pera'] = 2300


# Actualizar precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

frutas = list(precios_frutas.keys())



# Diccionario de contactos
contactos = {}

def crear_contactos():
    cantidad = int(input("Ingrese la cantidad de contactos que desea agregar: "))
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        contactos[nombre] = telefono
    return contactos

crear_contactos()

print(f"El número de Juan es: {contactos['Juan']}")


# Diccionario de frecuencias de palabras en una frase
frase = input("Ingrese una frase: ")

# Crear un diccionario con las palabras de la frase como claves y 0 como valor inicial
diccionario_frase = dict.fromkeys(frase.split(), 0)

# Contar la frecuencia de cada palabra en la frase
for palabra in frase.split():
    diccionario_frase[palabra] += 1
print("Frecuencia de palabras en la frase:" + str(diccionario_frase))

#Tupla de 3 notas por alumno

def crear_notas():
    notas = {}
    cantidad = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del alumno: ")
        nota1 = float(input(f"Ingrese la primera nota de {nombre}: "))
        nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
        nota3 = float(input(f"Ingrese la tercera nota de {nombre}: "))
        notas[nombre] = (nota1, nota2, nota3)
    return notas

# Crear notas de alumnos
notas_alumnos = crear_notas()
# Imprimir las notas de los alumnos
print(notas_alumnos)


#Sets y datos repetidos

aprobados_parcial_1 = {'Juan', 'Ana', 'Pedro', 'María', 'Luis'}
aprobados_parcial_2 = {'Ana', 'Pedro', 'Luis', 'Sofía', 'Carlos'}

aprobados = []
for alumno in aprobados_parcial_1:
    if alumno in aprobados_parcial_2:
        aprobados.append(alumno)

medio_aprobados = []
for alumno in aprobados_parcial_1:
    if alumno not in aprobados_parcial_2:
        medio_aprobados.append(alumno)
for alumno in aprobados_parcial_2:
    if alumno not in aprobados_parcial_1:
        medio_aprobados.append(alumno)        

print("Alumnos que aprobaron solo un parcial:", medio_aprobados)

# Manejo de stock de productos en una tienda con diccionario de productos

stock= {'heladeras':10, 'lavarropas':5, 'cocinas':8, 'aires acondicionados':3}

def consultar_stock():
    producto = input("Ingrese el nombre del producto que desea consultar: ")
    if producto in stock:
        print(f"El stock de {producto} es: {stock[producto]}")
    else:
        print(f"El producto {producto} no se encuentra en el stock.")

def actualizar_stock(): 
    producto = input("Ingrese el nombre del producto que desea actualizar: ")
    if producto in stock:
        cantidad = int(input(f"Ingrese la nueva cantidad de {producto}: "))
        stock[producto] = cantidad
        print(f"El stock de {producto} ha sido actualizado a: {stock[producto]}")
    else:
        print(f"El producto {producto} no se encuentra en el stock.")
        print("¿Desea agregarlo? (s/n)")
        respuesta = input().lower()
        if respuesta == 's':
            agregar_producto()
        else:
            print("No se ha realizado ninguna acción.")

def agregar_producto():
    producto = input("Ingrese el nombre del nuevo producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar: "))
    stock[producto] = cantidad
    print(f"El producto {producto} ha sido agregado con una cantidad de: {stock[producto]}")

def manipular_stock():
    while True:
        print("\nOpciones:")
        print("1. Consultar stock")
        print("2. Actualizar stock")
        print("3. Agregar producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            consultar_stock()
        elif opcion == '2':
            actualizar_stock()
        elif opcion == '3':
            agregar_producto()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


#agenda de eventos utilizando diccionario con tuplas como claves
agenda = {}
def crear_agenda():
    cantidad = int(input("Ingrese la cantidad de eventos que desea agregar: "))
    for i in range(cantidad):
        dia = input("Ingrese el día del evento (lunes, martes, etc): ")
        hora = input("Ingrese la hora del evento (HH:MM): ")
        evento = input("Ingrese el nombre del evento: ")
        agenda[(dia, hora)] = evento
    return agenda

def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado para este día y hora.")

agenda = crear_agenda()
print("Agenda creada:", agenda)

print(consultar_evento("lunes", "10:00"))

#voltear diccionario
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(f"Diccionario de capitales y países: {capitales_paises}")
