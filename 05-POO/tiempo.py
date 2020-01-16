'''
1. Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

t = Tiempo(1, 20, 30)

donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente. 

Crea métodos para:

Sumar y restar otro objeto de la clase Tiempo.
Sumar y restar segundos, minutos y/o horas.
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
'''


class Tiempo:

    '''
    Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

    t = Tiempo(1, 20, 30)

    donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.
    '''
    #Se crea el constructor
    def __init__(self, horas, minutos, segundos):
        """
        Construcutor de la clase.
        lanza una excepción en caso de valores incorrectos.
        :param horas:
        :param minutos:
        :param segundos:
        """
        assert horas>= 0 and 0<=minutos<60 and 0<=minutos<60
        #si estamos aqui se cumple lo anterior y los valores son correctos
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    #propiedades

    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos
    
    @property
    def segundos(self):
        return self.__segundos


    def __str__(self):
        return f"{self.horas}h {self.minutos}m {self.segundos}s"

    #Sumar y restar horas
    def suma_horas (self, horas):
        '''
        Suma horas al objeto. Si el objeto es negativo lanza una excepción.
        :param horas:
        return
    
        '''
        assert self.horas + horas <= 0
        self.__horas += horas

    def resta_horas (self, horas):
        '''
        Suma horas al objeto. Si el objeto es negativo lanza una excepción.
        :param horas:
        return
    
        '''
        # self.suma_horas(-horas) También se puede hacer así
        assert self.horas - horas <= 0
        self.__horas -= horas
    # Sumar y restar minutos
    def suma_minutos(self, minutos):
        '''
        Suma mimutos al objeto. Si el objeto es negativo lanza una excepción.
        :param minutos:
        return
        '''
        seg = Tiempo.__segundos_total(self) + minutos * 60
        assert seg => 0
        resultado = Tiempo.segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = resultado.horas, resultado.minutos, resultado.minutos

    @staticmethod
    def __segundos_total(t):
        return t.horas*3600 + t.minutos*60 + t.segundos
    
    @staticmethod
    def __segundos_a_tiempo(s):
        return t.horas*3600 + t.minutos*60 + t.segundos

    if __name__ == '__main__':
        t1 = Tiempo(10,10,10)
        print(f"T1:{t1}")

    
        
    
