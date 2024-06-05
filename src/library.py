class Biblioteka:
    
    def __init__(self):
        self.lista_knjiga = []
        
    def dodaj_knjigu(self, knjiga):
        self.lista_knjiga.append(knjiga)
        
    def ispis_knjiga(self):
        for object in self.lista_knjiga:
            print(object.display_info())
            
    def pretraga_knjige(self, kriterijum, uslov):
        lista = []
        with open("listaknjiga.txt", "r") as file:
            for line in file:
                book_data = line.strip().split(", ")
                if kriterijum.lower() == "naslov" and uslov.lower() in book_data[0].lower():
                    lista.append(book_data)
                elif kriterijum.lower() == "autor" and uslov.lower() in book_data[1].lower():
                    lista.append(book_data)
                elif kriterijum.lower() == "godina" and uslov == book_data[2]:
                    lista.append(book_data)
                elif kriterijum.lower() == "zanr" and uslov.lower() in book_data[3].lower():
                    lista.append(book_data)
        return lista