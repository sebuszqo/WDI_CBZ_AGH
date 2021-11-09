def pierwszosc(number):
    if number == 2:
        return True
    elif number % 2 == 0 or number <= 1:
        return False
    for f in range(2, int(number**0.5)+1):
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
            pierwszosc(number)
        print(f'Najblizsza liczba pierwsza blisko twojej jest: {number}')
    else:
        print("Podana liczba jest liczba pierwasza")













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
