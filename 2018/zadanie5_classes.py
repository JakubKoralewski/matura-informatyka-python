from zadanie5_wczytaj import woda
import math


class Dzien:
    dni = []
    iloscDni = 0
    maxDoplyw = 0
    doplywNaRok = [0]
    startRok = 2008
    prevRok = 2008

    def __init__(self, r, m, d, doplyw):
        self.r = r

        if r != Dzien.prevRok:
            Dzien.doplywNaRok.append(0)

        Dzien.prevRok = r
        self.d = d
        self.m = m
        self.doplyw = doplyw
        Dzien.iloscDni += 1
        Dzien.doplywNaRok[-1] += doplyw
        Dzien.dni.append(self)

    @staticmethod
    def getbiggestrokvalue():
        maxdoplyw = 0
        for rok in Dzien.doplywNaRok:
            if rok > maxdoplyw:
                maxdoplyw = rok
        return maxdoplyw

    def data(self):
        return f'{self.r}-{self.m}-{self.d}'

    @staticmethod
    def getdzienbyvalue(**value):
        szukane = [[key, item] for key, item in value.items()][0]
        valuename = szukane[0]
        value = szukane[1]
        for dzien in Dzien.dni:
            print(valuename, getattr(dzien, valuename))
            print(value)
            if getattr(dzien, valuename) == value:
                print(valuename, value)
                return dzien

    @staticmethod
    def getrokbyvalue(value):
        lista = Dzien.doplywNaRok
        for i, rok in enumerate(lista):
            if value == rok:
                return Dzien.startRok + i

    @staticmethod
    def znajdzpasse():
        passa = {}
        started = False
        passaLength = 0
        passaMaxLength = 0
        lista = Dzien.dni
        for dzien in lista:
            if dzien.doplyw >= 10000:
                passaLength += 1
                if started == False:
                    tempstart = f"{dzien.r}-{dzien.d}-{dzien.m}"
                started = True
            else:
                if passaLength > passaMaxLength:
                    passaMaxLength = passaLength
                    passa['start'] = tempstart
                    passa['end'] = tempend
                    passa['length'] = passaLength
                tempend = f"{dzien.r}-{dzien.d}-{dzien.m}"
                started = False
                passaLength = 0
        return passa


for dzien in woda:
    r = dzien['r']
    m = dzien['m']
    d = dzien['d']
    doplyw = dzien['doplyw']
    Dzien(r, m, d, doplyw)

miesiace = [0]


def one_to_three():
    print('')
    prevm = None
    for dzien in Dzien.dni:
        if dzien.r == 2008:
            if prevm is not None:
                if dzien.m == prevm:
                    pass
                else:
                    miesiace.append(0)
            miesiace[-1] += dzien.doplyw
            prevm = dzien.m

    for x, miesiac in enumerate(miesiace):
        miesiac = str(miesiac)
        x = str(x+1)
        print(x.rjust(len(miesiac)), end=" ")
    print()

    for miesiac in miesiace:
        print(miesiac, end=" ")
    print()

    print(Dzien.znajdzpasse())


totalWater = 500000
firstTime = True
for i, dzien in enumerate(Dzien.dni):
    # O polnocy
    assert isinstance(dzien.doplyw, int)
    totalWater += dzien.doplyw

    if totalWater > 1000000:
        if firstTime:
            print(f'PZ. Data: {dzien.data()}')
            firstTime = False
        totalWater = 1000000
    if dzien.r == 2008 and dzien.m == 2 and dzien.d == 1:
        print(f'Data: {dzien.data()}. Poziom wody: {totalWater}')

    # 0 8 rano
    totalWater = totalWater - math.ceil(totalWater*0.02)







