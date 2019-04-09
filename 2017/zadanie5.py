from zadanie5_import import druzyny, sedziowie, wyniki, Mecz, Sedzia, Druzyna

def zad1a():
    """Podaj, ile towarzyskich, ile ligowych oraz ile pucharowych meczów rozegrała drużyna
    Galop Kucykowo z drużynami ze swego miasta."""
    towarzyskie = 0
    ligowe = 0
    pucharowe = 0
    for mecz in wyniki:
        mecz: Mecz
        if mecz.druzyna.miasto != 'Kucykowo':
            continue
        if mecz.rodzaj == 'P':
            pucharowe += 1
        elif mecz.rodzaj == 'L':
            ligowe += 1
        elif mecz.rodzaj == 'T':
            towarzyskie += 1
    print(f'towarzyskie: {towarzyskie}\nligowe: {ligowe}\npucharowe: {pucharowe}')
#zad1a()

def zad1b():
    ilosc_na_rok_z_miasta = {}
    for mecz in wyniki:
        mecz: Mecz
        if mecz.druzyna.miasto != 'Kucykowo':
            continue
        obecna_ilosc = ilosc_na_rok_z_miasta.get(mecz.rok, 0)
        ilosc_na_rok_z_miasta[mecz.rok] = obecna_ilosc + 1
    print(f'Max: {sorted(ilosc_na_rok_z_miasta.items(), key = lambda x: x[1], reverse=True)[0]}')
zad1b()

def zad2():
    zestawienie = {}
    for mecz in wyniki:
        mecz: Mecz
        obecna_ilosc = zestawienie.get(mecz.druzyna, 0)
        zestawienie[mecz.druzyna] = obecna_ilosc + mecz.br_zdobyte - mecz.br_stracone
    zerowy_bilans = []
    for druzyna, bilans in zestawienie.items():
        druzyna: Druzyna
        if bilans == 0:
            zerowy_bilans.append(druzyna.nazwa)

        
    print(f'Zestawienie: {zerowy_bilans}')
#zad2()

def zad3():
    wygrane = 0
    przegrane = 0
    zremisowane = 0

    for mecz in wyniki:
        mecz: Mecz
        if mecz.gdzie != 'W':
            continue
        if mecz.br_zdobyte > mecz.br_stracone:
            wygrane += 1
        elif mecz.br_zdobyte < mecz.br_stracone:
            przegrane += 1
        else:
            zremisowane += 1
    
    print(f'Wygrane: {wygrane}')
    print(f'Przegrane: {przegrane}')
    print(f'Zremisowane: {zremisowane}')

#zad3()

def zad4():
    sedziowie_pucharowi = set()
    for mecz in wyniki:
        mecz: Mecz
        if mecz.rodzaj != 'P':
            continue
        sedziowie_pucharowi.add(mecz.sedzia)
    
    sedziowie_niepucharowi = set(sedziowie) - sedziowie_pucharowi 
    print(f'ilosc sedziow niepucharowych: {len(sedziowie_niepucharowi)}')

#zad4()
    
