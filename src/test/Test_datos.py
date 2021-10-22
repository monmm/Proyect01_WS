import unittest
from sys import path
path.append("../..")
from src.main.MYP.datos import Datos

class TestDatos(unittest.TestCase):

    bdd_ch = Datos("src/test/data_test/dataset.csv")
    bdd_in = Datos("src/test/data_test/data.csv")
    bdd_x = Datos("nofile.csv")
    

    def test_setData(self):
        # Verificamos la salida con un archivo inexistente    
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_x)
        self.assertEqual ("Algo salió mal con el archivo", str(exception_info.exception))    
        
        # Verificamos la salida cuando los campos de los tickets están incompletos        
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_in)
        self.assertEqual ('Tickets incompletos', str(exception_info.exception))
        
        # Verificamos la salida cuando tenemos un número distinto a 3 mil tickets
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_ch)
        assert str(exception_info.exception) == 'Cantidad de Tickets incorrecta'
        

    if __name__ == "__main__":
        unittest.main()
