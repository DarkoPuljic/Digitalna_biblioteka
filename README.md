# DIGITALNA BIBLIOTEKA
## Opis Projekta
Digitalna biblioteka je jednostavna aplikacija koja omogućava korisnicima da dodaju nove knjige, pretražuju knjige po različitim kriterijumima, izmenjuju informacije o knjigama, brišu knjige iz biblioteke i sačuvaju/učitaju biblioteku iz fajla.

# Pokretanje Aplikacije

KOD JE ISKLUČIVO NAPISAN U PYTHON KODU, TAKO DA JE POTREBNO DA IMATE INSTALIRAN PYTHON NA VAŠEM PERSONALNOM RAČUNARU!

1. Klonirajte repozitorijum:
   git clone https://github.com/DarkoPuljic/Digitalna_biblioteka

2. Pokretanje aplikacije
   python src/main.py

# Korišćenje aplikacije

Nakon što ste uspešno preuzeli i pokrenuli aplikaciju sve komande koje možete koristiti će biti ispisane na terminalu, dok se samo korišćenje izvršava preko terminala.

# Funkcionalnosti
* Dodavanje knjige
  Korisnici mogu dodati knjigu unosom naslova, autora, godine izdavanja i žanra.

* Pretraga knjiga
  Korisnici mogu pretraživati knjige po naslovu, autoru, godini izdavanja ili žanru.
  
* Izmena informacija o knjizi
  Korisnici mogu izmeniti informacije o postojećoj knjizi.

* Brisanje knjige
  Korisnici mogu obrisati knjige iz biblioteke.

* Rad sa fajlovima
  Korisnici mogu sačuvati biblioteku u fajl i učitati biblioteku iz fajla

# User Stories
Korisničke priče su navedene u fajlu user_stories.md.

# Tehnički Zahtevi
Detaljni tehnički zahtevi su navedeni u fajlu requirements.md.

# Testiranje
Aplikacija koristi pristup Test Driven Development-a (TDD). Testovi su locirani u folderu test

* Pokretanje testova
python -m unittest discover -s test

# Autor
Darko Puljić