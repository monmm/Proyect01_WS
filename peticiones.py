# We need requests module for the HTTP requests and JSON module to work with the response.
#from typing import KeysView
import requests, time, json

class Solicita:

   ciudades = {'TLC':'Toluca', 'MTY':'Monterrey', 'MEX':'Ciudad de México', 'TAM':'Tampico', 
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
   data = {}
   latitude = ""
   longitude = ""

   def __init__(self, key):
      self.api_key = key

   def coordRequest(self, coords):
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
         else:
            return self.data

   def cityRequest(self, name, coords):
      if not isinstance(name, str):
         raise TypeError
      if (len(name) != 3):
         raise ValueError('Código de ciudad incorrecto')
      else:
         self.city = self.ciudades.get(name)
         city_url = self.head_url + "q=%s&appid=%s" % (self.city, self.api_key) + self.tail_url
         self.response = requests.get(city_url)
         if self.response.status_code == 200:
            self.data = self.response.json()
            time.sleep(1)
            return self.data
         else:
            self.coordRequest(self, coords)
      