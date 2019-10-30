'''
Ejercicio 02: 

 Autor: Javier Epifanio López

 Fecha: 28/10/2019

 Algoritmo:




 Variables:
'''

# Inicializamos contadores
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

# Pedimos cantidad de números a introducir
cantidad_numumeros = int(input("¿Cuántos números vas a introducir?: "))

# Ciclo
for i in range(1,cantidad_numumeros+1):
    num = int(input(f"Número {i}: "))
    # Comprobamos si es +, - ó 0 e incrementamos contador
    if num>0:
        contador_positivos += 1
    elif num<0:
        contador_negativos += 1
    else:
        contador_ceros += 1
        
# Mostramos resultados
print("Números positivos: ", contador_positivos)
print("Números negativos: ", contador_negativos)
print("Números igual a 0: ", contador_ceros)