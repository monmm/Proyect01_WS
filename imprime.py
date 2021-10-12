# Usamos -tabulate- para imprimir tablas de manera estética.
from tabulate import tabulate

def respuesta(i, dic_o, dic_d):
	"""Imprime el reporte del tiempo de un ticket.

    Obtiene las propiedas que nos interesan de la ciudad de origen 
	y la ciudad de destino y las organiza en una lista para darle 
	formato e imprimir el reporte dentro de una tabla.

    Parámetros:
    i -- número de ticket
    dic_o -- diccionario con la respuesta de origen
    dic_d -- diccionario con la respuesta de destino
    
    """
	data_or = dic_o['main']
	name = dic_o['name']
	report = dic_o['weather']
	temp_min = data_or['temp_min']
	temp_max = data_or['temp_max']
	sensation = data_or['feels_like']
	humedad = data_or['humidity']

	data_des = dic_d['main']
	nombre = dic_d['name']
	reporte = dic_d['weather']
	t_min = data_des['temp_min']
	t_max = data_des['temp_max']
	sen = data_des['feels_like']
	hum = data_des['humidity']
	
	reporte = [["Ticket %s" % (i), "Ciudad Origen", "Ciudad Destino"], 
        	["Nombre:", f"{name}", f"{nombre}"], 
         	["Descipción: ", f"{report[0]['description'].title()}", f"{reporte[0]['description'].title()}"],
         	["Temp Min||Max: ", f"{temp_min} || {temp_max} Cº", f"{t_min} || {t_max} Cº"],
         	["Sensacion: ", f"{sensation} Cº", f"{sen} Cº"],
         	["Humedad: ", f"{humedad} %", f"{hum} %"]]

	print(tabulate(reporte, headers='firstrow', tablefmt='simple', stralign='right', floatfmt='.0f'))
	print("\n")