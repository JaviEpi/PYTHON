'''
Ejercicio 09: Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Autor: Javier Epifanio López

Fecha: 29/10/2019

Algoritmo:
    PEDIR cuántos números quieren que se muestren de números primos 
    Cálcalumos si es primo
    Si son primos se añaden a una lista
    Se muestran la lista de números primos que hemos pedido
    Si el número que hemos pedido es negativo devolvemos que introduzca un valor positivo

Variables:
    * n,cont = 4,2
    num = valor de números primos que queramos que se muestren en pantalla
'''
#Pedimos un número 
n,cont = 4,2
num=int(input("¿Cuántos números primos quieren que se muestren?: "))
# Cálculamos si es primo y creamos una lista de los números primos
if(num>2):
    cad = "2 - 3"
    while cont < num:
        i=2
    while i<=n:
        if(i==n):
            cad= cad+" - "+str(i)
            cont=cont+1
        else:
            if(n % i ==0):
                i=n
                i=i+1
                n=n+1
                print(cad)
else:
    if(num>0):
        if(num==1):
            print("es primo 2")
        else:
            print("es primo 2, 3") 
    else:
        print("Ingrese un número positivo")