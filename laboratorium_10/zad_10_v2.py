import re

def plik():
    with open("opis_psa.txt", "r", encoding="utf-8") as f:
        tekst = f.read()
        tekst = tekst + " "
        wzor = " "
        return (f"Twój tekst liczy: {len(re.findall(wzor,tekst))} słów.")


if __name__ == "__main__":
    print(plik())

### Przypadki testowe ###
# Plik nr 1 (lorem.txt):
# Ilość słów: 117 
# Plik nr 2 (opis_kota.txt):
# Ilość słów: 39
# Plik nr 3 (opis_psa.txt):
# Ilość słów: 359
