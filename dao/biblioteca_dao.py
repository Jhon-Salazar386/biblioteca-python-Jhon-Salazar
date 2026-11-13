from gestor.gestor_ficheros import (
    cargar_libros,
    cargar_socios,
    guardar_libros,
    guardar_socios,
    registrar_evento
)

class BibliotecaDAO:

    def cargar_libros(self):
        return cargar_libros()

    def cargar_socios(self):
        return cargar_socios()

    def guardar_libros(self, libros):
        guardar_libros(libros)

    def guardar_socios(self, socios):
        guardar_socios(socios)

    def registrar_evento(self, evento, detalles):
        registrar_evento(evento, detalles)
