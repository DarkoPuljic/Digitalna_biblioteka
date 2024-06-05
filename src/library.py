class Biblioteka:
    
    def __init__(self):
        self.lista_knjiga = []
        
    def dodaj_knjigu(self, knjiga):
        self.lista_knjiga.append(knjiga)
        
    def ispis_knjiga(self):
        for object in self.lista_knjiga:
            print(object.display_info())