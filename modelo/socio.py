class Socio:

    contador_socios = 0

    def __init__(self, nombre, email, codigo_libro_prestado = None):
        
        self.__class__.contador_socios += 1
        
        self.codigo = self.contador_socios
        self.nombre = nombre
        self.email = email
        self.codigo_libro_prestado = codigo_libro_prestado

    def tiene_libro_prestado(self):
        return self.codigo_libro_prestado is not None

    def __str__(self):
        return (f"Codigo de socio: {self.codigo}\n"
                f"Nombre: {self.nombre}\n"
                f"Email: {self.email}\n"
                f"Codigo libro prestado: {self.codigo_libro_prestado or "Sin libro"}\n")
