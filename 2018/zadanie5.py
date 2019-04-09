from zadanie5_wczytaj import woda

print(woda)
doplywroczny = [0]
i = 0
fiveone = {}
lastBigDoplyw = False
BigDoplywCount = 0
MaxDoplywCount = 0
for i, dzien in enumerate(woda):
    r = dzien['r']
    m = dzien['m']
    d = dzien['d']
    doplyw = dzien['doplyw']

    if m == 1 and d == 1 and i != 0:
        doplywroczny.append(0)
    doplywroczny[-1] += doplyw

    # jesli >= od 10000
    if doplyw >= 10000:

        # jesli jest to pierwszy raz
        if lastBigDoplyw == False:
            fiveone['startdatetemp'] = [r, m, d]

        lastBigDoplyw = True
        BigDoplywCount += 1
    # jesli < 10000
    else:
        # jesli ostatnim razem bylo wieksze lub rowne 10000
        if lastBigDoplyw == True:
            if BigDoplywCount > MaxDoplywCount:
                MaxDoplywCount = BigDoplywCount
            BigDoplywCount = 0
            fiveone['enddate'] = [r, m, d]
        lastBigDoplyw = False


max_value = max(doplywroczny)
print(f"max_value: {max_value}")
max_index = doplywroczny.index(max_value)
print(f"5.1: {max_index+2008}")

print(f"""
5.2: 
startdate = {fiveone['startdate']}
enddate = {fiveone['enddate']}
BigDoplywCount = {BigDoplywCount}
 """)
