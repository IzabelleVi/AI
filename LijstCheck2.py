
def verschil(lst, lengte):
    verschil = lst[1] - lst[0]

    for i in range(0, lengte):
        for j in range(i + 1, lengte):
            if (lst[j] - lst[i] > verschil):
                verschil = lst[j] - lst[i]

    return verschil


lst = [1, 5, 12, 18, 21]
lengte = len(lst)
print( verschil(lst, lengte))
