from zadanie6_import import kierowcy, wyscigi, wyniki, Wynik, Kierowca, Wyscig
from pprint import pprint

# z45;Kubica;Robert;Polska
def zad1():
    sezony = {}
    wyscigi_pkt = {}
    for wynik in wyniki:
        wynik: Wynik

        if wynik.id_kierowcy == 'z45':
            sezon = wynik.wyscig.rok
            sezony.setdefault(sezon, 0)
            sezony[sezon] += wynik.pkt
            wyscigi_pkt[wynik.wyscig.gp] = wynik.pkt
    print(f'Najlepszy sezon: {max(sezony.items(), key=lambda x: x[1])}')
    print(f'Najlepszy wyscig: {max(wyscigi_pkt.items(), key=lambda x: x[1])}')
#zad1()

def zad2():
    miejsca = {}
    for wynik in wyniki:
        wynik: Wynik
        miejsce = wynik.wyscig.gp
        miejsca.setdefault(miejsce, 0)
        miejsca[miejsce] += 1
    print(f'Najmniej razy w {min(miejsca.items(),key=lambda x: x[1])}')
#zad2()

def zad3():
    klasyfikacja = {}
    for wynik in wyniki:
        wynik: Wynik
        if wynik.wyscig.rok in [2006, 2000, 2012]:
            klasyfikacja.setdefault(wynik.wyscig.rok, {})
            klasyfikacja[wynik.wyscig.rok].setdefault(wynik.kierowca, 0)
            klasyfikacja[wynik.wyscig.rok][wynik.kierowca] += wynik.pkt
    print(klasyfikacja)
    for rok in klasyfikacja:

        wygrany_kierowca: Kierowca = max(klasyfikacja[rok].items(), key=lambda x: x[1])
        print(f'Zwycięzca w {rok} roku to {wygrany_kierowca[0].imie} {wygrany_kierowca[0].nazwisko}. Zdobył {wygrany_kierowca[1]} pkt.')
#zad3()

def zad4():
    kraje = {}
    for wynik in wyniki:
        if wynik.wyscig.rok == 2012 and wynik.pkt > 0:
            kraj = wynik.kierowca.kraj
            kraje.setdefault(kraj, set())
            kraje[kraj].add(wynik.kierowca)
    for kraj in kraje:
        kraje[kraj] = len(kraje[kraj])
    pprint(kraje)
#zad4()

def wszystkie_zadania():
    for x in range(1, 5):
        odpal_zadanie(x)


def odpal_zadanie(x: int):
    if x < 0 or x > 3:
        print('Zły numer podpunktu. <1-4>')
        return
    print(f'\n\n__________________ZADANIE nr.{x}:\n')
    if x == 1:
        zad1()
    elif x == 2:
        zad2()
    elif x == 3:
        zad3()
    elif x == 4:
        zad4()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Zadanie 6 z informatyki arkusz 2015. Podpunkty od 1 do 4.')
    parser.add_argument('podpunkt', metavar='N', type=str, nargs='*',
                   help='numer podpunktu zadania jakie odpalic, np. `1`, `1 2 3`, `4`, `*`')
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