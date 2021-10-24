import unittest
from sys import path
path.append("../..")
from src.main.MYP.peticiones import Solicita
import requests

class TestSolicita(unittest.TestCase):

    s = Solicita("bb7b3c191ef83a5993c4a01589eeab2c")
    r = s.cityRequest("MTY", (0,0))
    v = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=25.7785&lon=-100.107&appid=bb7b3c191ef83a5993c4a01589eeab2c").json()
    lat = 25.7785
    lon =  -100.107

    def test_city_request(self):
        """Test para las peticiones por ciudad.

        Verificamos que se lance la excepción correspondiente 
        con un código de ciudad incorrecto.

        Excepciones a verificar:
        TypeError -- cuando el valor no es una cadena
        ValueError -- cuando el código no es de 3 carateres
    
        """
        self.assertRaises(TypeError,Solicita.cityRequest,self,10)
        with self.assertRaises(ValueError) as exception_info:
            Solicita.cityRequest(self,"MILAN", (0,0))
        assert str(exception_info.exception) == 'Código de ciudad incorrecto'

    def test_coord_request(self):
        """Test para las peticiones por coordenadas.

        Verificamos que se lance la excepción correspondiente 
        cuando nuestras coordenadas no son correctas.

        Excepciones a verificar:
        TypeError -- cuando el valor de la longitud o la latitud 
        no son una cadena    
        """
        self.assertEquals (self.lat,self.v['coord']['lat']) 
        self.assertEquals (self.lon,self.v['coord']['lon']) 
        self.assertRaises(TypeError,Solicita.cityRequest,10)

    if __name__ == "__main__":
        unittest.main()