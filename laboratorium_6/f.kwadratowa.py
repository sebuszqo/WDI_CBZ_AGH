def delta(a,b,c):
    delta = b**2 - 4*a*c
    try:
        if a + b + c == 0:
            x_1 = 1
            x_2 = c/a
        elif delta > 0:
            delta = delta**0.5
            x_1 = (-b - (delta)) / (2 * a)
            x_2 = (-b + (delta)) / (2 * a)
        elif delta == 0:
            x_1 = x_2 = (-b)/(2*a)
    except delta < 0:
            print("Program nie obsluguje liczb zespolonych.")
    print(x_1, x_2)

print("Podaj współczynniki funkcji kwadratowej (a, b, c)")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta(a,b,c)



