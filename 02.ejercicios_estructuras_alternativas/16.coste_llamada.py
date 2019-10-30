# Ejercicio 16: La política de cobro de una compañía telefónica es: cuando se 
# realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que 
# los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los
# siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. 
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en 
# turno 
# de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar
# cuánto debe pagar por cada concepto una persona que realiza una llamada.
#
# Autor: Javier Epifanio López
#
# Fecha: 20/10/2019
#
# Algoritmo:
# PEDIR tiempo llamada
# PEDIR si la llama es en domingo
# SI la llamada no es en domingo PEDIR si es por la M o T
# Cálculos coste de la llamada
# MOSTRAR el coste total de la llamada
#
# Variables:
#   * tiempo_llamada
#   * domingo
#   * coste
#

# Pedimos los datos necesarios
tiempo_llamada = int(input("¿Cuánto tiempo es la llamada?: "))
domingo = input("¿Es Domingo? (S/N): ")
# Si no es domingo preguntar si es por la mañana o por la tarde
if domingo.upper()=="N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ")

# Cálculamos cuanto le va a costar la llamada dependiendo del tiempo
if tiempo_llamada<=5:
    coste = tiempo_llamada*100
elif tiempo_llamada<=8:
    coste = (tiempo_llamada-5)*80+500
elif tiempo_llamada<=10:
    coste = (tiempo_llamada-8)*70+240+500
else:
    coste = (tiempo_llamada-10)*50+140+240+500
# Calculamos el total de la llamada el coste de la llamada + el impuesto 
if domingo.upper()=="S":
    coste += coste*0.03
elif turno.upper()=="M":
    coste += coste*0.15
else:
    coste += coste*0.10

# Mostramos el coste total de la llamada
print("El coste de la llamada:",coste/100,"euros.")