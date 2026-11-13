from modelo.libro import Libro
from modelo.socio import Socio
from dao.biblioteca_dao import BibliotecaDAO
from errores.libro_exception import LibroException
from errores.socio_exception import SocioException

class Biblioteca:

    def __init__(self):
        self.dao = BibliotecaDAO()
        self.libros = self.dao.cargar_libros()
        self.socios = self.dao.cargar_socios()

    def mostrar_libros(self):
        return self.libros.copy()

    def mostrar_libros_disponibles(self):

        disponibles = []

        for libro in self.libros:
            if libro.esta_disponible():
                disponibles.append(libro)

        return disponibles

    def buscar_libro(self, titulo):

        if not titulo.strip():
            raise LibroException("El titulo no pued estar vacio")

        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                return libro

        return None

    def prestar_libro(self, codigo_libro, codigo_socio):

        try:
            codigo_libro = int(codigo_libro)
            codigo_socio = int(codigo_socio)

        except ValueError:
            raise ValueError("El valor debe ser un numero entero")

        libro = next((l for l in self.libros if l.codigo == codigo_libro),None)

        socio = next((s for s in self.socios if s.codigo == codigo_socio), None)

        if libro is None:
            raise LibroException("Libro inexistente", codigo_libro)

        if socio is None:
            raise SocioException("Socio inexistente", codigo_socio)

        if not libro.esta_disponible():
            raise LibroException("Libro prestado", codigo_libro)

        if socio.codigo_libro_prestado is not None:
            raise SocioException("Socio ya tiene un libro", codigo_socio)

        libro.codigo_de_socio = socio.codigo
        socio.codigo_libro_prestado = libro.codigo

        self.dao.registrar_evento("PRESTAMO", f"Socio {socio.codigo}, libro {libro.codigo}")

        return True

    def devolver_libro(self, codigo_socio):

        try:
            codigo_socio = int(codigo_socio)

        except ValueError:
            raise ValueError("El valor debe ser un numero entero")

        socio = next((s for s in self.socios if s.codigo == codigo_socio), None)

        if socio is None:
            raise SocioException("Socio inexistente", codigo_socio)

        if socio.codigo_libro_prestado is None:
            raise SocioException("No tiene libros prestados", codigo_socio)

        codigo_libro = socio.codigo_libro_prestado

        libro = next((l for l in self.libros if l.codigo == codigo_libro), None)

        if libro is None:
            raise LibroException("Libro asociado al préstamo inexistente", codigo_libro)

        if libro.codigo_de_socio != socio.codigo:
            raise LibroException("El libro no pertenece al socio", codigo_libro)

        libro.codigo_de_socio = None
        socio.codigo_libro_prestado = None

        self.dao.registrar_evento("DEVOLUCION", f"Socio {socio.codigo}, libro {codigo_libro}")

        return True

    def mostrar_prestamos(self):

        prestamos = []

        for socio in self.socios:
            if socio.codigo_libro_prestado is not None:

                for libro in self.libros:
                    if libro.codigo == socio.codigo_libro_prestado:
                        prestamo = f"{socio.nombre} -> {libro.titulo}"
                        prestamos.append(prestamo)

        return prestamos

    def anadir_libro(self, titulo, autor, anio, categoria):

        if not titulo.strip():
            raise LibroException("El título no puede estar vacío")

        if not autor.strip():
            raise LibroException("El autor no puede estar vacío")

        if not categoria.strip():
            raise LibroException("La categoría no puede estar vacía")

        try:
            anio = int(anio)

        except ValueError:
            raise ValueError("Campo debe ser de tipo numero entero")

        if anio <= 0:
            raise LibroException("El año debe ser positivo")

        libro = Libro(titulo, autor, anio, categoria)

        self.libros.append(libro)

        return True

    def anadir_socio(self, nombre_socio, email_socio):

        if not nombre_socio.strip():
            raise SocioException("El nombre no puede estar vacío")

        if not email_socio.strip():
            raise SocioException("El email no puede estar vacío")

        socio = Socio(nombre_socio, email_socio)

        self.socios.append(socio)

        return True

    def guardar_datos(self):

        self.dao.guardar_libros(self.libros)
        self.dao.guardar_socios(self.socios)

        return True
