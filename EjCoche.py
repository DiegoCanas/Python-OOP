# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:07:11 2023

@author: dicacam
"""
obj = Coche()

    class Coche:                                                    #Identifica la clase
        
        ruedas = 4                                                  #Se definen los atributos de la clase
        
        def __init__(self, color, aceleracion):                     #Instancia
            self.color = color                                      #Se definen los atributos de la instancia
            self.aceleracion = aceleracion
            self.velocidad = 0
            
        def acelera(self):                                          #Operaciones o métodos
            self.velocidad = self.velocidad + self.aceleracion      #Se definen los métodos
            
        def frena(self):
            v = self.velocidad - self.aceleracion
            if v < 0:
                v = 0
            self.velocidad = v
            
#Heredar clase

    class CocheVolador(Coche):
        
        ruedas = 6
        
        def __init__(self, color, aceleracion, esta_volando=False):
            super().__init__(color,aceleración)                         #Super() devuelve un objeto temporal de la superclase
            self.esta_volando = esta_volando                            #que permite invocar a los métodos definidos en la misma
                                                                        #Es como incluir los valores del init anterior
        def vuela(self):
            self.esta_volando = True            
            
        def aterriza(self):
            self.esta_volando = False
            
#Funciones isinstance() e issubclass()

#isinstance(), devuelve True si el objeto es de la clase o de una de sus clases hijas
#issubclass(), true si la clase  a(primer valor) es subclase de b(segundo valor)

c = Coche('rojo', 20)
cv = CocheVolador('azul', 60)

isinstance(c, Coche)                #True
isinstance(cv, Coche)               #True
isinstance(c, CocheVolador)         #False
isinstance(cv, CocheVolador)        #True
issubclass(CocheVolador, Coche)     #True
issubclass(Coche, CocheVolador)     #False

#Python permite crear herencias múltiples

class A:
    def print_a(self):
        print('a')


class B:
    def print_b(self):
        print('b')


class C(A, B)               #Aquí está
    def print_c(self):
        print('c')


c = C()
c.print_a()
c.print_b()
c.print_c()

#Atributos Privados

class A:
    def __init__(self):
        self._contador = 0  # Este atributo es privado

    def incrementa(self):
        self._contador += 1

    def cuenta(self):
        return self._contador


class B(object):
    def __init__(self):
        self.__contador = 0  # Este atributo es privado

    def incrementa(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

#Diferencias entre poner una _ y poner dos __

class A:
    def __init__(self):
        self._contador = 0  # Este atributo es privado

    def incrementa(self):
        self._contador += 1

    def cuenta(self):
        return self._contador


class B(object):
    def __init__(self):
        self.__contador = 0  # Este atributo es privado

    def incrementa(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

#Se define en el ejemplo un atributo privado en el caso de A

>>> a = A()
>>> a.incrementa()
>>> a.incrementa()
>>> a.incrementa()
>>> print(a.cuenta())
3
>>> print(a._contador)
3

#Aunque no se debe, se puede acceder al valor

#En la clase B se define el atributo privado con doble guión

>>> b = B()
>>> b.incrementa()
>>> b.incrementa()
>>> print(b.cuenta())
2
>>> print(b.__contador)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'B' object has no attribute '__contador'
>>> print(b._B__contador)
2

#Ya no se puede acceder al atributo fuera de la clase, el identificador se ha sustituido por _B__contador


#Poliformismo: Polimorfismo es la capacidad de una entidad de referenciar en tiempo de ejecución a instancias de diferentes clases

#Ejemplo, se definen clases:

class Perro:
    def sonido(self):
        print('Guauuuuu!!!')

class Gato:
    def sonido(self):
        print('Miaaauuuu!!!')
        
class Vaca:
    def sonido(self):
        print('Múuuuuuuu!!!')

def a_cantar(animales):             #Define la funcion a cantar
    for animal in animales:         #Hace una variable animal dentro del bucle for, esta es polimorfica porque referencia a objetos de las clases, Perro, Gato, Vaca.
        animal.sonido()             #Referencia con animal.sonido

if __name__ == '__main__':          
    perro = Perro()
    gato = Gato()
    gato_2 = Gato()
    vaca = Vaca()
    perro_2 = Perro()
    granja = [perro, gato, vaca, gato_2, perro_2]   #Crea granja, sin más
    a_cantar(granja)                                #Hace que todos canten, sin más
















































































.
