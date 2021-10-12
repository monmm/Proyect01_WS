"""
Test class
@monmm
"""
import unittest
from datos import Datos

class TestDatos(unittest.TestCase):
    
    bdd_ch = Datos("dataset.csv")
    bdd_in = Datos("data.csv")
    bdd_x = Datos("nofile.csv")
    

    def test_setData(self):
        # Verificamos la salida con un archivo inexistente
        with self.assertRaises(FileNotFoundError) as exception_info:
            Datos.setData(self.bdd_x)
        assert str(exception_info.exception) == 'No existe el archivo'
        self.assertEqual(exception_info.exception.code, 1)
        # Verificamos la salida cuando no teneos permisos de lectura
        with self.assertRaises(FileNotFoundError) as exception_info:
            Datos.setData(self.bdd_x)
        assert str(exception_info.exception) == 'No existe el archivo'
        self.assertEqual(exception_info.exception.code, 1)
        # Verificamos la salida cuando los campos de los tickets están incompletos
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_ch)
        assert str(exception_info.exception) == 'Tickets incompletos'
        # Verificamos la salida cuando tenemos un número distinto a 3 mil tickets
        with self.assertRaises(SystemExit) as exception_info:
            Datos.setData(self.bdd_ch)
        assert str(exception_info.exception) == 'Cantidad de Tickets incorrecta'       

    if __name__ == "__main__":
        unittest.main()
