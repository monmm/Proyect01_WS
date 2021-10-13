from peticiones import Solicita
from datos import Datos
from imprime import respuesta

class Ticket:
    
    api_key = "2b0278a7ed481d119f4ffb3a34a6d97d" # api_key de @monica
    sol_key = Solicita(api_key) # inicializamos nuestra llave para OpenWeather
    bdd = Datos("dataset1.csv") # definimos nuestra base de datos
    Datos.setData(bdd) # obtenemos los datos de nuestra base de datos
    or_answer = {}
    des_answer = {}
    peticiones = {} 
    num_ticket = 1 

    def getDesCoord(self):
        """Obtiene las coordenas de la ciudad de destino.

        Devuelve en una tupla la latitud y longitud de 
        la ciudad de destino.

        Utiliza los datos del ticket -- self -- para obtener la 
        información.
    
        """
        return (self.get('destination_latitude'), self.get('destination_longitude'))

    def getOrCoord(self):
        """Obtiene las coordenas de la ciudad de origen.

        Devuelve en una tupla la latitud y longitud de 
        la ciudad de origen.

        Utiliza los datos del ticket -- self -- para obtener la 
        información.
    
        """
        return (self.get('origin_latitude'), self.get('origin_longitude'))

    """Realizamos la petición para cada ticket de nuestra lista de tickets.

    Verificamos que o hayamos hecho ya la solicitud para 
    las ciudades de origen o destino.

    Si no hemos realizado la petición,
        obtenemos las coordenadas y solicitamos la petición,
        guardando la respuesta de la API.
        Finalmente, añadimos la respuesta con el nombre de la ciudad 
        en el diccionario de peticiones.
    Si ya realizamos la petición,
        obtenemos la respuesta a la solicitud de 
        nuestra lista de peticiones realizadas.

    Por último, mandamos a imprimir la información solicitada de nuestro ticket.

    """
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
    
    # Código para verificar el número de peticiones realizadas a OpenWeather.
    # print(len(peticiones))