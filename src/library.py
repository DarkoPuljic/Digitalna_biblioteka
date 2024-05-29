class Biblioteka:
    def __init__(self):
        self.knjige = []

    def dodaj_knjigu(self, knjiga):
        self.knjige.append(knjiga)
        print("Knjiga dodana!")

    def prikazi_knjige(self):
        if not self.knjige:
            print("Biblioteka je prazna.")
        else:
            print("Knjige u biblioteci:")
            for knjiga in self.knjige:
                print(f"Naslov: {knjiga.naslov}, Autor: {knjiga.autor}, Godina izdavanja: {knjiga.godina_izdavanja}, Žanr: {knjiga.zanr}")
                
                
    def pretrazi_po_naslovu(self, naslov):
        rezultati = []
        for knjiga in self.knjige:
            if naslov.lower() in knjiga.naslov.lower():
                rezultati.append(knjiga)
        return rezultati

    def pretrazi_po_autoru(self, autor):
        rezultati = []
        for knjiga in self.knjige:
            if autor.lower() in knjiga.autor.lower():
                rezultati.append(knjiga)
        return rezultati

    def pretrazi_po_godini(self, godina):
        rezultati = []
        for knjiga in self.knjige:
            if godina == knjiga.godina_izdavanja:
                rezultati.append(knjiga)
        return rezultati

    def pretrazi_po_zanru(self, zanr):
        rezultati = []
        for knjiga in self.knjige:
            if zanr.lower() in knjiga.zanr.lower():
                rezultati.append(knjiga)
        return rezultati
knjiga1 = Knjiga("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
knjiga2 = Knjiga("1984", "George Orwell", 1949, "Dystopian fiction")
knjiga3 = Knjiga("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
biblioteka.dodaj_knjigu(knjiga1)
biblioteka.dodaj_knjigu(knjiga2)
biblioteka.dodaj_knjigu(knjiga3)

# Pretraga po naslovu
rezultati_naslov = biblioteka.pretrazi_po_naslovu("Harry Potter")
print("Rezultati pretrage po naslovu:")
for knjiga in rezultati_naslov:
    print(f"Naslov: {knjiga.naslov}, Autor: {knjiga.autor}, Godina izdavanja: {knjiga.godina_izdavanja}, Žanr: {knjiga.zanr}")