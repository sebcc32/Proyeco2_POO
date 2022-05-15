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
        self.criterio = criterio

    def agregar_nota_definitiva(self, nota):
        self.nota = nota

    def __str__(self) -> str:
        return json.dumps(self.__dict__)