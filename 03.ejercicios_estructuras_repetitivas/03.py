'''
Ejercicio 03: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

Autor: Javier Epifanio López

Fecha: 28/10/2019

Algoritmo:
    Pedimos letra
    Comprobamos si es vocal --> y lo mostramos
    Comprobamos si es consonante --> y lo mostramos
    si es espacio salir



Variables:
    *letra
'''
letra = input("Letra: ")
while letra != (" "):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Vocal")
    else:
        print ("Consonante")

    letra = input("Letra: ")
