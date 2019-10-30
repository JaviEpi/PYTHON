# Ejercicio 18: Realiza un programa que pida el día de la semana (del 1 al 7) y   
# escriba el día correspondiente. Si introducimos otro número nos da un error.
#
# Autor: Javier Epifanio López
#
# Fecha: 20/10/2019
#
# Algoritmo
# PEDIR un número entero entre 1 y 12
# SI el número == 1 día --> Lunes
# SI el número == 2 día --> Martes
# SI el número == 3 dia --> Miercoles
# SI el número == 4 día --> Jueves
# SI el número == 5 día --> Viernes
# SI el número == 6 dia --> Sábado
# SI el número == 7 dia --> Domingo
# MOSTRAR el día de la semana
#
# Variables:
#   * num = número día de la semana (1 a 7)
#

# Pedimos el número entero entre 1 y 12
num = int(input("Número día de la semana (1-7): "))

# SI el número == 1 --> Lunes
if num == 1:
    print("Lunes")

# SI el número == 2 día --> Martes
if num == 2:
    print("Martes")

# SI el número == 3 día --> Martes
if num == 3:
    print("Miércoles")

# SI el número == 4 día --> Miércoles   
if num == 4:
    print("Jueves")

# SI el número == 5 día --> Viernes
if num == 5:
    print("Viernes")

# SI el número == 6 día --> Sábado 
if num == 6:
    print("Sábado")

# SI el número == 7 día --> Domingo
if num == 7:
    print("Domingo")

if num > 7:
    print("Error cada semana tiene 7 días")
if num < 1:
    print("Error cada semana tiene 7 días")
