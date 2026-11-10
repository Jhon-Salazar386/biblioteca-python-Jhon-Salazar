from datetime import datetime

from modelo.libro import Libro
from modelo.socio import Socio

RUTA_LIBROS = "./gestor/datos_libros.txt"
RUTA_SOCIOS = "./gestor/datos_socios.txt"
RUTA_LOG = "./gestor/log.txt"

def cargar_libros():

    libros = []

    with open(RUTA_LIBROS, "r", encoding="utf-8") as fichero:

        for linea in fichero:

            try:

                datos_libro = linea.strip().split(";")

                libro = Libro(datos_libro[1], datos_libro[2], int(datos_libro[3]), datos_libro[4], None if datos_libro[5] == "None" else datos_libro[5])

                libros.append(libro)

            except Exception as e:
                raise Exception(e)

    return libros

def cargar_socios():

    socios = []

    with open(RUTA_SOCIOS, "r", encoding="utf-8") as fichero:

        for linea in fichero:

            try:

                datos_socio = linea.strip().split(";")

                socio = Socio(datos_socio[1], datos_socio[2], None if datos_socio [3] == "None" else datos_socio [3])

                socios.append(socio)

            except Exception as e:
                raise Exception(e)
            
    return socios

def guardar_libros(libros):

    with open(RUTA_LIBROS, "w", encoding="utf-8") as fichero:

        for libro in libros:

            socio = libro.codigo_de_socio if libro.codigo_de_socio else "None"

            fichero.write(f"{libro.codigo};{libro.titulo};{libro.autor};" f"{libro.anio};{libro.categoria};{socio}\n")

def guardar_socios(socios):

    with open(RUTA_SOCIOS, "w", encoding="utf-8") as fichero:

        for socio in socios:

            fichero.write(f"{socio.codigo};{socio.nombre};" f"{socio.email};{socio.codigo_libro_prestado or 'None'}\n")

def registrar_evento(evento, detalles):

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(RUTA_LOG, "a", encoding="utf-8") as fichero:

        fichero.write(f"[{fecha}][{evento}][{detalles}]\n")
