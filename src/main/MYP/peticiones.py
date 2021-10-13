# Importamos -request- para realizar las solicitudes HTTP y-json- para trabajar con la respuesta.
# -time- nos permite introducir un retraso en la ejecución de nuestro programa.
# Con -sys- generamos la excepción SystemExit con el que Python sale sin imprimir el seguimiento de pila.
import requests, json, time, sys

class Solicita:

   # Hacemos un poco de trampa 'traduciendo' los códigos de los aeropuertos.
   codigos_aero = {'TLC':'Toluca', 'MTY':'Monterrey', 'MEX':'Ciudad de México', 'TAM':'Tampico', 
               'GDL':'Guadalajara', 'CJS':'Ciudad Juárez', 'CUN':'Cancún', 'TIJ':'Tijuana', 
               'HMO':'Hermosillo', 'CME':'Campeche', 'MID':'Mérida', 'CTM':'Chetumal', 
               'VER':'Veracruz', 'OAX':'Oaxaca', 'HUX':'Huatulco', 'ZIH':'Ixtapa', 
               'PVR':'Puerto Vallarta', 'LIM':'Lima', 'HAV':'La Habana', 'BOG':'Bogotá', 
               'MIA':'Miami', 'LAX':'Los Ángeles', 'JFK':'Nueva York', 'TRC':'Torreón', 
               'PXM':'Puerto Escondido', 'ACA':'Acapulco', 'MZT':'Mazatlán', 'GUA':'Guatemala', 
               'AGU':'Aguascalientes', 'VSA':'Villahermosa', 'BZE':'Ciudad de Belice', 'DFW':'Dallas', 
               'CZM':'Cozumel', 'ORD':'Chicago', 'PHX':'Phoenix', 'CUU':'Chihuahua', 
               'QRO':'Querétaro', 'BJX':'León', 'PBC':'Puebla', 'PHL':'Filadelfia', 
               'SLP':'San Luis Potosí', 'CLT':'Douglas', 'YYZ':'Mississauga', 'IAH':'Houston', 
               'YVR':'Vancouver', 'CDG':'Paris', 'ZCL':'Zacatecas', 'AMS':'Ámsterdam', 
               'ATL':'Georgia', 'CEN':'Ciudad Obregón', 'MAD':'Madrid', 'SCL':'Santiago'}

   head_url = "https://api.openweathermap.org/data/2.5/weather?"
   tail_url = "&units=metric&lang=es"
   response = ""
   city = ""
   latitude = ""
   longitude = ""
   data = {} # diccionario para guardar la respuesta de la API

   def __init__(self, key):
      """Inicializamos nuestra llave para la API.

        Parámetros:
        key -- llave de OpenWeather

      """
      self.api_key = key

   def coordRequest(self, coords):
      """Realiza una petición a la API por coordenadas

      Regresa los datos metereológicos actuales de una ubicación 
      por coordenadas llamando a la API con el url correspondiente 
      creado a partir de los datos obtenidos como parámetros.

      Usamos:
      time.sleep()-- para asegurarnos de hacer solo una petición por segundo.

      Parámetros:
      coords -- coordenadas de nuestra ciudad requerida

      Excepciones:
      TypeError -- Si nuestras coordenadas no son tipo string
      ConnectionError -- Si ocurre algún error al solicitar a la API

      """
      self.latitude = coords[0]
      self.longitude = coords[1]
      if not isinstance(self.latitude, str) and not isinstance(self.longitude, str):
         raise TypeError
      else:
         coord_url = self.head_url + "lat=%s&lon=%s&appid=%s" % (self.latitude, self.longitude, self.api_key) + self.tail_url
         try: 
            self.response = requests.get(coord_url)
            self.data = self.response.json()
            time.sleep(1)
         except requests.ConnectionError:
            print ("Error de conexión")
            sys.exit(1)
         else:
            return self.data

   def cityRequest(self, name, coords):
      """Realiza una petición a la API por nombre de ciudad.

      Traduce el código de aeropuerto y regresa los datos metereológicos 
      actuales de una ubicación por nombre de ciudad llamando a la API 
      con el url correspondiente creado a partir de los datos obtenidos 
      como parámetros.

      Si no es posible obtener una respuesta, realiza la petición por coordenadas.

      Usamos:
      time.sleep()-- para asegurarnos de hacer solo una petición por segundo.

      Parámetros:
      name -- nombre de la ciudad requerida
      coords -- coordenadas de nuestra ciudad requerida

      Excepciones:
      TypeError -- Si el nombre no es de tipo string
      ValueError -- Si el código tiene más de tre carácteres
    
      """
      if not isinstance(name, str):
         raise TypeError
      if (len(name) != 3):
         raise ValueError('Código de ciudad incorrecto')
      else:
         self.city = self.codigos_aero.get(name)
         city_url = self.head_url + "q=%s&appid=%s" % (self.city, self.api_key) + self.tail_url
         self.response = requests.get(city_url)
         if self.response.status_code == 200:
            self.data = self.response.json()
            time.sleep(1)
            return self.data
         else:
            self.coordRequest(self, coords)
      