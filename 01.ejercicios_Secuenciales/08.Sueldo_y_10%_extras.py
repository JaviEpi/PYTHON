# Ejercicio 8: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
#
# Autor: Javier Epifanio López
#
# Fecha: 09/10/2019
#
# Algoritmo:
# PEDIR sueldo
# PEDIR venta_1
# PEDIR venta_2
# PEDIR venta_3
# Cálculos comisiones --> (10/100 * venta 1) + (10/100 * venta 2) + (10/100 * venta 3)
# Cálculos --> sueldo + comisiones
# Mostrar la comisión
# Mostrar el sueldo total --> (sueldo mensual + comisiones mensuales)
#
# Variables:
# Sueldo   
# Venta 1
# Venta 2
# Venta 3
#

# Pedimos el sueldo, venta_1, venta_2, venta_3
sueldo = float(input("Sueldo mensual del vendedor: "))
venta_1 = float(input("Primera venta: "))
venta_2 = float(input("Segunda venta: "))
venta_3 = float(input("Tercera venta: "))

# Cálculos
comisiones = 10/100 * (venta_1 + venta_2 + venta_3)
sueldo_total = sueldo + comisiones

# Mostrar comisiones y el sueldo total(sueldo mensual + comisiones mensuales)
print(f"Comisión mensual sobre las ventas: {comisiones} €")
print(f"Sueldo total mensual: {sueldo_total} €")