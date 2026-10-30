class LibroException(Exception):
    def __init__(self, mensaje, valor_error):
        self.valor_error = valor_error
        super().__init__(mensaje)
