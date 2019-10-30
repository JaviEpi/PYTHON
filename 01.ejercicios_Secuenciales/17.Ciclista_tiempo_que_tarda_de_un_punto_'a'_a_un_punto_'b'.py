# Ejercicio 17: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta      # llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR hora, minutos y segundos de inicio
# PEDIR segundos que tarda en llegar a la otra ciudad
# Cálculos
# Muestro la hora de llegada
#
# Variables:
#   *hora_inicio
#   *mininutos_inicio
#   *segundos_inicio 
#   *segundos_viaje 
#

# Pedimos la hora de inicio y cuanto tiempo ha tardado en realizar el viaje
hora_inicio = int(input("Hora de salida: "))
minutos_inicio = int(input("Minutos de salida: "))
segundos_inicio = int(input("Segundos de salida: "))
segundos_viaje = int(input("Tiempo que ha tardado en segundo: "))

# Cálculos
seg_total = ((hora_inicio * 3600) + (minutos_inicio * 60) + segundos_inicio)
hora_llegada = seg_total // 3600
minutos_llegada = (seg_total % 3600) // 60
segundos_llegada = (seg_total % 3600) % 60
# Mostramos el tiempo que ha tardado del punto A al punto B
print(f"Hora de llegada {hora_llegada}:{minutos_llegada}:{segundos_llegada}")
