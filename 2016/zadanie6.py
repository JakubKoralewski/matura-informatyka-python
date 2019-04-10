from get_dane import get_dane


def zaszyfruj(tekst: str, k: int) -> str:
    nowy_tekst = ''
    for char in tekst:
        nowy_tekst += chr(((ord(char) - 65 + k) % 26) + 65)
    return nowy_tekst


def zad1():
    with open('wyniki_6_1.txt', 'w+') as wyniki_6_1:
        with open(get_dane('dane_6_1.txt'), 'r') as plik6_1:
            for line in plik6_1:
                line = line.strip()
                line_zaszyfr = zaszyfruj(line, 107)
                #print(f'{line} -> {line_zaszyfr}')

                wyniki_6_1.write(f'{line_zaszyfr}\n')
        print(f'Odpowiedzi do zadania 1 zapisano do pliku w {get_dane("dane_6_1.txt")}')
    print('Test:')
    print(f'{ "Przebiegł pomyślnie " if "LQWHUSUHWRZDQLH" == zaszyfruj("INTERPRETOWANIE", 107) else "Nie udało się :("}')
#zad1()


def zad2():
    with open('wyniki_6_2.txt', 'w+') as wyniki:
        with open(get_dane('dane_6_2.txt'), 'r') as plik:
            for line in plik:
                line = line.strip().split(' ')
                try:
                    wyniki.write(f'{zaszyfruj(line[0], -int(line[1]))}\n')
                except IndexError:
                    print('Ta linia jest popsuta. Zgodnie z komunikatem dyrektora CKE z 18 maja 2016 roku.')
        print(f'Odpowiedzi do zadania 2 zapisano do pliku w {get_dane("dane_6_2.txt")}')
    print('Test:')
    print(
        f'{ "Przebiegł pomyślnie " if "ZAWISLAK" == zaszyfruj("BCYKUNCM", -1718) else "Nie udało się :("}')
#zad2()


def oblicz_przesuniecie(chr1: int, chr2: int) -> int:
    return ((chr1 - 65 + (chr1 - chr2)) % 26) + 65


def zad3():
    pierwsze_slowo = ''
    with open('wyniki_6_3.txt', 'w+') as wyniki:
        with open(get_dane('dane_6_3.txt'), 'r') as plik:
            for line in plik:
                line = line.strip().split(' ')
                ost_przesuniecie = -1
                for i, char in enumerate(line[0]):
                    przesuniecie = ((ord(line[0][i]) - ord(line[1][i])) - 65) % 26
                    if i != 0:
                        if przesuniecie != ost_przesuniecie:
                            wyniki.write(line[0] + '\n')
                            break

                    ost_przesuniecie = przesuniecie
    with open('wyniki_6_3.txt', 'r') as wyniki:
        for line in wyniki:
            line = line.strip()
            pierwsze_slowo = line
            break
    print(f'Odpowiedzi do zadania 3 zapisano do pliku w {get_dane("dane_6_3.txt")}')
    print('Test:')
    print(
        f'{ "Przebiegł pomyślnie " if "SMIGIELSKI" == pierwsze_slowo else "Nie udało się :("}')
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
    parser = argparse.ArgumentParser(description='Zadanie 6 z informatyki arkusz 2016. Podpunkty od 1 do 3.')
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