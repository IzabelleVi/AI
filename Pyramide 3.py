n = int(input())

def pyramide3 (n):
    spatie = 2 * n - 2

    for i in range(0, n):
        for j in range(0, spatie):
            print(end=" ")
        spatie = spatie - 2

        for j in range(0, i + 1):
            print("* ", end="")

        print("\r")


pyramide3(n)