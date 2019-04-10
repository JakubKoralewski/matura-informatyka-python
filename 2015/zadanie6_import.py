from get_dane import get_dane

kierowcy = []
wyniki = []
wyscigi = []


class Kierowca:

    def __init__(self, _id, nazwisko, imie, kraj):
        # Id_kierowcy;Nazwisko;Imie;Kraj
        self.id = _id
        self.nazwisko = nazwisko
        self.imie = imie
        self.kraj = kraj

    def __repr__(self):
        return f'<Kierowca {self.imie} {self.nazwisko}>'


with open(get_dane('Kierowcy.txt')) as kierowcy_plik:
    for line in kierowcy_plik:
        line = line.strip().split(';')
        if line[0] == 'Id_kierowcy':
            continue
        kierowcy.append(Kierowca(line[0], line[1], line[2], line[3]))

class Wyscig:

    def __init__(self, _id, rok, gp):
        self.id = _id
        self.rok = int(rok)
        self.gp = gp


with open(get_dane('Wyscigi.txt')) as kierowcy_plik:
    for line in kierowcy_plik:
        # Id_wyscigu, Rok, GrandPrix
        line = line.strip().split(';')
        if line[0] == 'Id_wyscigu':
            continue
        wyscigi.append(Wyscig(line[0], line[1], line[2]))


class Wynik:

    def __init__(self, id_kierowcy, pkt, id_wyscigu):
        self.id_kierowcy = id_kierowcy

        for kierowca in kierowcy:
            if kierowca.id == id_kierowcy:
                self.kierowca = kierowca
        self.pkt = float(pkt.replace(',', '.'))
        self.id_wyscigu = id_wyscigu

        for wyscig in wyscigi:
            if wyscig.id == id_wyscigu:
                self.wyscig = wyscig


with open(get_dane('Wyniki.txt')) as kierowcy_plik:
    for line in kierowcy_plik:
        # Id_kierowcy, Punkty, Id_wyscigu
        line = line.strip().split(';')
        if line[0] == 'Id_kierowcy':
            continue
        wyniki.append(Wynik(line[0], line[1], line[2]))

#print(f'wyscigi: {wyscigi}')
#print(f'kierowcy: {kierowcy}')
#print(f'wyniki: {wyniki}')