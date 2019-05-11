import os


def get_dane(plik: str) -> str:
    return os.path.join(os.path.split(__file__)[0], "dane_czII", plik)