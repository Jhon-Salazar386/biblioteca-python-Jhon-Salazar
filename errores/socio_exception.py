class SocioException(Exception):
    def __init__(self, mensaje, valor):
        self.valor = valor
        super().__init__(mensaje)
