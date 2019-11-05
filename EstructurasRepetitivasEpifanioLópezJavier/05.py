'''
Ejercicio 05: Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
    La suma de los números que están dentro del intervalo (intervalo abierto).
    Cuantos números están fuera del intervalo.
    Informa si hemos introducido algún número igual a los límites del intervalo.

 Autor: Javier Epifanio López

 Fecha: 28/10/2019

 Algoritmo:




 Variables:
    * cont_fuera_intervalo = 0
    * igual_limites = False
    * sema_dentro_intervalo = 0
'''

# Variables para el programa
cont_fuera_intervalo = 0
igual_limites = False
suma_dentro_intervalo = 0

# Comprobamos que el limite inferior es menor que el limite superior
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    if limite_inferior>limite_superior:
        print("ERROR: El límite inferior debe ser menor que el superior.")
    if not (limite_inferior>limite_superior): break

# Proceso
num = int(input("Introduce un número (0, para salir): "))
while num!=0:
    # Pertenece al intervalo
    if num > limite_inferior and num < limite_superior:
        suma_dentro_intervalo += num
    else:
    # No pertenece al intervalo
        cont_fuera_intervalo+=1

    # Número igual a alguno de los límites
    if num == limite_inferior or num == limite_superior:
        igual_limites = True
    num = int(input("Introduce un número (0, para salir): "))

# Resultados
print("La suma de los número dentro del intervalo es", suma_dentro_intervalo)
print("La cantidad de números fuera del intervalo es", cont_fuera_intervalo) 

if igual_limites:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")