a = int(input())
b = int(input())
max_passwords = int(input())
password = 0
neshto = False
for A in range(ord('#'), ord('7') + 1):
    for B in range(ord('@'), ord('`') + 1):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
                password += 1
                A += 1
                B += 1
                if password == max_passwords or (x == a and y == b):
                    neshto = True
                    break
            if neshto:
                break
        if neshto:
            break
    if neshto:
        break