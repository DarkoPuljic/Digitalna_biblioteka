import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Biblioteka
from book import Knjiga

class Test_Libary(unittest.TestCase):
    def test_cuvanje_knjige(self):
        b = Knjiga("dd", "dd", 167, "dd")
        b2 = Knjiga("dd", "dd", 167, "dd")
        l = Biblioteka()
        l.dodaj_knjigu(b)
        l.dodaj_knjigu(b2)
        self.assertEqual(len(l.lista_knjiga), 2)

if __name__ == '__main__':
   unittest.main()