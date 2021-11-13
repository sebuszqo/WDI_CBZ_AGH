from math import sqrt


def results(a, b, c):
    delta = b*b - 4*a*c
    try:
        if delta > 0:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            print(f'x1 = {x1}  x2= {x2}\n')
            if x1 > 0 and x2 > 0:
                print(f"Postac iloczynowa jest równa: {a}(x-{x1})(x-{x2})\n")
            elif x1 < 0 and x2 < 0:
                print(f"Postac iloczynowa jest równa: {a}(x+{-x1})(x+{-x2})\n")
            elif x1 < 0 and x2 > 0:
                print(f"Postac iloczynowa jest równa: {a}(x+{-x1})(x-{x2})\n")
            elif x1 > 0 and x2 < 0:
                print(f"Postac iloczynowa jest równa: {a}(x-{x1})(x+{-x2})\n")

        elif delta == 0:
            x0 = -b/(2*a)
            print(f'x0 ={x0}')
            if x0 > 0:
                print(f"Postać iloczynowa jest równa: {a}(x-{x0})^2")
            elif x0 < 0:
                print(f"Postać iloczynowa jest równa: {a}(x+{-x0})^2")

        else:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)

    except ValueError:
        return("Program nie obsługuje liczb zespolonych")


while True:
    print("--------------------------------")
    print('Równanie kwadratowe ax^2+bx+c=0')
    print("--------------------------------")
    a = int(input('1. Wartość parametru a: '))
    b = int(input('2. Wartość parametru b: '))
    c = int(input('3. Wartość parametru c: '))
    print("--------------------------------")
    results(a, b, c)
