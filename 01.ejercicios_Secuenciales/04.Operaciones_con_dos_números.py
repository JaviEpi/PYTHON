# Ejercicio 4: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR un número
# PEDIR un número
# SUMAR --> a + b
# RESTAR --> a - b
# MULTIPLICAR --> a * b
# Dividir --> a / b
# Variables:
#   *Número 1
#   *Número 2
#

# Pedimos los números
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

# Cálculos
suma = a + b
resta = a - b
multiplicación = a * b
división = a / b

# Mostramos los resultados
print("Resultado suma: ", suma)
print("Resultado resta: ", resta)
print("Resultado multiplicación: ", multiplicación)
print("Resultado división: ", división)