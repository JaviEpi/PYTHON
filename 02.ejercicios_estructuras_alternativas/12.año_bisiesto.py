# Pedimos el año
año = int(input("Introduce el año: "))
if año % 4 == 0:
    if año % 100 != 0:
        print("El año ", año, " es bisiesto")
    elif año % 400 == 0:
        print("El año ", año, " es bisiesto")
    else:
        print("El año ", año, " no es bisiesto")
else:
    print("El año ", año, " no es bisiesto")