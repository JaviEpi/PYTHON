# Ejercicio 5: Convertidor de grados Fahrenheit a grados Celsius
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR grados Fahrenheit
# CONVERTIR a  grados Celsius -->  (°F − 32) * 5 / 9
# MOSTRAR resultado
#
# Variables:
# Grados Fahrenheit
#

# Pedimos grados Fahrenheit
F = float(input("Grados Fahrenheit: "))

# Convertir de Fahrenheit a Celsius
C = (F - 32) * 5 / 9

# Mostramos el resultado en grados Celsius
print(F, "°F son", C, "°C")