'''
Ejercicio 02: Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Autor: Javier Epifanio López

Fecha: 28/10/2019

Algoritmo: 
    PEDIR cantidad de numeros a introducir
    Comprobar uno a uno si el número es positivo --> Si lo es añadir a contador positivo
    Comprobar uno a uno si el número es negativo --> Si lo es añadir a contador negativo
    Comprobar uno a uno si el número es cero     --> Si lo es añadir a contador cero
    Mostrar el número de números positivos, negativos y ceros



Variables:
    * contador_positivos
    * contador_negativos
    * contador_ceros
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