from controller.biblioteca import Biblioteca
from errores.libro_exception import LibroException
from errores.socio_exception import SocioException

class MainView:

    def main(self) -> None:

        biblioteca = Biblioteca()
        print("Libros y socios cargados")

        opcion = ""

        while opcion != "8":

            self.menu()

            try:
                opcion = input("Opción: ")

                match opcion:

                    case "1":
                        self.mostrar_libros(biblioteca)

                    case "2":
                        self.mostrar_disponibles(biblioteca)

                    case "3":
                        self.buscar_libro(biblioteca)

                    case "4":
                        self.prestar_libro(biblioteca)

                    case "5":
                        self.devolver_libro(biblioteca)

                    case "6":
                        self.mostrar_prestamos(biblioteca)

                    case "7":
                        self.anadir_libro_o_socio(biblioteca)

                    case "8":
                        biblioteca.guardar_datos()
                        print("Saliendo de la biblioteca.")

                    case _:
                        print("Opción no válida.")

            except (LibroException, SocioException, ValueError) as error:
                print(f"Error: {error}")

    def menu(self) -> None:

        print("\n BIBLIOTECA ")
        print("1. Mostrar libros")
        print("2. Mostrar libros disponibles")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar préstamos")
        print("7. Añadir socio o libro")
        print("8. Salir")

    def mostrar_libros(self, biblioteca: Biblioteca) -> None:

        libros = biblioteca.mostrar_libros()

        if not libros:
            print("No hay libros registrados.")
            return

        for libro in libros:
            print(libro)

    def mostrar_disponibles(self, biblioteca: Biblioteca) -> None:

        libros_disponibles = biblioteca.mostrar_libros_disponibles()

        if not libros_disponibles:
            print("No hay libros disponibles.")
            return

        for libro in libros_disponibles:
            print(libro)

    def buscar_libro(self, biblioteca: Biblioteca) -> None:

        titulo = input("Título a buscar: ")

        libro_encontrado = biblioteca.buscar_libro(titulo)

        if libro_encontrado is not None:
            print(libro_encontrado)
        else:
            print("Libro no encontrado.")

    def prestar_libro(self, biblioteca: Biblioteca) -> None:

        codigo_libro = input("Código del libro: ")
        codigo_socio = input("Código del socio: ")

        biblioteca.prestar_libro(
            codigo_libro,
            codigo_socio
        )

        print("Libro prestado correctamente.")

    def devolver_libro(self, biblioteca: Biblioteca) -> None:

        codigo_socio = input("Código del socio: ")

        biblioteca.devolver_libro(codigo_socio)

        print("Se ha devuelto el libro correctamente.")

    def mostrar_prestamos(self, biblioteca: Biblioteca) -> None:

        prestamos = biblioteca.mostrar_prestamos()

        if not prestamos:
            print("No hay préstamos por ahora.")
            return

        for prestamo in prestamos:
            print(prestamo)

    def anadir_libro_o_socio(self, biblioteca: Biblioteca) -> None:

        opcion = input(
            "1. Añadir libro | 2. Añadir socio | 3. Volver: "
        )

        match opcion:

            case "1":
                self.anadir_libro(biblioteca)

            case "2":
                self.anadir_socio(biblioteca)

            case "3":
                print("Volviendo al menú principal.")

            case _:
                print("Opción no válida.")

    def anadir_libro(self, biblioteca: Biblioteca) -> None:

        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = input("Año: ")
        categoria = input("Categoría: ")

        biblioteca.anadir_libro(
            titulo,
            autor,
            anio,
            categoria
        )

        print("Libro añadido correctamente.")

    def anadir_socio(self, biblioteca: Biblioteca) -> None:

        nombre_socio = input("Nombre: ")
        email_socio = input("Email: ")

        biblioteca.anadir_socio(
            nombre_socio,
            email_socio
        )

        print("Socio añadido correctamente.")
