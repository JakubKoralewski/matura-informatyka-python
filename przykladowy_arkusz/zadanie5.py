from get_dane import get_dane


class Sprzedaz:

    def __init__(self, nr, typ, rodzaj, kolor, cena, data):
        self.nr = nr

        self.typ = typ
        self.rodzaj = rodzaj
        self.kolor = kolor

        self.cena = cena
        self.data = data
        self.data_lista = data.split('-')
	    self.miesiac = self.data_lista[1]

    def __repr__(self):
        return f'<Sprzedaz nr="{self.nr}" typ="{self.typ}" data="{self.data}">'


sprzedaze = []

with open(get_dane('rowery.txt')) as plik:
    for line in plik:
        line = line.strip().split('\t')
        x1 = line[0]
        x2 = line[1]
        x3 = line[2]
        x4 = line[3]
        x5 = line[4]
        x6 = line[5]
        if x1 == 'Nr':
	        continue
        sprzedaze.append(Sprzedaz(x1, x2, x3, x4, x5, x6))

zestawienie = {}

for sprzedaz in sprzedaze:
	zestawienie.setdefault(sprzedaz.typ, 0)
	zestawienie[sprzedaz.typ] += 1

print(sorted(list(zestawienie.items()), key=lambda x: x[1]))


