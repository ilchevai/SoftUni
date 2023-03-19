n = int(input())
current_bigger_than_n = False
current = 1
for row in range(1, n + 1):
    for colum in range(1, row + 1):
        if current > n:
            current_bigger_than_n = True
            break
        print(str(current) + " ", end="")
        current += 1
    if current_bigger_than_n:
        break
    print()
