def get_top_k_words(text: str, k):
    text = text.replace(',', '')
    text = text.replace('.', '')
    lista_slow = text.split()
    lista_slow = [elem.lower() for elem in lista_slow if elem != '']
    slownik = dict()
    for element in lista_slow:
        slownik[element] = slownik.get(element, 0) + 1
    lista_krotek = list(slownik.items())
    lista_krotek.sort(reverse=True, key=lambda x: x[1])
    return lista_krotek[:k]


if __name__ == '__main__':
    with open('SPOILER_lorem.txt', 'r') as f:
        tekst = ''
        for i in f.readlines():
            tekst += i.rstrip()
    print(get_top_k_words(tekst, 1))
    print(get_top_k_words(tekst, 3))