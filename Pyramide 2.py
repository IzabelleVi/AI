n = int(input())

x = 0
while(x < n):
    x += 1
    plek = n - x

    hoeveelheid = 2*x-1
    while(hoeveelheid > 0):
        print("*", end='')
        hoeveelheid -= 1

    print()