from peticiones import Solicita
from datos import Datos
from imprime import respuesta

class Ticket:
    
    api_key = "2b0278a7ed481d119f4ffb3a34a6d97d" # api_key de monica
    sol_key = Solicita(api_key) # inicializamos nuestra llave para OpenWeather
    bdd = Datos("dataset1.csv") # definimos nuestra base de datos
    Datos.setData(bdd) # obtenemos los datos de nuestra base de datos
    or_answer = {}
    des_answer = {}
    peticiones = {} 
    num_ticket = 1 

    def getDesCoord(self):
        return (self.get('destination_latitude'), self.get('destination_longitude'))

    def getOrCoord(self):
        return (self.get('origin_latitude'), self.get('origin_longitude'))

    for ticket in bdd.tickets:
        if ticket.get('origin') not in peticiones.keys():
            coord = getOrCoord(ticket)
            or_answer = Solicita.cityRequest(sol_key, ticket.get('origin'), coord)
            peticiones.setdefault(ticket.get('origin'), or_answer)            
        else:
            or_answer = peticiones.get(ticket.get('origin'))

        if ticket.get('destination') not in peticiones:
            coord = getDesCoord(ticket)
            des_answer = Solicita.coordRequest(sol_key, coord)
            peticiones.setdefault(ticket.get('destination'), des_answer)
        else:
            des_answer = peticiones.get(ticket.get('destination'))

        respuesta(num_ticket, or_answer, des_answer)
        num_ticket += 1 
    # Verificamos la cantidad de peticiones realizadas a OpenWeather
    print(len(peticiones))