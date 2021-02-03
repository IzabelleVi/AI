zin1 = input("Geef een zin:")
zin2 = input("Geef nog een zin:")
n = 0


def tekstcheck(zin1, zin2, n):
    if zin1 == zin2:
        print("De zinnen verschillen niet!")
    if zin1 != zin2:
        aap = True
        while aap:
            if zin1[n] == zin2[n]:
                n = n + 1

            else:
                verschil = n
                aap = False
                print("Het verschil zit op index:", verschil)


tekstcheck(zin1, zin2, n)
