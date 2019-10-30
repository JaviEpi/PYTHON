# Ejercicio 14: La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
#
# Autor: Javier Epifanio López
#
# Fecha: 20/10/2019
#
# Algoritmo:
# PEDIR precio_kg_uva
# PEDIR tipo_uva
# PEDIR tamaño_uva
# SI es tipo A y tamaño 1 --> + 0.2€
# SI es tipo A y tamaño 2 --> + 0.3€
# SI es tipo B y tamaño 1 --> - 0.3€
# SI es tipo B y tamaño 2 --> - 0.5€
# MOSTRAR la ganancia obtenida
#
# Variables:
#   * precio_kg_uva
#   * tipo_uva
#   * tamaño_uva
#

# Pedimos los datos necesarios para el programa
precio_kg_uva = float(input("Precio inicial kg de la uva: "))
tipo_uva = input("Tipo de uva (A/B): ")
tamaño_uva = int(input("Tamaño de la uva (1/2): "))

# SI es tipo A y tamaño 1 --> + 0.2€
if tipo_uva == "A" and tamaño_uva == 1:
    print("La ganancia obtenida es: ", precio_kg_uva+0.2, "€")

# SI es tipo A y tamaño 2 --> + 0.3€
elif tipo_uva == "A" and tamaño_uva == 2:
    print("La ganancia obtenida es: ", precio_kg_uva+0.3, "€")

# SI es tipo B y tamaño 1 --> - 0.3€
elif tipo_uva == "B" and tamaño_uva == 1:
    print("La ganancia obtenida es: ", precio_kg_uva-0.3, "€")

# SI es tipo B y tamaño 2 --> - 0.5€
else:
    print("La ganancia obtenida es: ", precio_kg_uva-0.5, "€")