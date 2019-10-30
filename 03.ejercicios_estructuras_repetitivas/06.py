'''
Ejercicio 06: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

Autor: Javier Epifanio López

Fecha: 28/10/2019

Algoritmo:
    PEDIR la base 
    PEDIR el exponente
    POTENCIA = 1
    Cálculos
    Mostramos en pantalla

Variables:
    * base
    * exponente
    * potencia
'''

base = float(input("Base: "))
exponente = int(input("Exponente: "))
potencia = 1

for cont in range (1, exponente + 1):
    potencia = potencia * base
print("Potencia = ", potencia)

