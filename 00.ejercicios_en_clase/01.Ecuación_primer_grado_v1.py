    # Ejercicio : Resolver una ecuación de primer grado.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# LEER a,b
# x <-- -b/a
# ESCRIBIR x
# Variables:
#   *a y b: coeficientes de x y termino independiente
#

print("Resolución de una ecuación de 1er tipo 'ax+b=0'")
print("---------------------------------------------- ")

# Pedimos datos
a = float(input("Valor de 'a' (coeficiente x)-------- :"))
b = float(input("Valor de 'b' (término independiente) :"))

# Cálculos
if a!=0:
    x = -b/a
    # Mostramos el resultado de la ecuación de primer grado si a != 0
    print("El resultado de la ecuación de primer grado es: ", x)

# Mostramos el resultado de la ecuación de primer grado si a = 0
if a==0:
    print("La ecuación no solución")