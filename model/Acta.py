"""
    Clase Acta en la cual se almacena la informacion de un acta,
    su ID, autor, nombre, tipo, director, jurados, nota y criterios
    que se le fueron evaluados.
"""

import json

class Acta:

    def __init__(self) -> None:
        super().__init__()

        # Datos de toda evaluacion
        self.numero = ""
        self.fecha = ""
        self.autor = ""
        self.nombre_del_trabajo = ""
        self.tipo_de_trabajo = " "
        self.directora = " "
        self.codirector = " "
        self.jurado1 = " "
        self.jurado2 = " "
        self.nota = ""

        self.criterio = {}

    def agregar_criterio(self, criterio):
        "Agrega el criterio al acta"
        self.criterio = criterio

    def agregar_nota_definitiva(self, nota):
        "Agrega la nota al acta"
        self.nota = nota

    def __str__(self) -> str:
        return json.dumps(self.__dict__)