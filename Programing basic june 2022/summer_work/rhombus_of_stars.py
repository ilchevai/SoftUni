n = int(input())

for row in range(1, n + 1):
    if row < n:
        print(" " * (n - row), end="")
    for col in range(1, row + 1):
        print("* ", end="")
    print()
for rows in range(n - 1, 0, -1):
    if rows < n:
        print(" " * (n - rows), end="")
    for cols in range(rows, 0, -1):
        print("* ", end="")
    print()
