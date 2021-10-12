import csv, sys

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
                        print("Tickets incompletos")
                        sys.exit(1)
                    else:
                        self.tickets.append(line)
        except FileNotFoundError as e:
            print ("No existe el archivo")
            sys.exit(1)
        except IOError as e:
            print ("Error al leer el archivo")
            sys.exit(1)

        if (len(self.tickets) != 3000-1):
            print("Cantidad de Tickets incorrecta")
            sys.exit(1)
        for n in self.tickets:
            if (('' in n.values()) == True):
                print("Tickets incompletos")
                sys.exit(1)