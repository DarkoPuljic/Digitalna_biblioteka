import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Biblioteka
from book import Knjiga

class Test_Libary(unittest.TestCase):
    def test_cuvanje_knjige(self):
        knjiga1 = Knjiga("Naslov", "Autor", 1, "Zanr")
        knjiga2 = Knjiga("1984", "Džordž Orvel", 1949, "Fantastika")
        biblioteka = Biblioteka()
        biblioteka.dodaj_knjigu(knjiga1)
        biblioteka.dodaj_knjigu(knjiga2)
        self.assertEqual(len(biblioteka.lista_knjiga), 2)

if __name__ == '__main__':
   unittest.main()