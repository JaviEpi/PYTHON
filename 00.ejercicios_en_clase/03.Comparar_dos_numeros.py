# Ejercicio 3: Comparar dos numeros, para saber que número es mayor.
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
#

# Pedimos los datos numéricos 'a' y 'b'
a = float(input("Valor de 'a': "))
b = float(input("Valor de 'b': "))

#Cálculos
if a > b:
    print (f"El valor mayor es {a}")
else:
    print(f"El valor mayor es {b}")
