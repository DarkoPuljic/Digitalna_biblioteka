import unittest
import os

class TestFileSave(unittest.TestCase):
    
    def test_fajla(self):
        file_path="listaknjiga.txt"
        unos="test"
        with open("listaknjiga.txt", "w") as file:
            file.write(unos)

        self.assertTrue(os.path.exists(file_path))
        
        with open(file_path, "r") as file:
            unos1= file.read()

        self.assertEqual(unos1, unos)

if __name__ == "__main__":
    unittest.main()