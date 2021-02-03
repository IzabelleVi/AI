lst = [ [2, 4, 7, 1], [3, 8, 5, 9], [6, 0, 2, 5] ]

def gemiddelde(lst):
    gemiddelde = [sum(x) / len(x) for x in zip(*lst)]
    print(gemiddelde)

gemiddelde(lst)