'''
Ejercicio 04 :Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Autor: Javier Epifanio López

Fecha: 28/10/2019

Algoritmo:


Variables:
'''
# Pedimos datos
num_1 = int(input("Introduce el número 1: "))
num_2 = int(input("Introduce el número 2: "))

# Si primer número es impar pasamos al siguiente par
if num_1 % 2 == 1:
    num_1 += 1
# Mostramos salida
for num in range(num_1, num_2 + 1, 2):
    print(f"{num} ",end="")