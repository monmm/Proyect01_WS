# Importamos -csv- para llamar a DictReader y mapear la información de cada fila a un diccionario.
# Con -sys- generamos la excepción SystemExit con el que Python sale sin imprimir el seguimiento de pila.
import csv, sys

class Datos:

    def __init__(self, archivo):
        """Cargamos nuestros datos (tickets).

        Asignamos el nombre de nuestro archivo e
        Inicializamos una lista para guardar nuestros tickets.

        Parámetros:
        archivo -- nombre del archivo de nuestra base de datos

        """
        self.archivo = archivo
        self.tickets = []
    
    def setData(self):
        """Obtenemos nuestros tickets.

        Lee el archivo y guarda cada fila (ticket) en un diccionario
        cuyas claves son dadas por la primera fila de nuestro csv.
        Verifica que los campos de cada ticket esten completos y
        luego guarda cada ticket en nuestra lista de tickets.

        Finalmente verifica que hayamos recibido 3000 tickets.

        Excepciones:
        SystemExit -- Si los campos de algun ticket no están completos
        FileNotFoundError -- Si no existe el archivo
        IOError -- Si ocurre algun error de lectura
        SystemExit -- Si no contamos con 3000 tickets
    
        """
        try:
            with open(self.archivo, 'r') as data:
                for line in csv.DictReader(data):
                    if (('' in line.values()) == True):
                        sys.exit("Tickets incompletos")
                    else:
                        self.tickets.append(line)
        except FileNotFoundError as e:
            sys.exit("Algo salió mal con el archivo")
        except IOError as e:
            sys.exit("Algo salió mal con el archivo")

        if (len(self.tickets) != 3000):
            sys.exit("Cantidad de Tickets incorrecta")
            