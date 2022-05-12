class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        self.actas = {}    # tipo diccionario

    def agregar_acta(self, acta_obj):
        self.actas[acta_obj.numero] = acta_obj
