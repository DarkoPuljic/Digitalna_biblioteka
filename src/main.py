import unittest
import sys
sys.path.append(r'C:\Users\Darko\Desktop\Darko Puljić Projekat\src')
from book import Knjiga
from library import Biblioteka


knjiga1 = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
knjiga2 = Knjiga("1984", "George Orwell", 1949, "Dystopian fiction")
knjiga3 = Knjiga("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
Biblioteka.dodaj_knjigu(knjiga1)
Biblioteka.dodaj_knjigu(knjiga2)
Biblioteka.dodaj_knjigu(knjiga3)

# Pretraga po naslovu
rezultati_naslov = Biblioteka.pretrazi_po_naslovu("Harry Potter")
print("Rezultati pretrage po naslovu:")
for Knjiga in rezultati_naslov:
    print(f"Naslov: {Knjiga.naslov}, Autor: {Knjiga.autor}, Godina izdavanja: {Knjiga.godina_izdavanja}, Žanr: {Knjiga.zanr}")