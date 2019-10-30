# Ejercicio 11: Programa que lea 3 datos de entrada A, B y C. Estos corresponden a 
# las dimensiones de los lados de un triángulo. El programa debe determinar que 
# tipo de triangulo es, teniendo en cuenta los siguiente:
#   Si se cumple Pitágoras entonces es triángulo rectángulo
#   Si sólo dos lados del triángulo son iguales entonces es isósceles.
#   Si los 3 lados son iguales entonces es equilátero.
#   Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR los lados del triangulo
# Cálculos
# MOSTRAR el tipo de triangulo 
#
# Variables:
#   * lado_a
#   * lado_b
#   * lado_c
#

import math

# Pedimos datos
lado_a = float(input("Introduce longitud lado A: "))
lado_b = float(input("Introduce longitud lado B: "))
lado_c = float(input("Introduce longitud lado C: "))

# Cálculamos si el triangulo es equilátero y lo mostramos 
if lado_a == lado_b and lado_a == lado_c:
    print("El triángulo es Equilatero")
else:
    # Cálculamos si el triangulo es rectángulo y lo mostramos 
    if ((lado_a**2 + lado_b**2) == lado_c**2) or ((lado_a**2 + lado_c**2) == lado_b**2) or ((lado_b**2 + lado_c)**2 == lado_a**2):
        print("El triángulo es Rectángulo")

    # Cálculamos si el triangulo es isósceles y lo mostramos 
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("El triángulo es Isóceles")

    # Cálculamos si el triangulo es escaleno y lo mostramos
    else:
        print("El triángulo es Escaleno")