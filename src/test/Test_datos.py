import unittest
from sys import path
path.append("../..")
from src.main.MYP.datos import Datos

class TestDatos(unittest.TestCase):

    bdd_ch = Datos("src/test/data_test/dataset.csv")
    bdd_in = Datos("src/test/data_test/data.csv")
    bdd_x = Datos("nofile.csv")
    

    def test_setData(self):
        """Test para los datos recibidos (tickets).

        Verificamos que se lance la excepción correspondiente 
        con un archivo inexistente,    
        cuando los campos de los tickets están incompletos y
        cuando tenemos un número distinto a 3 mil tickets.

        Excepciones a verificar:
        SystemExit
    
        """         
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_x)
        self.assertEqual ("Algo salió mal con el archivo", str(exception_info.exception))    
                 
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_in)
        self.assertEqual ('Tickets incompletos', str(exception_info.exception))
        
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_ch)
        assert str(exception_info.exception) == 'Cantidad de Tickets incorrecta'
        

    if __name__ == "__main__":
        unittest.main()
