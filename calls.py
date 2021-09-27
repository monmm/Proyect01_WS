"""
Finding the current weather of any city using OpenWeatherMap API
Tutorial followed: https://www.tutorialspoint.com/
@monmm
"""

# We need requests module for the HTTP requests and JSON module to work with the response.
import requests, json, time

# example call = api.openweathermap.org/data/2.5/weather?q={City}&appid={API_key}
api_key = "2b0278a7ed481d119f4ffb3a34a6d97d"	
head_url = "https://api.openweathermap.org/data/2.5/weather?"
# &units=metric - We change the standard units, Kelvin to Celsius.
# &lang=es - Spanish translation for the city name and description fields.
tail_url = "&units=metric&lang=es"

"""
1st call {Origin: TLC, Latitude: 19.3371, Longitude: -99.566 
		  Destination: MTY, Latitude: 25.7785, Longitude: -100.107}
"""

# Calling by name
city = "Toluca"
city_url = head_url + "q=%s&appid=%s" % (city, api_key) + tail_url 
# HTTP request. Look at the last comment to better understand what requests gives us.
response = requests.get(city_url)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   main = data['main']
   name = data['name']
   temperature = main['temp']
   sensation = main['feels_like']
   report = data['weather']
   print("\n")
   print(f"Destination City: {name}")
   print(f"Weather Report: {report[0]['description'].title()}")
   print(f"Temperature: {temperature}" + " Celsius")
   print(f"Sensation: {sensation}" + " Celsius")
else:
   print("Error en la solicitud")
# Taking care of threads and calls.
time.sleep(1)

# Calling by coordinates
lat = "25.7785"
lon = "-100.107"
coord_url = head_url + "lat=%s&lon=%s&appid=%s" % (lat, lon, api_key) + tail_url
response = requests.get(coord_url)
if response.status_code == 200:
   data = response.json()
   main = data['main']
   name = data['name']
   temperature = main['temp']
   sensation = main['feels_like']
   report = data['weather']
   print("\n")
   print(f"Origin City: {name}")
   print(f"Weather Report: {report[0]['description'].title()}")
   print(f"Temperature: {temperature}" + " Celsius")
   print(f"Sensation: {sensation}" + " Celsius")
else:
   print("Error en la solicitud")

"""
Example of the request answer

{'coord': 
	{'lon': -99.1277, 
	 'lat': 19.4285},
 'weather': 
 	[{'id': 803, 
 	  'main': 'Clouds', 
 	  'description': 'broken clouds', 
 	  'icon': '04d'}], 
 'base': 'stations',
 'main': {'temp': 295.87, 
 	  'feels_like': 295.4, 
 	  'temp_min': 291.4, 
 	  'temp_max': 297.1, 
 	  'pressure': 1017, 
 	  'humidity': 46}, 
 'visibility': 10000, 
 'wind': {'speed': 2.68, 'deg': 320}, 
 'clouds': {'all': 57}, 
 'dt': 1632693662, 
 'sys': {'type': 2, 
 	 'id': 47729, 
	 'country': 'MX', 
	 'sunrise': 1632659171, 
	 'sunset': 1632702552},
 'timezone': -18000, 
 'id': 3530597, 
 'name': 'Mexico City', 
 'cod': 200}
"""