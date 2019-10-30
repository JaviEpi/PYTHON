# Ejercicio 19: Escribe un programa que pida un número entero entre uno y doce e  # imprima el número de días que tiene el mes correspondiente.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR un número entero entre 1 y 12
# SI el número == 1, 3, 5, 7, 8, 10 o 12 --> 31 días
# SI el número == 4, 6, 9 o 11 --> 30 días
# SI el número == 2 --> 28 dias
# MOSTRAR el número de dias que tiene el mes
#
# Variables:
#   * num = número del mes (1 a 12)
#

# Pedimos el número entero entre 1 y 12
num = int(input("Número del mes: "))

# SI el número == 1 o 3 o 5 o 7 o 8 o 10 o 12 --> 31 días
if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
    print("El mes tiene 31 días")

# SI el número == 4 o 6 o 9 o 11 --> 30 días
elif num == 4 or num == 6 or num == 9 or num == 11:
    print("El mes tiene 30 días")

else:
    print("El mes tiene 28 o 29 dias")



