import random
from typing import Counter

def prime(a):
    if a == 2 or a == 3:
        return True
    elif a % 2 == 0 or a % 3 == 0 or a <= 1: #wyrzucone liczby parzyste, wiec w dalszym kroku mozna nie sprawdzac podzielnosci przez l.parzyste
        return False
    i = 5
    while i*i < a:
        if a % i == 0 or a % (i+2) == 0:
            return False 
        i += 6
    return True

def problem(tab):
        print(len(tab))
        long = len(tab)
        counter = 0
        for i in range(long):
            if prime(tab[i]):
                counter += 1 
        long += counter
        for i in range(long):
            a = tab[i]
            if prime(a):
                tab.insert(i + 1, 0)
            else:
                continue
        tab2 = []
        sum = 0   
        k = 0
        for s in range(long):
            if tab[s] != 0:
                sum += tab[s]
            else:
                tab2.append(sum)
                sum = 0
        return tab,  tab2       
             
# n = int(input("Podaj ile liczb mam wpisac w tablice: "))
# tab = [random.randint(1, 100) for i in range(n)]
tab = [7,45,45,34,53,45,4,3,11,18]
# tab =[77, 53, 92]
print(problem(tab))
        

    # for i in range(long + 1):
    #     a = tab[i]
    #     if prime(a):
    #         counter +=1
    # print(counter)
# print(tab)

# output:
# lista po modyfikacji [7,0,45,45,34,53,0,45,4,3,0,11,0,18,30]. Wynik: 7;177;52,11.
