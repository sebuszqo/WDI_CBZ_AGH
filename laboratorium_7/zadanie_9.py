# def spr(lista_1):
#         for i in range (0, len(lista_1)):
#             if lista_1[i] == lista_1[i + 1]:
#                 return False
#             return True

# def dopisanie(lista_1):
#     for a in range(len(lista_1)):
#         if lista_1[a] > lista_1[a+1]:
#             l = lista_1[a]
#             while l != lista_1[a+1]:
#                 lista_1.append(l)
#                 l -= 1
            

            
# print("Podaj 5 liczb, które mam wpisac do tablicy i ją uzupełnić:")

# while True:
#     try:
#         lista_1 = []
#         lista_1.append(int(input("Nr 1: ")))
#         lista_1.append(int(input("Nr 2: ")))
#         lista_1.append(int(input("Nr 3: ")))
#         lista_1.append(int(input("Nr 4: ")))
#         lista_1.append(int(input("Nr 5: ")))
#         spr(lista_1)
#         if spr(lista_1) == True:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("2 liczby sa takie same, probuj ponownie")
#         continue
# dopisanie(lista_1)
# print(lista_1)


def spr(lista_1):
    try:
        lista_1.append(int(input("Nr 1: ")))
        lista_1.append(int(input("Nr 2: ")))
        lista_1.append(int(input("Nr 3: ")))
        lista_1.append(int(input("Nr 4: ")))
        lista_1.append(int(input("Nr 5: ")))
        for i in range (0, (len(lista_1)-1)):
            if lista_1[i] == lista_1[i + 1]:
                lista_1.clear()
                raise ValueError
        # dopisanie(lista_1)
        # return lista_1
        return True
    except ValueError:
        print("2 liczby sa takie same, probuj ponownie")
        
        

def dopisanie(lista_1):
    for a in range(0, len(lista_1)-1):
        if lista_1[a] > lista_1[a+1]:
            l = lista_1[a]
            for l in range(lista_1[a], lista_1[a+1], -1):
                lista_1.append(l)

        elif lista_1[a] < lista_1[a+1]:
            l = lista_1[a]
            for l in range(lista_1[a], lista_1[a+1]):
                lista_1.append(l)
    del lista_1[0:5]
    return lista_1
         #dorzucic zeby wypisywalo jesczze jedna liczbe od ktorej zaczyna i zeby nie bral ostatniej liczby jaka jest w tablicy, elif na odwort i jakos to zlaczyc :c
                # l -= 1
            # while l != lista_1[a+1] and l >= 0:
                   
print("Podaj 5 liczb, które mam wpisac do tablicy i ją uzupełnić:")

lista_1 = []
while True:
    if spr(lista_1) == True:
        dopisanie(lista_1)
        print(lista_1)
        lista_1.clear()
    else:
        continue