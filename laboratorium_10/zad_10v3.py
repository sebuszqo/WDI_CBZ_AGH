def word(str,s):
    if s == "Y" or s == "y":
        print(str)
    elif s == "N" or s == "n":
        pass
    for i in '-.,\n':
        str = str.replace(i,' ')
    str = str.lower()
    word_list = str.split()
    return f"Plik ten zawiera: {len(word_list)} słów"




while True:
        f_names = {"1":"lorem.txt", "2":"opis_kota.txt", "3":"opis_psa.txt", "4":"opis_domu.txt", "5":"opis_małpy.txt", "6":"AGH.txt"} 
        print()
        n = input(f"Witaj użytkowniku, wybierz który plik chcesz sprawdzić:\n {f_names} \n:")
        print()
        s = input("Czy chcesz wyświetlić ten plik ? (Y/N): ")
        file_r = f_names[n]
        with open(file_r, "r", encoding="utf-8") as f:
            str = f.read()
        print(word(str,s))