n = int(input())

for i in range(n + 1):
    print(" " * (n - i), end="")
    print("*" * i, "|", "*" * i)
