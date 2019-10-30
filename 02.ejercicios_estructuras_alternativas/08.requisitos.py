# Ejercicio 08: Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ 
# y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es
# mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero
# el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se
# debe mostrar ‘NO ACEPTADA’.
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR la nota que ha  obtenido
# PEDIR la edad que tiene
# PEDIR el sexo
# Si la nota >= 5 and edad >= 18 and sexo == F --> MOSTRAR ACEPTADA
# Si la nota >= 5 and edad >= 18 and sexo == H --> MOSTRAR POSIBLR
# Si NO  cumple una de ellas --> MOSTRAR NO ACEPTADA
#
# Variables:
#   * nota
#   * edad
#   * sexo
#

# Pedimos los datos que necesitamos
nota = float(input("Nota obtenida: "))
edad = int(input("Edad: "))
sexo = input("Sexo (H/M): ")

# Si la nota >= 5 and edad >= 18 and sexo == F --> ACEPTADA
if nota >= 5 and edad >= 18 and sexo == "M":
    print("ACEPTADA")

# Si la nota >= 5 and edad >= 18 and sexo == H --> POSIBLE
elif nota >= 5 and edad >= 18 and sexo == "H":
    print("POSIBLE")
# Si no cumple una de ellas --> NO ACEPTADA
else:
    print("NO ACEPTADA")