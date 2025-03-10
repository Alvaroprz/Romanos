class Tarta:
 
     def __init__(self, sabor: str, puntuacion: int = 0) -> None:
         self.sabor = sabor
         self.puntos = puntuacion
 
     def __str__(self) -> str:
         return f'{self.sabor}'
         return f'{self.sabor}({self.puntos})'
 
     def __repr__(self):
         return self.__str__()
 
 
"""
 - Almacenar las tartas
 - Almacenar las tartas                  DONE!
 - Puedo agregar una tarta               DONE!
 - Saber cuál es la tarta "ganadora"
 - Puedo agregar una tarta
 
 Mejora:
 - Agregar varias tartas a la vez
 - Vaciar la lista de tartas
"""
 
 
class CataTartas:
 
     def __init__(self):
         self.tartas = []
 
     def agregarObjetoTarta(self, tarta: Tarta) -> None:
        def agregar_objeto_tarta(self, tarta: Tarta) -> None:
         if not isinstance(tarta, Tarta):
             raise TypeError('No es una tarta!')
         self.tartas.append(tarta)
 
     def agregarTarta(self, sabor: str, puntuacion: int) -> None:
        def agregar_tarta(self, sabor: str, puntuacion: int) -> None:
         nueva_tarta = Tarta(sabor, puntuacion)
         self.tartas.append(nueva_tarta)
         # self.agregarObjetoTarta(nueva_tarta)
 
     def obtener_mejor_tarta(self) -> Tarta:
         mejor = None
         for tarta in self.tartas:
             if mejor is None or tarta.puntos > mejor.puntos:
                 mejor = tarta
         return mejor
 
     def __str__(self):
         resultado = ''
         for tarta in self.tartas:
             if resultado != '':
                 resultado = resultado + ', '
             resultado = resultado + str(tarta)
 
         return resultado
 
     def __repr__(self):
         return self.__str__()