# Ejercicio 9: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá # pagar finalmente por su compra.
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR total compra
# Cálculos --> descuento = 15/100 * total_compra
# Cálculos --> precio_final = total_compra - descuento
#
# Variables:
#   Total_compra
#   

# Pedimos el total de la compra
total_compra = float(input("Total de la compra: "))

# Cálculo el 15% del total de la compra
descuento = total_compra * 15/100
precio_final = total_compra - descuento
 
# Mostrar el precio final
print(f"El precio final de la compra es de {precio_final} €")