

"""

# Ejercicio 1. Tartas

## Enunciado

Como se acerca mi cumpleaños, estoy tratando de hacer varias tartas para ver cuál me gusta más.

Crea una clase `Tarta` que permita almacenar el sabor y una puntuación de 0 a 5.

## Ayuda a la implementación

- Para crear la tarta solamente es necesario identificar el sabor.
- La puntuación inicial será 0 y se puede modificar una vez creada la tarta mediante un atributo.

Puedes comprobar si una tarta te gusta más que otra comparando los valores de sus atributos puntuacion.


## Segunda parte (extra)

- Crea una lista con cinco tartas.
- Da a cada una una puntuación.
- Haz una función que tomando la lista de tartas devuelva
  la tarta con mayor puntuación

¿Qué pasa si en lugar de una función creo una clase `CataTartas` (o `ListaTartas`)?

"""

"""
class Tarta:

    def __init__(self, sabor: str, puntos: int = 0):
        self.sabor = sabor
        self.setPuntos(puntos)

    def getPuntos(self):
        return self.__puntos

    def setPuntos(self, puntos):
        if 0 <= puntos <= 5:
            self.__puntos = puntos
        else:
            raise ValueError('La puntuación de la tarta debe ser entre 0 y 5')


tarta = Tarta('chocolate')
print(tarta.sabor, tarta.getPuntos())

tarta.setPuntos(5)
print(tarta.sabor, tarta.getPuntos())


fresa = Tarta('fresa', 6)
print(fresa.sabor, fresa.getPuntos())
"""

class Tarta:
    def __int__(self, sabor:str, puntuacion:int=0)->None:
        self.sabor = sabor
        self.puntos = puntuacion

tartas = [
    Tarta("fresa", 3),
    Tarta("chocolate", 4),
    Tarta("Tres chocolates", 5),
    Tarta("Queso", 4),
    Tarta("Whisky", 2)
]

def mejor_tarta(tartas):
    mejor = None

    for tarta in tartas:
        if mejor is None or tarta.puntos > mejor.puntos:
            mejor = tarta
    return mejor

resultado = mejor_tarta(tartas)
print(resultado)