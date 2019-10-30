# Ejercicio 14: Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR un numero de dos cifras
# Cálcuos --> Invertir numero
# Mostrar en pantalla
#
# Variables:
#   número
#

# Pedimos un número
numero = int(input("Introduzca un numero de dos digitos: "))

# Cálculo el número inverso
cifra_1 = int((numero % 100) / 10)
cifra_2 = numero % 10 
numero_inverso = (str(cifra_2) + str(cifra_1))

# Mostramos el resultado del invertido
print("El numero inverso es: ", numero_inverso)