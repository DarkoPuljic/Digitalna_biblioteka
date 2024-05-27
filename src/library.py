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