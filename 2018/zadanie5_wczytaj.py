nazwa = "woda"
woda = []
i = 0
with open(f"DANE_PR2/{nazwa}.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        line = line.split('\t')
        data = line[0].split('-')
        woda.append({
            'r': int(data[0]),
            'm': int(data[1]),
            'd': int(data[2]),
            'doplyw': int(line[1])
        })

        i += 1

