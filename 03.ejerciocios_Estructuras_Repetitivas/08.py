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

'''
horas = 0
minutos = 0
segundos = 0

while True:
    print(f"{horas:02} : {minutos:02} : {segundos:02}", end="")
    time.sleep(1)

    if segundos < 59:
        segundos += 1
    else:
        segundos = 0
        if minutos < 59:
            minutos = 1
        else:
            minutos = 0
            horas += 1
    print(0 * "\b", end="")       
'''
print("Cronómetro iniciado")

for horas in range(0,24):
    for minutos in range(0,60):
        for segundos in range(0,60):
            print(f"{horas:02}:{minutos:02}:{segundos:02}")
            time.sleep(1)