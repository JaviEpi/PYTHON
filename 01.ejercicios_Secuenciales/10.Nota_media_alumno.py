# Ejercicio 10: Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se # compone de los siguientes porcentajes:
#
#   *55% del promedio de sus tres calificaciones parciales.
#
#   *30% de la calificación del examen final.
#
#   *15% de la calificación de un trabajo final.
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR nota examen_parcial_1
# PEDIR nota examen_parcial_2
# PEDIR nota examen_parcial_3
# PEDIR nota examen_final
# PEDIR nota trabajo_final
# Cálculos --> [(examen_parcial_1 + examen_parcial_2 + examen_parcial_3) / 3] * 55/100
# Cálculos --> examen_final * 30/100
# Cálculos --> trabajo_final * 15/100
# Cálculos --> Sumo las tres notas
# Mostrar el resultado
#
# Variables:
#   examen_parcial_1
#   examen_parcial_2
#   examen_parcial_3
#   examen_final
#   trabajo_final
#

# Pedimos los datos necesarios (examenes_parciales, examen final y trabajo_final)
examen_parcial_1 = float(input("Nota examen parcial 1: "))
examen_parcial_2 = float(input("Nota examen parcial 2: "))
examen_parcial_3 = float(input("Nota examen parcial 3: "))
examen_final = float(input("Nota examen final: "))
trabajo_final = float(input("Nota trabajo final: "))

# Cálculo la media de la nota
# Cálculo el 55% de la nota media de los tres examenes_parciales
porcentaje_examenes_parciales = 0.55 * ((examen_parcial_1 + examen_parcial_2 + examen_parcial_3) / 3)

# Cálculo el porcentaje del examen_final
porcentaje_examen_final =  0.3 * examen_final

# Cálculo el porcentaje del trabajo_final
porcentaje_trabajo_final = 0.15 * trabajo_final 

# Mostramos la nota final del alumno
print(f"La nota final es de: {porcentaje_examenes_parciales + porcentaje_examen_final + porcentaje_trabajo_final}")
