# Ejercicio 15: El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
#
# Autor: Javier Epifanio López
#
# Fecha: 20/10/2019
#
# Algoritmo:
# PEDIR el numero que va al viaje
# SI num_alumnos >= 100 --> 65€
# SI num_alumnos < 99 and num_alumnos >= 50 --> 70€
# SI num_alumnos < 49 and num_alumnos >= 30 --> 95€
# SI num_alumnos < 100 --> 
# MOSTRAR el precio total
#
# Variables:
#   * num_alumnos
#

# Pedimos el numero de alumnos que iran al viaje
num_alumnos = int(input("Número total de alumnos que asistiran al viaje: "))

# SI num_alumnos >= 100 --> 65€
if num_alumnos >= 100:
    print("El coste por el número de alumnos es de: 65€, y el coste del autobus es de: ",4000/num_alumnos,"El total del viaje es de: ",65+4000/num_alumnos, "€")

# SI num_alumnos < 99 and num_alumnos >= 50 --> 70€
elif num_alumnos < 99 and num_alumnos >= 50:
    print("El coste por el número de alumnos es de: 70€, y el coste del autobus es de: ",4000/num_alumnos,"El total del viaje es de: ",70+4000/num_alumnos, "€")

# SI num_alumnos < 49 and num_alumnos >= 30 --> 95€
elif num_alumnos < 49 and num_alumnos >= 30:
    print("El coste por el número de alumnos es de: 95€, y el coste del autobus es de: ",4000/num_alumnos,"El total del viaje es de: ",95+4000/num_alumnos, "€")
# SI num_alumnos < 100 --> 
else:
   print("El coste por el número de alumnos es de: 95€, y el coste del autobus es de: ",4000/num_alumnos,"El total del viaje es de: ",95+4000/num_alumnos, "€")