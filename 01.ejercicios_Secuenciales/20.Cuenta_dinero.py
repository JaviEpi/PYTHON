# Ejercicio 20: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas # monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos). 
#
# Autor: Javier Epifanio López
#
# Fecha: 10/10/2019
#
# Algoritmo:
# PEDIR monedas de 2€
# PEDIR monedas de 1€
# PEDIR monedas de 50 cent.
# PEDIR monedas de 20 cent.
# PEDIR monedas de 10 cent.
# Cálculos
# MOSTRAR el total en euros y centimos
#
# Variables:
#   * Monedas_2€
#   * Monedas_1€
#   * Monedas_50cent
#   * Monedas_20cent
#   * Monedas_10cent
#

# Pedimos el numero de monedas de 2€, 1€, 50 centimos, 20 centimos o 10 centimos.
Monedas_2euros = float(input("Numero de monedas de 2€: "))
Monedas_1euros = float(input("Numero de monedas de 1€: "))
Monedas_50cent = float(input("Numero de monedas de 50 centimos: "))
Monedas_20cent = float(input("Numero de monedas de 20 centimos: "))
Monedas_10cent = float(input("Numero de monedas de 10 centimos: "))

# Cálculos
total_euros = (Monedas_2euros * 2 + Monedas_1euros * 1 + Monedas_50cent * 0.5 + Monedas_20cent * 0.2 + Monedas_10cent * 0.1)

# Mostramos el total de euros
print("Tengo ", total_euros, "€")