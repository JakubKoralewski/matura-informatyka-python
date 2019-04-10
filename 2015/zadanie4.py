from get_dane import get_dane

liczby = []

with open(get_dane('liczby.txt'), 'r') as liczby_plik:
    for line in liczby_plik:
        line = line.strip()
        liczby.append(line)


def ilosc_liczb_0_niz_1(liczby):
    ilosc_takich_liczb = 0
    for liczba in liczby:
        liczba0 = 0
        liczba1 = 0
        for char in liczba:
            if char == '0':
                liczba0 += 1
            elif char == '1':
                liczba1 += 1
        if liczba0 > liczba1:
            ilosc_takich_liczb += 1
        else:
            pass
    return ilosc_takich_liczb


def zad1():
    test_liczby = [
        '101011010011001100111',
        '10001001',
        '1000000',
        '101010011100',
        '100010'
    ]
    test_wynik = ilosc_liczb_0_niz_1(test_liczby)
    zdany = test_wynik == 3
    print(f'Test {"zdany" if zdany else f"Nie zdany, zamiast 3 wyszło {test_wynik}"}')

    print(f'Ilość takich liczb: {ilosc_liczb_0_niz_1(liczby)}')
#zad1()

def zad2ez():
    """
    Ta implementacja problemu w 2 podpunkcie
    wykorzystuje wbudowane funkcje Pythona,
    które bardzo ułatwiają wykonanie tego zadania.
    """
    podzielne_przez_2 = 0
    podzielne_przez_8 = 0
    for liczba in liczby:
        liczba = int(liczba, 2)
        if liczba % 2 == 0:
            podzielne_przez_2 += 1
        if liczba % 8 == 0:
            podzielne_przez_8 += 1
    print(f'Podzielne przez 2: {podzielne_przez_2}')
    print(f'Podzielne przez 8: {podzielne_przez_8}')
#zad2ez()

def str_to_bin_to_int(string: str) -> int:
    value = 0
    i = len(string)-1
    for bin_str in string:
        bin_int = int(bin_str)
        value += bin_int * 2**i
        i -= 1
    return value

def test_str_to_bin_to_int():
    print('Test własnej implementacji.')
    prawidlowo = int('1100101010', 2)
    test = str_to_bin_to_int('1100101010')
    dziala = prawidlowo == test
    print("Udało się" if dziala else f"Nie udało się, bo powinno być {prawidlowo}, a było {test}!")

#test_str_to_bin_to_int()

def zad2():
    """
    Ta implementacja problemu w 2 podpunkcie
    stara się nie wykorzystywać funkcji `int`,
    która czyni ten podpunkt tak łatwym.
    """
    podzielne_przez_2 = 0
    podzielne_przez_8 = 0
    for liczba in liczby:
        liczba = str_to_bin_to_int(liczba)
        if liczba % 2 == 0:
            podzielne_przez_2 += 1
        if liczba % 8 == 0:
            podzielne_przez_8 += 1
    print(f'Podzielne przez 2: {podzielne_przez_2}')
    print(f'Podzielne przez 8: {podzielne_przez_8}')
#zad2()

def zad3():
    lista_liczb_int = [{'wartosc': int(x, 2), 'oryginal': x} for x in liczby]
    maks = max(enumerate(lista_liczb_int), key=lambda x: x[1]['wartosc'])
    minim = min(enumerate(lista_liczb_int), key=lambda x: x[1]['wartosc'])
    print(maks)
    print(f'Maksymalna wartość w linii {maks[0] + 1}')
    print(f'Minimalna wartość w linii {minim[0] + 1}')
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
    parser = argparse.ArgumentParser(description='Zadanie 4 z informatyki arkusz 2015. Podpunkty od 1 do 3.')
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