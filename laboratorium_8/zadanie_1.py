import random
from typing import Counter

def prime(a): #funkcja sprawdzajaca czy liczba jest pierwsza 
    if a == 2 or a == 3:
        return True
    elif a % 2 == 0 or a % 3 == 0 or a <= 1: 
        return False
    i = 5
    while i*i < a:
        if a % i == 0 or a % (i+2) == 0:
            return False 
        i += 6
    return True

def problem(tab): # glowna funkcja dopisujaca oraz sumujaca
        long = len(tab)
        counter = 0
        for i in range(long): # pierwsza petla sprawdzajaca ilosc liczb pierwszych w tablicy
            if prime(tab[i]):
                counter += 1 
        long += counter
        for i in range(long): # druga petla dodajaca 0 po kazdej liczbie pierwszej
            a = tab[i]
            if prime(a):
                tab.insert(i + 1, 0) # moduł .insert (miejsce w tablicy, wartosc) dodaje 0
            else:
                continue
        tab2 = [] # druga tablica ktora ma przechowywac sumy podzbiorów
        sum = 0   
        for s in range(long):
            if tab[s] != 0: # warunek na wykrycie 0 w tablicy
                sum += tab[s]
            else:
                tab2.append(sum) # jesli nie bedzie 0 to dopisze wczesniej policzona sume do nowej tablicy 
                sum = 0 # wyzerowanie "licznika" sumy aby mozna bylo liczyc kolejny podzbior
        return tab,  tab2       

while True:            
    n = int(input("Podaj ile liczb mam wpisac w tablice: "))
    tab = [random.randint(1, 100) for i in range(n)]
    # tab = [7,45,45,34,53,45,4,3,11,18]
    # tab =[77, 53, 92]
    returnik = problem(tab)
    print(returnik)


##### Przypadki testowe #####
# Przypadek nr 1:
# output: lista po dodaniu 0
# Przypadek nr 2:
# output: lista po dodaniu 0 [7,0,45,45,34,53,0,45,4,3,0,11,0,18,30]. Wynik: 7;177;52,11.
# Przypadek nr 3:
# output: lista po dodaniu 0
# Przypadki kolejne: 
# Program jako głowne zalozenie ma generowac liczby losowe i wpisywac je do tablicy, tak wiec reszta sprawdzen moze zostac wykonana na losowo dobranych tabliach: 
# Przypadek z problemem: 
# gdy n =1000000, progam ma problem.
