lst= [ 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1]

def check_nul(lst):
   return (lst.count(0))

def check_een(lst):
    return (lst.count(1))

def check():

    nul = check_nul(lst)
    een = check_een(lst)
    if nul > een:
        print("De lijst voldoet niet aan de voorwaarden, er zijn meer nullen dan eenen")
    else:
        if nul > 12:
            print("De lijst voldoet niet aan de voorwaarden, er zijn te veel nullen")
        else:
            print("De lijst voldoet wel aan de voorwaarden")

check()