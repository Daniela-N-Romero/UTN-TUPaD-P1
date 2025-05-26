#Ejercicio 1: Factorial de un número

def factorial(n):
    if n == 0 or n == 1:
        suma = 1
    else:
        suma = n * factorial(n-1)
    return suma

def factoriales_hasta():
  n = int(input("Ingresa un número hasta el cuál quieres calcular factoriales: "))
  for i in range(1, n+1):
    print(f"El factorial de {i} es { factorial(i)}")

# ----------------------------------------------------------------------------------------    

#Ejercicio 2: Obtener serie de Fibonacci hasta n

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_hasta(pos):
  # pos = int(input("¿Qué posición de la serie de Fibonacci querés saber?: "))
  for i in range(pos):
    print(fibonacci(i), end=" ")

# ----------------------------------------------------------------------------------------    

#Ejercicio 3: Potencia de un número

def elevar_n_a_m(n,m):
  if m == 0:
    return 1
  else:
    return n * elevar_n_a_m(n, m-1)

def calcular_potencia():
  base = int(input("Ingresa la base de la potencia a calcular: "))
  exponente = int(input("Ingresa el exponente de la potencia a calcular: "))
  print(f"{base} elevado a {exponente} es {elevar_n_a_m(base,exponente)}")

# ----------------------------------------------------------------------------------------    

# Ejercicio 4: Conversión de decimal a binario

def div_guardar_resto(n):
  if n == 0 or n == 1:
    resto = str(n) # si la división es 0 o 1, guardo directamente ese valor (porque sera el resto al querer dividirlo por 2)
    return resto
  else:
    resto = str(n%2) # guardo el resto de la división entre 2
    n = n//2 # divido el número entre 2 para que la siguiente iteración se devuelva el resto de la división de n ahora dividido por 2
  return  div_guardar_resto(n) + resto  #concateno el resto guardado en la variable resto con el resultado de la función recursiva. De esta manera voy guardando los restos de cada división y al final los concateno para obtener el número binario completo.

def a_binario():
    n = int(input("Ingrese un número entero mayor a 0 para convertir en binario: "))
    div_guardar_resto(n)
    print(f"El número {n} en binario es: {div_guardar_resto(n)}") 


# ----------------------------------------------------------------------------------------    

#Ejercicio 5: Conversión de binario a decimal

def revertir_string(x):
  if len(x) == 0:
    return ""
  else:
    new_x = x[-1] # guardo el último caracter de la cadena
    x = x[0:-1] # elimino el último caracter de la cadena
  return new_x + revertir_string(x) # concateno el último caracter guardado con el resultado de la función recursiva, que va a devolver el resto de la cadena sin el último caracter. De esta manera voy guardando los caracteres de la cadena y al final los concateno para obtener la cadena invertida.

def es_palindromo():
  string = input("Ingrese una palabra para verificar si es palindromo: ")
  new_str = revertir_string(string)
  return string == new_str

# ----------------------------------------------------------------------------------------
#Ejercicio 6: suma recursiva de los dígitos de un número

def suma_digitos(n):
  if 0 < n < 10:
    return n
  elif n >= 10:
    ult_digito = n % 10 
  return ult_digito + suma_digitos(n // 10) # sumo el último dígito con el resultado de la función recursiva, que va a devolver la suma de los dígitos restantes del número.

# ----------------------------------------------------------------------------------------

#Ejercicio 7: piramide con bloques

def contar_bloques(n):
  suma= 0
  if n == 0:
    return 0
  elif n > 0:
    suma += n
  return suma + contar_bloques(n-1)

#Ejercicio 8: contar veces que aparece un dígito en un número

def contar_digito(n, dig):
  if n == 0:
    return int(n == dig)
  else:
    ult_dig = n % 10 
    n = n // 10
    return int(ult_dig == dig) + contar_digito(n, dig)
