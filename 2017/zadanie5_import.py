import os
from pprint import pprint

def get_dane(file: str):
    return os.path.join('DANE_PR2', file)

druzyny = []
sedziowie = []
# (mecze)
wyniki = []

class Druzyna():
    def __init__(self, _id, nazwa, miasto):
        self.id = _id
        self.nazwa = nazwa
        self.miasto = miasto
    def __repr__(self):
        return f'<Druzyna nazwa=`{self.nazwa}` id=`{self.id}` miasto=`{self.miasto}`>'

class Sedzia():
    def __init__(self, nr_lic, imie, nazwisko):
        self.nr_lic = nr_lic
        self.imie = imie
        self.nazwisko = nazwisko
    def __repr__(self):
        return f'<Sedzia imie=`{self.imie}` nazwisko=`{self.nazwisko}` nr_lic=`{self.nr_lic}`>'

class Mecz():
    """
    Data_meczu – data rozegrania meczu w formacie rrrr-mm-dd

    Rodzaj_meczu – rodzaj meczu (T – towarzyski, L – ligowy, P – pucharowy, jeden znak)

    Gdzie – miejsce rozegrania meczu (W – wyjazdowy, D – u siebie, jeden znak)

    Id_druzyny – identyfikator drużyny przeciwnej, liczba z zakresu od 1 do 100

    Nr_licencji – numer licencji sędziego meczu, tekst o długości 6 znaków

    Bramki_zdobyte – bramki zdobyte przez Galop Kucykowo, liczba z zakresu od 0 do 20

    Bramki_stracone – bramki stracone przez Galop Kucykowo, liczba z zakresu od 0 do 20
    
    """
    def __init__(self, data, rodzaj, gdzie, id_druzyny, nr_lic, br_zdobyte, br_stracone):
        self.data = data
        self.rok, self.miesiac, self.dzien = data[:4], data[5:7], data[8:11]
        self.rodzaj = rodzaj
        self.gdzie = gdzie

        self.id_druzyny = id_druzyny
        for druzyna in druzyny:
            druzyna: Druzyna
            if druzyna.id == id_druzyny:
                self.druzyna = druzyna
                break
    
        self.nr_lic = nr_lic
        for sedzia in sedziowie:
            sedzia: Sedzia
            if sedzia.nr_lic == nr_lic:
                self.sedzia = sedzia
                break
        self.br_zdobyte = int(br_zdobyte)
        self.br_stracone = int(br_stracone)
    def __repr__(self):
        return f'<Mecz data=`{self.data}` rodzaj=`{self.rodzaj}` gdzie=`{self.gdzie}` id_druzyny=`{self.id_druzyny}` nr_lic=`{self.nr_lic}` sedzia=`{self.sedzia}` br_zdobyte=`{self.br_zdobyte}` br_stracone=`{self.br_stracone}`>'

with open(get_dane('druzyny.txt'), 'r') as druzyny_file:
    for line in druzyny_file:
        line = line.strip().split('\t')
        Id_druzyny = line[0]
        Nazwa = line[1]
        Miasto = line[2]
        if Id_druzyny == "Id_druzyny":
            continue
        druzyny.append(Druzyna(Id_druzyny, Nazwa, Miasto))

with open(get_dane('sedziowie.txt'), 'r') as sedziowie_file:
    for line in sedziowie_file:
        line = line.strip().split('\t')
        Nr_licencji = line[0]
        Imie = line[1]
        Nazwisko = line[2]
        if Nr_licencji == "Nr_licencji":
            continue
        sedziowie.append(Sedzia(Nr_licencji, Imie, Nazwisko))

with open(get_dane('wyniki.txt'), 'r') as wyniki_file:
    for line in wyniki_file:
        line = line.strip().split('\t')
        Data_meczu = line[0]
        Rodzaj_meczu = line[1]
        Gdzie = line[2]
        Id_druzyny = line[3]
        Nr_licencji = line[4]
        Bramki_zdobyte = line[5]
        Bramki_stracone = line[6]
        if Data_meczu == "Data_meczu":
            continue
        wyniki.append(Mecz(Data_meczu, Rodzaj_meczu, Gdzie, Id_druzyny, Nr_licencji, Bramki_zdobyte, Bramki_stracone))

#print(f'druzyny: {druzyny}')
#print(f'sedziowie: {sedziowie}')
#pprint(f'mecze: {wyniki}')