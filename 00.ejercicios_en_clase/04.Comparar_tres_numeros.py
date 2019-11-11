# Ejercicio 4: Comparar tres numeros, para saber que número es mayor.
#
# Autor: Javier Epifanio López
#
# Fecha: 16/10/2019
#
# Algoritmo:
# PEDIR un número 'a'
# PEDIR un número 'b'
# Cálculos --> a > b
# SI 'a' es mayor MOSTRAR a
# SI NO MOSTRAR 'b'
#
# Variables:
#   * 'a' --> numérico
#   * 'b' --> numérico
#   * 'c' --> numérico

# Pedimos los datos numéricos 'a' y 'b'
a = float(input("Valor de 'a': "))
b = float(input("Valor de 'b': "))
c = float(input("Valor de 'c': "))

#Cálculos y mostramos en pantalla el valor mayor de los tres
if a >= b and a >= c:
   print(f"el valor mayor es: {a}")
if b >= a and b >= c:
   print(f"el valor mayor es: {b}")
if c >= a and c >= b:
   print(f"el valor mayor es: {c}")