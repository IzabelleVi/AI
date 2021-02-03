
def palingdroom (woord):
    omgedraaid = list(woord)
    omgedraaid.reverse()
    omgedraaid = "".join(omgedraaid)
    return woord == omgedraaid

print(palingdroom("lepel"))