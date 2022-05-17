import json

""""
    Clase Criterio, en la cual se almacena la informacion de los criterios,
    su nombre, observaciones, notas por cada jurado y el ponderado de esta.
"""

class Criterio:

    def __init__(self) -> None:
        self.descripcion = ""
        self.observacion = " "
        self.nota1 = " "
        self.nota2 = " "
        self.ponderado = " "

    def __str__(self) -> None:
        return json.dump(self.__dict__)
