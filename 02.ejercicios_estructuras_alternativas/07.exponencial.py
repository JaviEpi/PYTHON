# Ejercicio 07: Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

#   El exponente sea positivo, sólo tienes que imprimir la potencia.
#   El exponente sea 0, el resultado es 1.
#   El exponente sea negativo, el resultado es 1 / potencia con el exponente       #   positivo.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR un número --> 'base'
# PEDIR un número --> 'exponente'
# SI expononente posisitivo --> mostrar la potencia
# SI exponente es 0 --> mostrar el resultado de la potencia --> 1
# SI exponente es negativp --> mostrar el resultado 1 / potencia
#
# Variables:
#   * base
#   * exponente

# Pedimos la base y el exponente
base = int(input("Valor de la base: "))
exponete = int(input("Valor del exponente: "))

# SI expononente posisitivo --> mostrar la potencia
if exponete > 0:
    print("El resultado es: ", base ** exponete)

# SI exponente es 0 --> mostrar el resultado de la potenci --> 1
if exponete == 0:
    print("El resultado es: 1")

# SI exponente es negativp --> mostrar el resultado 1 / potencia
if exponete < 0:
    print("El resultado es: ",(base ** (1 / exponete)))
