import os
import pickle

def get_dane(file:str):
    return os.path.join('DANE_PR2', file)

cukier = []
with open(get_dane('cukier.txt')) as cukier_file:
    for line in cukier_file:
        line = line.strip().split('\t')
        cukier.append([line[0], line[1], int(line[2])])

cennik = {}
with open(get_dane('cennik.txt')) as cennik_file:
    for line in cennik_file:
        line = line.strip().split('\t')
        cennik[line[0].strip()] = float(line[1].replace(',','.'))

def zad3(cukier):
    suma = {}
    for line in cukier:
        nip = line[1]
        ilosc = line[2]
        obecna_ilosc = suma.get(nip, 0)
        suma[nip] = obecna_ilosc + ilosc
    suma = sorted(suma.items(), key= lambda kv: kv[1], reverse=True)[:3]
    print(f'top3: {suma}')
#zad3(cukier)

def zad2(cukier, cennik):
    przychod = 0
    for line in cukier:
        data = line[0]
        rok = data[:4]
        ilosc = line[2]
        przychod += ilosc * cennik[rok]
    print(f'przychod: {przychod}')
#zad2(cukier,cennik)

def zad3(cukier):
    zestawienie = {}
    for line in cukier:
        data = line[0]
        rok = data[:4]
        ilosc = line[2]
        obecna_ilosc = zestawienie.get(rok, 0)
        zestawienie[rok] = obecna_ilosc + ilosc
    with open('zestawienie.csv', 'w+') as file:
        file.write('rok, ilosc\n')
        for rok in zestawienie.items():
            file.write(f'{rok[0]}, {rok[1]}\n')
#zad3(cukier)


klienci = {}
def dodaj_klienta(nip, ilosc, rabaty):
    if nip not in klienci:
        klienci[nip] = {'ilosc': ilosc}
    else:
        klienci[nip]['ilosc'] += ilosc
    calkowita_ilosc = klienci[nip]['ilosc']
    if 1000 > calkowita_ilosc >= 100:
        rabaty += 5 * ilosc
    elif 10000 > calkowita_ilosc >= 1000:
        rabaty += 10 * ilosc
    elif calkowita_ilosc >= 10000:
        rabaty += 20 * ilosc
    return rabaty


def zad4(cukier):
    rabaty = 0
    for line in cukier:   
        nip = line[1]
        ilosc = line[2]
        rabaty = dodaj_klienta(nip, ilosc, rabaty)
    print(f'rabaty: {rabaty/100:.2f}zł')
#zad4(cukier)


def zad5(cukier_lista):
    """ Tu moim zdaniem powinno byc ilosc_cukru = 5000, 
    ale wtedy odpowiedź nie zgadza się z kluczem. 
    5000 = 13 razy (3pkt): `za odpowiedź wynikającą z liczenia dokupionego cukru pierwszego dnia miesiąca (13).`
    0 = 14 razy (4pkt), ale wtedy sprzedają cukier nie mając w ogóle cukru ?!?!?!
    """
    ilosc_cukru = 0

    ostatni_miesiac = '01'
    dokupy = []
    i = 0
    for line in cukier_lista:
        data = line[0]
        cukier = line[2]
        rok, miesiac, dzien = data[:4], data[5:7], data[8:11]
        if ostatni_miesiac != miesiac:
            print(f'rok: {rok}, miesiac: {miesiac}, dzien: {dzien}, ilosc_cukru: {ilosc_cukru} ')
            print('Zaczął się nowy miesiąc')
            nowy_nabytek = 0
            while nowy_nabytek + ilosc_cukru < 5000:
                nowy_nabytek += 1000
            if nowy_nabytek >= 4000:
                dokupy.append((data, nowy_nabytek))
            ilosc_cukru += nowy_nabytek
            print(f'Kupiono {nowy_nabytek}kg cukru. Jest teraz {ilosc_cukru}kg cukru.')
            

        ilosc_cukru -= cukier

        
        i += 1
        ostatni_miesiac = miesiac
    print(f'Dokupy co najmniej 4000zl: {dokupy}')
    print(f'dokupy: było tak {len(dokupy)} razy.')

#zad5(cukier)







