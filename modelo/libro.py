class Libro:

    contador_libros = 0

    def __init__(self, titulo, autor, anio, categoria, codigo_de_socio=None):

        self.__class__.contador_libros += 1
        
        self.codigo = self.contador_libros
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_de_socio = codigo_de_socio

    def esta_disponible(self):
        return self.codigo_de_socio is None

    def __str__(self):
        return (f"Codigo de libro: {self.codigo}\n"
                f"Titulo: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Año: {self.anio}\n"
                f"Categoria: {self.categoria}\n"
                f"Disponible: {self.esta_disponible()}\n")
