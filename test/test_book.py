import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Knjiga

class TestKnjiga(unittest.TestCase):
    def test_knjiga_inicijalizacija(self):
        knjiga = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
        self.assertEqual(knjiga.naslov, "Harry Potter")
        self.assertEqual(knjiga.autor, "J.K. Rowling")
        self.assertEqual(knjiga.godina_izdavanja, 1997)
        self.assertEqual(knjiga.žanr, "Fantasy")
    
       
    def test_knjiga_inicijalizacija(self):
        knjiga = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
        self.assertEqual(knjiga.display_info(), "Harry Potter, J.K. Rowling, 1997, Fantasy")
        
if __name__ == '__main__':
    unittest.main()