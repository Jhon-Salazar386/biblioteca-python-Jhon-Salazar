class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, codigo_de_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_de_socio = codigo_de_socio

    def esta_disponible(self):
        return self.codigo_de_socio is None

    def __str__(self):
        return (f"Libro: {self.codigo}\n"
                f"Titulo: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Año: {self.anio}\n"
                f"Categoria: {self.categoria}\n"
                f"Codigo de socio: {self.codigo_de_socio}")
