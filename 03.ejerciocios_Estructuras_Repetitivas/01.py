'''
Ejercicio 01: Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

 Autor: Javier Epifanio López

 Fecha: 28/10/2019

 Algoritmo:




 Variables:
'''
import random

# Constantes
intentos_maximos = 10

# Inicializamos
intentos = 0
numero_adivinar = random.randrange(1,100)

# Proceso
while True: #Ciclo postcondición
    numero = int(input("Te quedan " + str(10 - intentos) + " intentos. " + 
    "Introduce un número entre 1 y 100: "))
    intentos += 1
    if numero < numero_adivinar:
        print(f"{numero} es menor que número a adivinar")
    else:
        print(f"{numero} es mayor que número a adivinar")
    if numero == numero_adivinar or intentos == intentos_maximos:
        break
# Mostramos resultado
if numero == numero_adivinar:
    print (f"Has adivinado el número en {intentos} intentos")
else:
    print (f"Has consumido el máximo de intentos, el número a adivinar era {numero_adivinar}")




