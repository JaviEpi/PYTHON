# Ejercicio 17: Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis      caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará
# el mensaje: “ERROR: número incorrecto.”.
# Ejemplo:
# 
#   Introduzca número del dado: 5
#   En la cara opuesta está el "dos"
#
# Autor: Javier Epifanio López
#
# Fecha: 17/10/2019
#
# Algoritmo:
# PEDIR numero que ha salido del dado
# SI num_dado == 1 --> En la cara opuesta esta el 6
# SI num_dado == 2 --> En la cara opuesta esta el 5
# SI num_dado == 3 --> En la cara opuesta esta el 4
# SI num_dado == 4 --> En la cara opuesta esta el 3
# SI num_dado == 5 --> En la cara opuesta esta el 2
# SI num_dado == 6 --> En la cara opuesta esta el 1
# SI el numero no esta entre el 1 o el 6 ERROR
#
# Variables:
#   * num_dado 
#

# PEDIR el resultado del dado
num_dado = int(input("Número obtenido del dado: "))

# SI num_dado == 1 --> En la cara opuesta esta el 6
if num_dado == 1:
    print("En la cara opuesta esta el 6")

# SI num_dado == 1 --> En la cara opuesta esta el 5
elif num_dado == 2:
    print("En la cara opuesta esta el 5")

# SI num_dado == 1 --> En la cara opuesta esta el 4
elif num_dado == 3:
    print("En la cara opuesta esta el 4")

# SI num_dado == 1 --> En la cara opuesta esta el 3
elif num_dado == 4:
    print("En la cara opuesta esta el 3")

# SI num_dado == 1 --> En la cara opuesta esta el 2
elif num_dado == 5:
    print("En la cara opuesta esta el 2")

# SI num_dado == 1 --> En la cara opuesta esta el 1
elif num_dado == 6:
    print("En la cara opuesta esta el 1")

# SI el numero no esta entre el 1 o el 6 ERROR
else:
    print("ERROR: Número incorrecto")

