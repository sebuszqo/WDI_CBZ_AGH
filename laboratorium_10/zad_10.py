def plik(str,s):
    if s == "Y" or s == "y":
        print(str)
    elif s == "N" or s == "n":
        pass
    split = list(str.split())
    print()
    print(split)
    return f"Plik ten zawiera: {len(split)} słów"


if __name__ == "__main__":
    while True:
        f_names = {"1":"lorem.txt", "2":"opis_kota.txt", "3":"opis_psa.txt", "4":"opis_małpy.txt"} 
        print()
        n = input(f"Witaj użytkowniku, wybierz który plik chcesz sprawdzić:\n {f_names} \n:")
        print()
        s = input("Czy chcesz wyświetlić ten plik ? (Y/N): ")
        file_r = f_names[n]
        with open(file_r, "r", encoding="utf-8") as f:
            str = f.read()
        print(plik(str,s))

### Przypadki testowe ###
# Plik nr 1 (lorem.txt):
# Ilość słów: 117 
# Plik nr 2 (opis_kota.txt):
# Ilość słów: 39
# Plik nr 3 (opis_psa.txt):
# Ilość słów: 359
# Plik nr 4 (opis_małpy.txt):
# Ilość słów: 276



