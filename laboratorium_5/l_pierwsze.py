def pierwszosc (x):
    if x <= 1:
        return False
    for l in range(2,int(x**0.5)):
        if x % l ==0:
            return False   
    return True

while True:
    x = int(input("Podaj liczbe jaka mam sprawdzic: "))
    if pierwszosc(x) == False:
        while not pierwszosc(x):
            x +=1
        print(f'najblizsza liczba pierwsza blisko twojej jest: {x}')
    else: 
        print("Podana liczba jest liczba pierwasza")


# b = int(input("Podaj koncowy przedzial: "))
# for x in range(2,b):
#     print(x, pierwszosc(x))


# if pierwszosc(x) == False:
#     print("Liczba nie jest pierwsza")
# else:
#     print("Liczba jest pierwsza")
