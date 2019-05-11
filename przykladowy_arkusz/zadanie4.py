from get_dane import get_dane

liczby = []

anagramy = []

with open(get_dane('dane_anagramy.txt'), 'r') as plik:
	for line in plik:
		liczby.append(line.strip().split(' '))


def czy_anagram(liczba1: str, liczba2: str) -> bool:
	global anagramy

	liczby1 = {}
	liczby2 = {}
	for cyfra1, cyfra2 in zip(liczba1, liczba2):
		liczby1.setdefault(cyfra1, 0)
		liczby1[cyfra1] += 1

		liczby2.setdefault(cyfra2, 0)
		liczby2[cyfra2] += 1

	anagramy += [liczby1, liczby2]
	return True if liczby1 == liczby2 else False


ilosc_anagramow = 0

for para_liczb in liczby:
	liczba1 = para_liczb[0]
	liczba2 = para_liczb[1]

	if czy_anagram(liczba1, liczba2):
		ilosc_anagramow += 1

print(f'Ilosc anagramow: {ilosc_anagramow}')


class AnagramySet:

	def __init__(self):
		self.lista = []

	def add(self, anagram: object):
		if anagram not in [x[0] for x in self.lista]:
			self.lista.append([anagram, 1])
		else:
			for i, x in enumerate(self.lista):
				if x[0] == anagram:
					self.lista[i][1] += 1

	def __repr__(self):
		return str(self.lista)


anagramy_set = AnagramySet()

for a in anagramy:
	anagramy_set.add(a)

anagramy_set: list = anagramy_set.lista
anagramy_set.sort(key=lambda x: x[1], reverse=True)
max_ilosc = anagramy_set[0]
print(f'Maksymalna ilosc: {max_ilosc[1]}')
