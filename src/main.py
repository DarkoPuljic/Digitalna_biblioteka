from library import Biblioteka
from book import Knjiga
biblioteka = Biblioteka()

while True:   
    print("\n DOBRODOŠLI U DIGITALNU BIBLIOTEKU! \n ŠTA ŽELITE PRVO DA URADITE?: \n 1-ZA DODAVANJE KNJIGE U BIBLIOTEKU \n 2-ZA PRIKAZ KNJIGA \n 3-ZA IZMENU KNJIGE IZ BIBLIOTEKE \n 4-ZA PRIKAZ SVIH KNJIGA  \n 0-ZA IZLAZ IZ BIBLIOTEKE")
    unos= input()

    if unos =="1":
        while True:
            print("MOLIMO VAS DA NAPIŠETE ODGOVARAJUĆE INFORMACIJE O KNJIZI KOJU ŽELITE DA DODATE!")
            naziv = input("NAZIV: ")
            autor = input("AUTOR: ")
            god_izdanja = input("GODINA IZDANJA: ")
            žanr = input("ŽANR: ")
            knjiga = Knjiga(naziv, autor, god_izdanja, žanr)
            biblioteka.dodaj_knjigu(knjiga)
            unos = input("AKO ŽELITE DA PREKINETE UNOS KNJIGA PRITISNITE ENTER")
            with open("listaknjiga.txt", "a") as file:
                for object in biblioteka.lista_knjiga:
                    file.write(object.display_info() + "\n")
            if unos == "":
                break
            
            

    elif unos == "2":
        kriterjum = input("PO ČEMU ŽELITE PRETRAGU?")
        uslov= input("Kljucna rec za pretragu: ")
        lista = biblioteka.pretraga_knjige(kriterjum, uslov)
        print("Rezultati pretrage: ")
        for result in lista:
            print(result)
            
    elif unos == "0":
        break