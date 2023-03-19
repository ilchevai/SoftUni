n = int(input())

for a in range(1):
    print("+", end=" ")
    for a in range(n - 2):
        print("-", end=" ")
    for a in range(1):
        print("+", end=" ")
        print()
        for b in range(n - 2):
            print("|", end=" ")
            for b in range(n - 2):
                print("-", end=" ")
            for b in range(1):
                print("|", end=" ")
            print()
        for c in range(1):
            print("+", end=" ")
            for c in range(n - 2):
                print("-", end=" ")
            for c in range(1):
                print("+", end=" ")

