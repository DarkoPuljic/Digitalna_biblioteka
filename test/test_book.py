import unittest
import sys
sys.path.append(r'C:\Users\Darko\Desktop\Darko Puljić Projekat\src')
from book import Knjiga

class TestKnjiga(unittest.TestCase):
    def test_knjiga_inicijalizacija(self):
        knjiga = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
        self.assertEqual(knjiga.naslov, "Harry Potter")
        self.assertEqual(knjiga.autor, "J.K. Rowling")
        self.assertEqual(knjiga.godina_izdavanja, 1997)
        self.assertEqual(knjiga.zanr, "Fantasy")
class TestKnjiga2(unittest.TestCase):
    def test_knjiga_inicijalizacija(self):
        knjiga = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
        self.assertEqual(knjiga.naslov, "Harry Potter")
        self.assertEqual(knjiga.autor, "J.K. Rowling")
        self.assertEqual(knjiga.godina_izdavanja, 1997)
        self.assertEqual(knjiga.zanr, "Fantasy")

if __name__ == '__main__':
    unittest.main()