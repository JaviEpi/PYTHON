# Ejercicio 3: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR cateto 1 
# PEDIR cateto 2
# Hipotenusa --> raiz cuadrada de c1**2 + c2**2
# Variables:
#   *Cateto1
#   *Cateto2
#

# Importamos la función math
import math

# Pedimos los valores de los catetos
c1 = float(input("Valor del cateto 1: "))
c2 = float(input("Valor del cateto 2: "))

# Cálculos --> hipotenusa**2 = ((c1**2)+(c2**2))
hipotenusa = math.sqrt((c1**2)+(c2**2))

# Mostramos resultado
print("La hipotenusa es: ", hipotenusa)