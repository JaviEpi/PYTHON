# Ejercicio 13: Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR un número
# Cálculos raiz cuadrada --> str(número)
# Cálculos raíz cúbica --> numero**(1/3)
#
# Variables:
#   número
#

# Importamos la función math para la raíz cuadrada
import math
# Pedimos un número
numero = float(input("Valor de un número: "))

# Cálculos
raiz_cuadrada = math.sqrt(numero)
raiz_cubica = (numero ** (1/3))

# Mostramos los resultados
print (f"Resultado de la raíz cuadrada: {raiz_cuadrada}")
print (f"Resultado de la raíz cúbica: {raiz_cubica}")