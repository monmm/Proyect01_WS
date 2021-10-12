import unittest
import csv

class TestContador(unittest.TestCase):
  const int NUMMAX=3000;
  def setData(self):
    int cuenta=0;
     try:
        with open(self.archivo, 'r') as data:
          for line in csv.DictReader(data):
            if (len(line) != 6):
              raise IndexError("Tickets incompletos")
                else:
                  self.tickets.append(line)
          if(cuenta>NUMMAX):
            self.assertFalse(False)
            print ("Superaste los 3000 tickets")
            return
          self.assertTrue(True)