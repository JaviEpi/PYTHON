# Ejercicio 15: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables. 
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR variables 'a' y 'b'
# Intercambiar valores
# Mostrar solución
#
# Variables:
#   *a: variable 'a'
#   *b: variable 'b'
#

# Pedimos el valor de las variables 'a' y 'b'
a = int(input("Valor de la variable 'a': "))
b = int(input("Valor de la variable 'b': "))

# Intercambiamos el valor de las variables
a,b = b,a

# Mostramos en pantalla el valor de las variables intercambiadas
print("Valor de 'a' intercamiado: ", a)
print("Valor de 'b' intercamiado: ", b)