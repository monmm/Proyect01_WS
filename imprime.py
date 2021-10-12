from tabulate import tabulate

def respuesta(i, dic_o, dic_d):
	main = dic_o['main']
	name = dic_o['name']
	report = dic_o['weather']
	temp_min = main['temp_min']
	temp_max = main['temp_max']
	sensation = main['feels_like']
	humedad = main['humidity']

	prime = dic_d['main']
	nombre = dic_d['name']
	reporte = dic_d['weather']
	t_min = prime['temp_min']
	t_max = prime['temp_max']
	sen = prime['feels_like']
	hum = prime['humidity']
	
	reporte = [["Ticket %s" % (i), "Ciudad Origen", "Ciudad Destino"], 
        	["Nombre:", f"{name}", f"{nombre}"], 
         	["Descipción: ", f"{report[0]['description'].title()}", f"{reporte[0]['description'].title()}"],
         	["Temp Min||Max: ", f"{temp_min} || {temp_max} Cº", f"{t_min} || {t_max} Cº"],
         	["Sensacion: ", f"{sensation} Cº", f"{sen} Cº"],
         	["Humedad: ", f"{humedad} %", f"{hum} %"]]
	print(tabulate(reporte, headers='firstrow', tablefmt='simple', stralign='right', floatfmt='.0f'))
	print("\n")