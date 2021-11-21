
# Proszę napisać program, który pobierze od użytkownika 5 różnych liczb całkowitych i doda je do listy. Program ma za zadanie uzupełnić listę liczbami całkowitymi znajdującymi się pomiędzy kolejnymi liczbami a następnie wypisać listę. Przykładowe dane wejściowe: [0,7,13,8,12], pożądane wyjście: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12]. Należy obsłużyć wyjątek, w którym dwie sąsiadujące ze sobą wprowadzone przez użytkownika liczby są takie same. #

#1 funkcja sprawdzająca czy 2 liczby pod rząd nie są takie same
def spr(lista_1):
    try:
        print("Podaj 5 liczb, które mam wpisac do tablicy i ją uzupełnić:")
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
        print("2 liczby sa takie same, spróbuj ponownie.")
        
        
# 2 funkcja wykonująca głowne zadanie tj. dopisywanie do listy brakujących elementów 
def dopisanie(lista_1):
    for a in range(0, len(lista_1)-1): #głowna petla w zakresie dlugosci listy -1, tak zeby program nie pobierał kolejnego wyrazu z listy tj. [0]
        if lista_1[a] > lista_1[a+1]: #sprawdzenie czy dany element listy jest wiekszy niz nastepny
            l = lista_1[a]      
            for l in range(lista_1[a], lista_1[a+1] + 1, -1):  # petla w zakresie od wartosci liczby [...] do wartosci [...+1] dopisuje coraz to mniejsze liczby o 1 w dol (.../.../-1)
                lista_1.append(l)

        elif lista_1[a] < lista_1[a+1]: # warunek odwrotny
            l = lista_1[a]
            for l in range(lista_1[a], lista_1[a+1] + 1):
                lista_1.append(l)
    del lista_1[0:5]# usuniecie pierwszych 4 wyrazow 
    return lista_1 # zwrocenie listy z dopisanymi wyrazami

if __name__ == '__main__':


    lista_1 = []# stworzenie pustej listy ktora bedzie dalej uzupelnniana 
    while True:
        if spr(lista_1) == True:#warunek czy 2 liczby sie nie powtarzaja
            dopisanie(lista_1)# wywolanie listy
            print(lista_1)#print returna tj. listy zwroconej
            lista_1.clear()#wyczyszczenie listy i przygotowanie jej na nastepne dane
        else:
            continue

#####Przypadki testowe#####
# Przypadek 1:
# nr1 = 20 
# nr2 = 30 
# nr3 = 10 
# nr4 = 5 
# nr5 = 10
# return: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 10, 9, 8, 7, 5, 6, 7, 8, 9, 10]
# Przypadek 2(Wyjątek):
# nr1 = 200 
# nr2 = 10
# nr3 = 150
# nr4 = 150
# nr5 =100
# return : 2 liczby sa takie same, sprobuj ponownie
# Przypadek 3:
# nr1 = 10
# nr2 = 1005
# nr3 = 1010
# nr4 = 1000
# nr5 = 1015
# return:
# Przypadek 4 (problem?):
# nr1 = 10
# nr2 = 100000
# nr3 = 10000
# nr4 = 15000
# nr5 = 15100
# return:
############################