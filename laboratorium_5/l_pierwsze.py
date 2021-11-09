def pierwszosc(number):
    if number == 2:
        return True
    elif number % 2 == 0 or number <= 1: #wyrzucone liczby parzyste, wiec w dalszym kroku mozna nie sprawdzac podzielnosci przez l.parzyste
        return False
    for f in range(3, int(number**0.5) + 1,2): #przedział od 3 do number**0.5 + 1, poniewaz dzielniki wystepuja parami.
        if number % f == 0:
            return False
    return True

while True:
    number = int(input("Podaj liczbe jaka mam sprawdzic: "))
    print()
    if pierwszosc(number) == False:
        print("Twoja liczba nie jest pierwsza")
        while pierwszosc(number)==False:
            number += 1
        print(f'Najblizsza liczba pierwsza blisko twojej jest: {number}')
        print()
    else:
        print("Podana liczba jest liczba pierwszą")
        print()













# number = int((input(":")))
# pierwszosc(number)

# if pierwszosc == True:
#     print("Podana liczba jest pierwsza")
# else:
#     print("Podana liczba nie jest pierwsza")

# b = int(input("Podaj koncowy przedzial: "))
# for number in range(2,b):
#     print(number, pierwszosc(number))


# if pierwszosc(number) == False:
#     print("Liczba nie jest pierwsza")
# else:
#     print("Liczba jest pierwsza")
