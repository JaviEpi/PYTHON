# Ejercicio 06: Programa que lea una cadena por teclado y compruebe si es una     
# letra mayúscula.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR la cadena
# SI la cadena --> cad >= A y cad <= Z --> mostrar la cadena es mayuscula
# SI NO mostrar la cadena no es mayuscula
#
# Variables:
#   * cad --> cadena
#

# Pedimos la cadena
cad = input("Introduce una cadena: ")

# if la cadena es una letra mayuscula muestralo y si no muestra que no es mayuscula
if len(cad)==1 and cad>="A" and cad<="Z":
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")