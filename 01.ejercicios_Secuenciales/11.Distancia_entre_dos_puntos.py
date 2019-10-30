# Ejercicio 11: Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR numero_1 y numero_2
# Cálculos --> distancia = (numero_2 - numero_1)
# MOSTRAR resultado
# Variables:
#   *numero_1
#   *numero_2

# Pedimos numero_1 y numero_2
numero_1 = int(input("Valor número 1: "))
numero_2 = int(input("Valor número 2: "))

# Cálculos
distancia = abs(numero_2 - numero_1)

# Mostramos el resultado de la distancia entre dos puntos
print("La distancia entre estos dos puntos es: ", distancia)
