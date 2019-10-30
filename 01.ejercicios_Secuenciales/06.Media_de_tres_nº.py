# Ejercicio 6: Programa que hace la media a tres números
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR un número
# PEDIR un número
# PEDIR un número
# Cálcuos --> (a + b + c)/ 3
# 
# Variables:
#   a <-- número al azar
#   b <-- número al azar
#   c <-- número al azar
#

# Pedir los tres números 
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

# Cálculos
media = (a + b + c)/ 3

# Mostramos en pantalla la media de los tres números
print("La media de los tres números es: ", media)