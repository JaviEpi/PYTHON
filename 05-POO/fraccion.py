import math

class Fraccion:
    #Constructor
    def __init__(self,numerador,denominador):
        self.__numerador=numerador
        self.__denominador=denominador
  
    #get y set del numerador   
    @property
    def numerador(self):
        return self.__numerador
  
    @numerador.setter
    def numerador(self,valor):
        self.numerador=valor
  
    #get y set del denominador   
    @property
    def denominador(self):
        return self.__denominador
  
    @denominador.setter
    def denominador(self,valor):
        self.denominador=valor   
    
    '''
    Devuelve el valor de la fraccion
    '''        
    def getValor(self):
        return self.numerador()/self.denominador()
  
    '''
    Multiplica la fraccion actual
    por un numero escalar
    @param numero
    '''   
    def multiplicaPorNumero(self,numero):
        numerador(numerador()*numero)
    '''
    Calcula el comun denominador
    @param numerador2 numerador de la segunda fraccion 
    @param denominador2 denominador de la segunda fraccion  
    '''      
    def comunDenominador(self,numerador2,denominador2):
        if denominador()<denominador2:
            denominador(denominador2)
            numerador((denominador2/denominador())*numerador2())
        else:
            denominador(denominador2)
            numerador(denominador()/denominador2)*numerador() 
    '''
    Suma dos fracciones
    @param numerador2 numerador de la segunda fraccion 
    @param denominador2 denominador de la segunda fraccion  
    '''           
    def sumar(self,numerador2,denominador2):
        self.comunDenominador(numerador2,denominador2)
        numerador(numerador()+numerador2) 
      
    '''
    Restar dos fracciones
    @param numerador2 numerador de la segunda fraccion 
    @param denominador2 denominador de la segunda fraccion  
    '''       
    def restar(self,numerador2,denominador2):
        self.sumar(self,numerador2*-1,denominador2*-1) 
        
    '''
    Multiplicar dos fracciones
    @param numerador2 numerador de la segunda fraccion 
    @param denominador2 denominador de la segunda fraccion 
    '''
    def multiplicar(self,numerador2,denominador2):
        numerador(numerador()*numerador2)
        denominador(denominador()*denominador2)
      
  
    '''
    simplifica la fraccion
    @param numerador 
    @param denominador 
    '''      
    def simplificar(self,numerador,denominador):
        simplificador=self.mcm(numerador,denominador)
        numerador(numerador()/simplificador)
        denominador(denominador()/simplificador)
    
    def __str__(self):
        print(numerador()+"/"+denominador())
if __name__ == "__main__":
    numerador=input("Introduce el numerador> ")
    denominador=input("Introduce el denominador> ")
    fraccion=Fraccion(numerador,denominador)
    print("Sumamos 1/2> ")
    fraccion.sumar(1,2)
    fraccion()
    print("Restamos 1/4> ")
    fraccion.restar(1,4)
    fraccion()