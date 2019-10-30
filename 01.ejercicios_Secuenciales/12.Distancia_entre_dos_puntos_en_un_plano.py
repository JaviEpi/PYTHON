# Ejercicio 12: Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR punto_1 y punto_2 (x1,y1) y (x2,y2)
# Cálculos --> distancia = str((x2-x1)**2 + (y2-y1)**2)
# MOSTRAR el resultado de la distancia entre dos puntos en un plano
#
# Variables:
#   *punto_1 (x1,y1)
#   *punto_2 (x2, y2)
#   *distancia

# Importamos la función math para hacer la raiz cuadrada
import math
# Pedimos el punto_1 y el punto_2 en el siguiente formato (x1,y1) y (x2,y2)
x1 = int(input(("Coordenada 'x' del primer punto: ")))
y1 = int(input(("Coordenada 'y' del primer punto: ")))
x2 = int(input(("Coordenada 'x' del segundo punto: ")))
y2 = int(input(("Coordenada 'y' del segundo punto: ")))

# Cálculos
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Mostramos el resultado de la distancia entre dos puntos en un plano
print(f"La distancia de estos dos punto en un plano es de: {distancia}")