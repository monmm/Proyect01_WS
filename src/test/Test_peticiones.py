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
        self.assertRaises(TypeError,Solicita.cityRequest,self,10)
        with self.assertRaises(ValueError) as exception_info:
            Solicita.cityRequest(self,"MILAN", (0,0))
        assert str(exception_info.exception) == 'Código de ciudad incorrecto'

    def test_coord_request(self):
        self.assertEqual (self.lat,self.v['coord']['lat']) 
        self.assertEqual (self.lon,self.v['coord']['lon']) 
        self.assertRaises(TypeError,Solicita.cityRequest,10)

    if __name__ == "__main__":
        unittest.main()