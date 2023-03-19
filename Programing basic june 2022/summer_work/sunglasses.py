from math import floor
n = int(input())

print("*" * 2 * n, end="")
print(" " * n, end="")
print("*" * 2 * n, end="")
print()
for row in range(n -2):
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*", end="")
    if row == floor((n - 1) / 2 - 1):
        print("|" * n, end="")
    else:
        print(" " * n, end="")
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*", end="")
    print()
print("*" * 2 * n, end="")
print(" " * n, end="")
print("*" * 2 * n, end="")