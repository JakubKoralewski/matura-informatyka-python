def one():
    nazwa = "sygnaly"
    answer = ""
    with open(f"DANE_PR2/{nazwa}.txt", 'r') as file:
        i = 0
        for slowo in file:
            i += 1
            if i % 40 == 0:
                answer+=slowo[9]

    print(answer)

def two():
    nazwa = "sygnaly"
    wynik = []
    with open(f"DANE_PR2/{nazwa}.txt", 'r') as file:
        for slowo in file:
            slowo = slowo.replace("\n", "")
            roznelitery = []
            iloscliter = 0
            for litera in slowo:
                if litera not in roznelitery:
                    roznelitery.append(litera)
                    iloscliter += 1
                #print(litera)
            wynik.append([iloscliter, slowo])
    highestScore = sorted(wynik)[-1][0]
    for slowo in wynik:
        if slowo[0] == highestScore:
            print(slowo[0], slowo[1])
            break
    #print(wynik[-1][1], wynik[-1][0])

def three():
    nazwa = "sygnaly"
    with open(f"DANE_PR2/{nazwa}.txt", 'r') as file:
        for slowo in file:
            slowo = slowo.replace("\n", "")
            dlugosc = len(slowo)
            maxdystans = 0

            for i in range(dlugosc):
                for j in range(dlugosc):

                    dystans = abs(ord(slowo[i]) - ord(slowo[j]))
                    if dystans > maxdystans:
                        maxdystans = dystans

            if maxdystans <= 10:
                print(slowo)




#one()
#two()
three()