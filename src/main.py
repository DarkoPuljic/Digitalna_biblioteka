import os
from library import Biblioteka
from book import Knjiga
biblioteka = Biblioteka()
file_path = "listaknjiga.txt"
temp_file_path = "listaknjiga_temp.txt"


while True:   
    print("\n DOBRODOŠLI U DIGITALNU BIBLIOTEKU! \n ŠTA ŽELITE PRVO DA URADITE?: \n 1-ZA DODAVANJE KNJIGE U BIBLIOTEKU \n 2-ZA PRIKAZ KNJIGA \n 3-ZA IZMENU KNJIGE IZ BIBLIOTEKE \n 4-ZA BRISANJE KNJIGA  \n 0-ZA IZLAZ IZ BIBLIOTEKE")
    unos= input()

    if unos =="1":
        while True:
            print("MOLIMO VAS DA NAPIŠETE ODGOVARAJUĆE INFORMACIJE O KNJIZI KOJU ŽELITE DA DODATE!")
            naslov = input("NASLOV: ")
            autor = input("AUTOR: ")
            godina_izdavanja = input("GODINA IZDANJA: ")
            žanr = input("ŽANR: ")
            knjiga = Knjiga(naslov, autor, godina_izdavanja, žanr)
            biblioteka.dodaj_knjigu(knjiga)
            unos = input("AKO ŽELITE DA PREKINETE UNOS KNJIGA PRITISNITE ENTER")
            with open("listaknjiga.txt", "a") as file:
                for object in biblioteka.lista_knjiga:
                    file.write(object.display_info() + "\n")
            if unos == "":
                break
            
            

    elif unos == "2":
        kriterjum = input("PO ČEMU ŽELITE PRETRAGU?")
        uslov= input("USLOV ZA PRETRAGU: ")
        lista = biblioteka.pretraga_knjige(kriterjum, uslov)
        print("REZULTATI PRETRAGE: ")
        for result in lista:
            print(result)
            
    elif unos == "3":
        print("Napisi informacije o knjizi koju zelite da izmenite.")
        naslov = input("NASLOV: ")
        autor = input("AUTOR: ")
        godina_izdavanja = input("GODINA IZDAVANJA: ")
        žanr = input("ŽANR: ")
        knjiga = Knjiga(naslov, autor, godina_izdavanja, žanr)

        print("Napisi informacije o izmenjenoj knjizi.")
        naslov1 = input("NASLOV: ")
        autor1 = input("AUTOR: ")
        godina_izdavanja1 = input("GODINA IZDAVANJA: ")
        žanr1 = input("ŽANR: ")
        knjiga1 = Knjiga(naslov1, autor1, godina_izdavanja1, žanr1)

        with open("listaknjiga.txt", "r") as file:
            lines = file.readlines()
    
        lines = [knjiga1.display_info() + '\n' if knjiga.display_info() in line else line for line in lines]
        with open("listaknjiga.txt", "w") as file:
            file.writelines(lines)
    
    elif unos == "4":
        print("NAPIŠITE ODGOVARAJUĆE INFORMACIJE KNJIGE KOJU ŽELITE DA OBRIŠETE")
        naslov = input("NASLOV: ")
        autor = input("AUTOR: ")
        godina_izdavanja = input("GODINA IZDAVANJA: ")
        žanr = input("ŽANR: ")
        knjiga = Knjiga(naslov, autor, godina_izdavanja, žanr)
        with open("listaknjiga.txt", "r") as file:
            lines = file.readlines()
            
        with open("listaknjiga_temp.txt", "w") as temp_file:
            for line in lines:
                if line.strip() != knjiga.display_info().strip():
                    temp_file.write(line)
        os.replace(temp_file_path, file_path)

                
        
    elif unos == "0":
        break
    