import os 

def get_dane(file: str):
    return os.path.join('DANE_PR2', file)

def get_piksele(debug = False):
    """
    320 wierszy
    200 kolumn
    """
    piksele = []
    with open(get_dane('dane.txt' if not debug else 'przyklad.txt'), 'r') as dane_file:
        for line in dane_file:
            line = line.strip().split(' ')
            piksele.append([int(piksel) for piksel in line])
    return piksele

piksele = get_piksele(debug=False)

def zad1():
    najjasniejszy = -1
    najciemniejszy = 256
    for line in piksele:
        najjasniejszy = max([max(line), najjasniejszy])
        najciemniejszy = min([min(line), najciemniejszy])
    print(f'najjasniejszy: {najjasniejszy}')
    print(f'najciemniejszy: {najciemniejszy}')

#zad1()

def zad2():
    polowa_linii = int(320/2)
    ilosc_nie_majacych_osi = 0
    for line in piksele:
        pierwsza_polowa = line[:polowa_linii]
        druga_polowa = line[polowa_linii:]
        druga_polowa.reverse()
        """ print(f'pierwsza_polowa: {pierwsza_polowa}')
        print(f'druga_polowa.reverse(): {druga_polowa}') """
        if pierwsza_polowa != druga_polowa:
            ilosc_nie_majacych_osi += 1
            #print(f'Linia ma pionową oś symetrii.')
    print(f'ilosc_nie_majacych_osi: {ilosc_nie_majacych_osi}')

#zad2()

def czy_kontrastujace(pix1, pix2):
    if pix1 - pix2 > 128 or pix2 - pix1 > 128:
        return True
    return False

def zad3():
    max_x = 320
    max_y = 200
    """ 4 sasiadujace pixele: UP, DOWN, LEFT, RIGHT """
    odp = 0
    for y in range(len(piksele)):

        line = piksele[y]

        for x in range(len(piksele[0])):
            THIS = line[x]

            left_index = x - 1
            if not left_index < 0:
                LEFT = line[left_index]
                if czy_kontrastujace(THIS, LEFT):
                    odp += 1
                    continue
    
            right_index = x + 1
            if not right_index >= max_x:
                RIGHT = line[right_index]
                if czy_kontrastujace(THIS, RIGHT):
                    odp += 1
                    continue

            up_index = y - 1
            if not up_index < 0:
                UP = piksele[up_index][x]
                if czy_kontrastujace(THIS, UP):
                    odp += 1
                    continue

            down_index = y + 1
            if not down_index >= max_y:
                DOWN = piksele[down_index][x]
                if czy_kontrastujace(THIS, DOWN):
                    odp += 1
                    continue

                
    print(f'odp: {odp}')

#zad3()



def zad4stackoverflow():

    def longest(lista):
        obecna_dlugosc = 0
        najdluzsze = 0
        for i in range(len(lista)):
            if i > 0:
                if lista[i] != lista[i-1]:
                    obecna_dlugosc = 0
            obecna_dlugosc += 1
            if obecna_dlugosc > najdluzsze:
                najdluzsze  = obecna_dlugosc          
        return najdluzsze 

    flipped = list(zip(*piksele)) # Tego bym na pewno nie umiał (bez internetu XD)
    longest_in_flipped = []
    for line in flipped:
        longest_in_flipped.append(longest(line))
    print(max(longest_in_flipped))

zad4stackoverflow()


def zad4():
    """ Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie
    obrazka), złożonej z pikseli tej samej jasności. 
    
    1. Zamień y z x'ami. [[1,2], [3,4]] => [[1,3], [2,4]]
    2. Wyszukaj najdłuższy powtarzający się fragment w każdej z utworzonych list.

    """
    # flipped = list(zip(*piksele)) # stackoverflow :/ Nie uzyje no bo sam bym nie wymyślił :/

    flipped = []
    for x in range(len(piksele[0])):
        for y in range(len(piksele)):
            if flipped[x] == None:
                flipped[x] = []
            flipped[x].append(piksele[y][x])
    print(flipped)

#zad4()



