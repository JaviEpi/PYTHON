# Ejercicio 20: Una compañía de transporte internacional tiene servicio en algunos 
# países de América del Norte, América Central, América del Sur, Europa y Asia. El 
# costo por el servicio de transporte se basa en el peso del paquete y la zona a  
# la que va dirigido. Lo anterior se muestra en la tabla:
#
# ZONA	UBICACIÓN	COSTO/GRAMO
# 1	América del Norte	24.00 euros
# 2	América Central	20.00 euros
# 3	América del Sur	21.00 euros
# 4	Europa	10.00 euros
# 5	Asia	18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son
# transportados, esto por cuestiones de logística y de seguridad. 
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en 
# su caso, el rechazo de la entrega.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR el peso del paquete
# PEDIR ubicación
# SI peso_paquete > 5 --> No pedidos superiores a 5kg
# SI ubicacion == "N" --> 24.00 €
# SI ubicacion == "C" --> 20.00 €
# SI ubicacion == "S" --> 21.00 €
# SI ubicacion == "E" --> 10.00 €
# SI ubicacion == "A" --> 18.00 €
# MOSTRAR el precio total del paquete
#
# Variables:
#   * peso_paquete
#   * ubivación
#

peso_paquete = float(input("El peso del paquete en Kg: "))
ubicacion = input("Zona de ubicación (N/C/S/E/A): ")


if peso_paquete > 5:
    print("Rechazo de la entrega no pedidos superiores a 5 Kg")

elif ubicacion == "N":
    print("El coste total es de: ", 24.00 * peso_paquete )
elif ubicacion == "C":
    print("El coste total es de: ", 20.00 * peso_paquete )
elif ubicacion == "S":
    print("El coste total es de: ", 21.00 * peso_paquete )
elif ubicacion == "E":
    print("El coste total es de: ", 10.00 * peso_paquete )
else:
    print("El coste total es de: ", 18.00 * peso_paquete )

