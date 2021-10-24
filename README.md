# Proyect01_WS

## Reporte de Clima

*Aplicación en la línea de comandos para mostrar el reporte del clima para 3 mil tickets de avión, escrita en Python.*

### Prerequisitos

-  Python
-  PyPI - tabulate

Asegúrese de de tener `python3` y `pip` en su computadora:

```sh
$ sudo apt-get install python3-pip
```

Luego, debe instalar la paquetería de tabulate:

```sh
$ pip install tabulate
```

### Ejecutar el Programa

Para ejecutar el programa sólo debe escribir en la línea de comandos:

```sh
$ python3 src/main/MYP/tickets.py
```

### Ejemplo

```sh
$ python3 tickets.py

             Ticket 1      Ciudad Origen     Ciudad Destino
        --------------  -----------------  -----------------
               Nombre:             Toluca    Las Ladrilleras
           Descipción:      Algo De Nubes    Nubes Dispersas
        Temp Min||Max:  17.97 || 21.09 Cº  28.67 || 33.14 Cº
            Sensacion:           17.46 Cº           32.24 Cº
              Humedad:               39 %               52 %


             Ticket 2      Ciudad Origen     Ciudad Destino
        --------------  -----------------  -----------------
               Nombre:        Mexico City    Las Ladrilleras
           Descipción:        Cielo Claro    Nubes Dispersas
        Temp Min||Max:  20.83 || 23.95 Cº  28.67 || 33.14 Cº
            Sensacion:           21.55 Cº           32.24 Cº
              Humedad:               29 %               52 %
``` 

### Pruebas unitarias

Para ejecutar los test del programa sólo debe escribir en la línea de comandos:

```
$ python3 -m unittest discover src/test/ -p "*.py"
```

