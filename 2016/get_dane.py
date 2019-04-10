import os

def get_dane(plik: str) -> str:

    return os.path.join(os.path.split(__file__)[0], "DANE_PR2", plik)

if __name__ == '__main__':
    print(os.path.join(os.path.split(__file__)[0], "DANE_PR2", "dane_6_1.txt"))