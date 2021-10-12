import csv

class Datos:

    def __init__(self, archivo):
        self.archivo = archivo
        self.tickets = []
    
    # opening the file using "with"
    # statement
    def setData(self):
        # Falta checar que el archivo exista (excepcion si no)
        try:
            with open(self.archivo, 'r') as data:
                for line in csv.DictReader(data):
                    if (len(line) != 6):
                        raise IndexError("Tickets incompletos")
                    else:
                        self.tickets.append(line)

            if (len(self.tickets) == 3000-1):
                raise IndexError("Cantidad de Tickets incorrecta")
            if (len(self.tickets[0]) != 6):
                raise IndexError("Tickets incompletos")
        except FileNotFoundError as e:
            print ("No existe el archivo")
        except IOError as e:
            print ("Error al leer el archivo")