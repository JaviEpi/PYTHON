# Ejercicio 19: Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta  # correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR numero de preguntas
# PEDIR numero de preguntas correctas
# PEDIR numero de preguntas incorrectas
# PEDIR numero de preguntas en blanco
# Cálculos para hallar la nota final
# MOSTRAR la nota final
#
# Variables:
#   * numero_preguntas
#   * preguntas_correctas
#   * preguntas_incorrectas
#   * preguntas_blanco
#

# Pedimos el total de pregunta 
numero_preguntas = int(input("Número de preguntas: "))
preguntas_correctas = int(input("Número de preguntas correctas: "))
preguntas_incorrectas = int(input("Número de preguntas incorrectas: "))
preguntas_blanco = int(input("Número de preguntas en blanco: "))

# Cálculos para hallar la nota final
nota_maxima = numero_preguntas * 5
nota_final = (preguntas_correctas * 5 + preguntas_incorrectas * -1 + preguntas_blanco * 0)

# Mostramos la nota final
print("La nota final es ", nota_final, "de", nota_maxima)