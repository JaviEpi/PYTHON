'''
Ejercicio 08: Hacer un programa que muestre un crono¡ómetro, indicando las horas, minutos y segundos.

Autor: Javier Epifanio López

Fecha: 28/10/2019

Algoritmo:
    Importamos la función time
    Mostramos en pantalla que se inicia el cronómetro
    Damos el rango de las horas, minutos y segundos
    Mostramos en pantalla el resultado de uno en uno

Variables: 
    * h = horas
    * m = minutos
    * s = segundos
'''

import time

print("Cronómetro iniciado")

for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            print(f"Hora: {h} Minuto: {m} Segundo:{s}")
            time.sleep(1)