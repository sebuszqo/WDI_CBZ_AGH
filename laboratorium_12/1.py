def uklad(w1, w2):
    a, b, c = w1
    d, e, f = w2
    y = div(przec(a), b)
    c = div(c, b)
    wolny = div(sub(f, multi(c, e)), d)
    wyn_x = add(multi(y, e), d)
    res_x = div(wolny, wyn_x)

    res_y = div(sub(f, multi(res_x, d)), e)
    print("x: {}, y: {}".format(res_x, res_y))
    res_x, res_y
w1 = ((2,1), (1,1), (3,1))
w2 = ((1,1), (1,1), (1,1))
print(uklad(w1,w2))


def przec(n):
    l, m = n
    return (-l, m)


def odw(n):
    l, m = n
    return (m, l)


def fix_minuses(n):
    l, m = n
    if l < 0 and m < 0:
        return -l, -m
    return l, m


def skroc(n):
    n_l, n_m = n
    for i in range(abs(n_l), 0, -1):
        if n_l % i == 0 and n_m % i == 0:
            n_l //= i
            n_m //= i
            break
    return n_l, n_m

def common_base(n1, n2):
    n1_l, n1_m = skroc(n1)
    n2_l, n2_m = skroc(n2)

    while abs(n1_m) != abs(n2_m):
        if abs(n1_m) < abs(n2_m):
            if n2_m % n1_m == 0:
                n1_l *= n2_m//n1_m
                n1_m *= n2_m//n1_m
            else:
                n1_m *= n2_m
                n1_l *= n2_m
        elif abs(n2_m) < abs(n1_m):
            if n1_m % n2_m == 0:
                n2_l *= n1_m//n2_m
                n2_m *= n1_m//n2_m
            else:
                n2_m *= n1_m
                n2_l *= n1_m
    return n1_l, n1_m, n2_l, n2_m


def add(n1, n2):
    n1_l, n1_m, n2_l, n2_m = common_base(n1,n2)
    l = n1_l + n2_l
    return skroc((l, n1_m))

def sub(n1, n2):
    n1_l, n1_m, n2_l, n2_m = common_base(n1, n2)
    l = n1_l - n2_l
    n = (l, n1_m)
    n = fix_minuses(n)
    return n

def multi(n1, n2):
    n1_l, n1_m = skroc(n1)
    n2_l, n2_m = skroc(n2)
    l = n1_l * n2_l
    m = n1_m * n2_m
    n = (l, m)
    n = fix_minuses(n)
    return skroc(n)


def div(n1, n2):
    n2_l, n2_m = n2
    l, m = multi(n1, (n2_m, n2_l))
    return l, m


def pow(n1, n2):
    n1_l, n1_m = skroc(n1)
    n2_l, n2_m = skroc(n2)
    if (n1_l ** (n2_l/n2_m)) % 1 == 0 and (n1_m ** (n2_l/n2_m)) % 1 == 0:
        return int(n1_l ** (n2_l/n2_m)), int(n1_m ** (n2_l/n2_m))
    print("Napotkano liczbę niewymierną! Zwracanie podanych wartości")
    return n1, n2