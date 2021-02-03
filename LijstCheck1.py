lst = [1, 1, 4, 5, 3, 4, 6, 7, 8, 4, 3, 2, 0, 1, 8, 9, 0, 0, 5, 9, 9, 8, 4, 5, 8, 7, 0]


def count(lst):
    n = int(input("Welk nummer wil je gechecked hebben?"))
    print(lst.count(n))

count(lst)