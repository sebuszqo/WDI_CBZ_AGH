import re


def plik():
    with open("plik1.txt", "r", encoding="utf-8") as f:
        tekst = f.read()
        tekst = tekst + " "
        wzor = " "
        return (f"Twój tekst liczy: {len(re.findall(wzor,tekst))} słów.")


if __name__ == "__main__":
    print(plik())
