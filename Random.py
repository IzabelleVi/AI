import random

nummer = random.randint(1, 10)


def raad(nummer):
    raad = input("Raad een getal tussen de 1 en 10")
    raad = int(raad)
    while True:
        raad = input("Raad een getal tussen de 1 en 10")
        raad = int(raad)
        if raad == nummer:
            print('Dat nummer is goed!')
            break
        elif raad < nummer:
            print("Het nummer zit hoger!")
            continue
        elif raad > nummer:
            print("Het nummer zit lager!")
            continue



raad(nummer)