def word(str,s):
    if s == "Y" or s == "y" or s == "":
        print(str)
    elif s == "N" or s == "n":
        pass
    for i in '-.,\n':
        str = str.replace(i,' ') #zamiana tych problematycznych miejsc na puste pole
    str = str.lower() # zamiana wszystkich duzych znaków na małe
    word_list = str.split() #zesplitowanie stringa do tablicy, żeby była tablica złozona z wyrazów 
    print()
    return f"Plik ten zawiera: {len(word_list)} słów" 




while True:
        f_names = {"1":"lorem.txt", "2":"opis_kota.txt", "3":"opis_psa.txt","4":"opis_małpy.txt"} 
        print()
        n = input(f"Witaj użytkowniku, wybierz który plik chcesz sprawdzić:\n {f_names} \n:")
        print()
        s = input("Czy chcesz wyświetlić ten plik ? (Y/n): ")
        print()
        file_r = f_names[n]
        with open(file_r, "r", encoding="utf-8") as f:
            str = f.read()
        print(word(str,s))


        ### Przypadki testowe ###
# Plik nr 1 (lorem.txt):
# Ilość słów: 117 
# Plik nr 2 (opis_kota.txt):
# Ilość słów: 39
# Plik nr 3 (opis_psa.txt):
# Ilość słów: 361 (Dlaczego inaczej niż program "zad_10.py"? Problem z - i dwoma słowami w jednym.)
# Plik nr 4 (opis_małpy.txt):
# Ilość słów: 275




