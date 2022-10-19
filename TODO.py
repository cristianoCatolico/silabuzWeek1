"""
Ejercicio 1: Hacer un programa que pida al usuario 5 nombres. Crear una lista con los 5 nombres. Despues hacer que muestre una frase los pronombres que empiezan con la letra A
"""


"""
Ejercicio 2: Haga un programa en Python que le pida al usuario tantos enteros como quiera, luego cree dos listas, una con la lista de números propuestos y la otra con
el número de ocurrencias. Por ejemplo, si el usuario ingresa 4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2] 
"""
matriz = [[1,2,3],[4,5,6],[7,8,9]]
listadd=[]
for i in range(len(matriz)):
      listadd.append(matriz[i][i])
      print (matriz[i][i])

prom = sum(listadd)/len(matriz)

print (f"El promedio es: {prom}")
"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""

"""
Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""
lista =["Hola", "Amigos", "Hoy", True]
agregar=input('Ingrese un valor: ')
ubicacion=input('precione "I" si quiere que la lista es al inicio o "F" si quiere que este al final ').upper()
if ubicacion=='I':
      inicio=lista.insert(0,agregar)
else:      
      ultimo=lista.append(agregar)
print(lista)
"""
Ejercicio 4
Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que dado un dato por el usuario, este sea eliminado de la lista. Tome en cuenta que el usuario ingresará datos que se encuentran dentro de la lista

Ejemplo:

Ingrese el dato a eliminar: 60

Salida: [15,20,50,80,40]
"""
lista2=[15,20,50,80,40,60]
eliminar=int(input('Ingrese un valor a eliminar: '))
print(lista2)
lista2.remove(eliminar)
print(lista2)

"""
Ejercicio 5
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado un elemento por el usuario, imprima el número de veces que se encuentra en la tupla.

Ejemplo:

Ingrese el elemento a contar: 4

Salida: 3
"""

"""
Ejercicio 6
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dado un nombre ingresado por el usuario imprime la talla.

Ejemplo:

Ingrese un nombre: Marcelo

Salida: 1.80
"""

"""
Ejercicio 7
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dada una talla por el usuario imprima el nombre.

Ejemplo:

Ingrese una talla: 1.80

Salida: Marcelo
"""
height_p = {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}

tall_p = float(input('Ingrese una de las tallas de la persona que desea encontrar (1.80, 1.50, 1.70, 1.40): '))

for key in height_p:
    if tall_p == height_p.get((key),tall_p):
        print("La talla le corresponde a",key)

"""
Ejercicio 8
Guarde los datos de una persona (nombre,apellido,edad) en un diccionario, luego imprimalo en el siguiente formato. "Hola mi nombre es [nombre] [apellido], y tengo [edad] años.
"""


"""
"""