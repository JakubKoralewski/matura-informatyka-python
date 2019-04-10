from get_dane import get_dane
from pprint import pprint
import math

class Wojewodztwo():
    def __init__(self, nazwa, k2013, m2013, k2014, m2014):
        self.nazwa = nazwa # np.: `w01D`
        self.numer = nazwa[1:3]
        self.region = nazwa[3:4]

        self.k2013 = int(k2013)
        self.m2013 = int(m2013)
        self.ludnosc2013 = self.k2013 + self.m2013

        self.k2014 = int(k2014)
        self.m2014 = int(m2014)
        self.ludnosc2014 = self.k2014 + self.m2014

        tempa_wzrostu = f'{(self.ludnosc2014 / self.ludnosc2013)}'.split('.')
        self.tempo_wzrostu = float(f'{tempa_wzrostu[0]}.{tempa_wzrostu[1][:4]}')


    def __repr__(self):
        return f'<Wojewodztwo nazwa={self.nazwa} numer={self.numer} region={self.region}>'

    def ludnosc(self, rok: int):
        """
        Jeżeli w jakimś województwie w danym roku ludność jest ponaddwukrotnie większa niż stan
        z roku 2013, to w tym województwie występuje efekt przeludnienia.
        """
        if rok < 2014:
            print('Rok zbyt mały.')
            return
        if rok == 2014:
            return self.ludnosc2014
        else:
            poprzedni_rok = self.ludnosc(rok - 1)
            nowa_wartosc = poprzedni_rok * self.tempo_wzrostu
            if poprzedni_rok > 2 * self.ludnosc2013:
                return poprzedni_rok
            return math.floor(nowa_wartosc)

    def przeludnienie_do_2025(self):
        if self.ludnosc(2025) > 2 * self.ludnosc2013:
            return True
        return False


wojewodztwa = []

with open(get_dane('kraina.txt')) as plik:
    for line in plik:
        line = line.strip().split(';')
        # nazwa województwa, liczba kobiet w 2013 roku, liczba mężczyzn w 2013 roku, liczba kobiet w 2014 roku, liczba mężczyzn w 2014 roku.
        nazwa = line[0]
        k2013 = line[1]
        m2013 = line[2]
        k2014 = line[3]
        m2014 = line[4]
        wojewodztwa.append(Wojewodztwo(nazwa, k2013, m2013, k2014, m2014))

def zad1():
    ludnosc = {}
    for woj in wojewodztwa:
        obecna_ilosc = ludnosc.get(woj.region, 0)
        ludnosc[woj.region] = obecna_ilosc + woj.ludnosc2013

    with open('wykres51.csv', 'w+') as csv:
        csv.write('region, ilosc\n')
        for reg in ludnosc:
            csv.write(f'{reg}, {ludnosc[reg]}\n')

    print(ludnosc)
#zad1()

def zad2():
    odp = {}
    for woj in wojewodztwa:
        if woj.k2014 > woj.k2013 and woj.m2014 > woj.m2013:
            odp.setdefault(woj.region, 0)
            odp[woj.region] += 1
    pprint(odp)
    print(f'W kraju {sum(odp.values())}')
#zad2()

def zad3():
    podpunkt1 = {}
    for woj in wojewodztwa:
        podpunkt1.setdefault(woj.nazwa, 0)
        podpunkt1[woj.nazwa] += woj.ludnosc(2025)

    print("""* Podaj liczbę wszystkich mieszkańców Edulandii w 2025 roku i wskaż, które województwo
będzie miało w tym roku najwięcej mieszkańców.""")
    najwieksza_ilosc = max(podpunkt1.items(), key=lambda x: x[1])
    print(f'Ilość wszystkich mieszkańców to {sum(podpunkt1.values())}')
    print(f'Największą ilość ma {najwieksza_ilosc}\n')

    print("""Podaj liczbę województw, w których kiedykolwiek wystąpi efekt przeludnienia w latach
2014–2025 włącznie.""")
    liczba_przeludnien = 0
    for woj in wojewodztwa:
        if woj.przeludnienie_do_2025():
            liczba_przeludnien += 1
    print(f'Liczba województw z przeludnieniem od 2014-2025 włącznie: {liczba_przeludnien}')
#zad3()

def wszystkie_zadania():
    for x in range(1, 4):
        odpal_zadanie(x)


def odpal_zadanie(x: int):
    if x < 0 or x > 3:
        print('Zły numer podpunktu. <1-3>')
        return
    print(f'\n\n__________________ZADANIE nr.{x}:\n')
    if x == 1:
        zad1()
    elif x == 2:
        zad2()
    elif x == 3:
        zad3()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Zadanie 5 z informatyki arkusz 2015. Podpunkty od 1 do 3.')
    parser.add_argument('podpunkt', metavar='N', type=str, nargs='*',
                   help='numer podpunktu zadania jakie odpalic, np. `1`, `1 2 3`, `3`, `*`')
    args = parser.parse_args()
    if len(args.podpunkt) == 0:
        wszystkie_zadania()
    else:
        for arg in args.podpunkt:
            if arg == '*':
                wszystkie_zadania()
                break
            try:
                arg = int(arg)
            except ValueError:
                print(f'Argument: {arg} jest niepoprawny!')
                continue
            odpal_zadanie(arg)
