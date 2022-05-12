import json

class Criterio:

    def __init__(self) -> None:
        self.descripcion = ""
        self.observacion = " "
        self.nota1 = " "
        self.nota2 = " "
        self.ponderado = " "

    def __str__(self) -> None:
        return json.dump(self.__dict__)
