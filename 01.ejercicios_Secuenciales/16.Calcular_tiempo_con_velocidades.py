# Ejercicio 16: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que # está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos 
# (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo # más rápido al otro.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# Leer las dos velocidades y la distancia (no puedo controlar que v1 > v2.
# Calcular tiempo --> (v=s/t), por lo tanto t=s/v --> Tiempo = distancia / (v1-v2)
# Cálculos --> El tiempo hay que pasarlo a minútos --> minutos = Tiempo * 60
# Mostrar tiempo
#
# Variables:
#   *velocidad_1 
#   *velocidad_2   
#   *distancia
#

# Pedimos las variables y la distancia
velocidad_1 = float(input("Velocidad del primer vehículo en km/h: "))
velocidad_2 = float(input("Velocidad del segundo vehículo, que tiene que ser inferior al del primer vehículo en km/h: "))
distancia = float(input("Distancia recorrida por ambos vehículos en metros: "))

# Hacemos los calculos y pasamos el tiempo a minutos
tiempo = distancia / (velocidad_1 - velocidad_2)
tiempo_minutos = tiempo * 60

# Mostramos el tiempo en minutos
print("El tiempo que tarda en recorrer la distancia es de ", tiempo_minutos, "minutos")