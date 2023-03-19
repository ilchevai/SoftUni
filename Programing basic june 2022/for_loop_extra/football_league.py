capacity = int(input())
fans = int(input())
fan1 = 0
fan2 = 0
fan3 = 0
fan4 = 0

for _ in range(fans):
    sector = input()
    if sector == "A":
        fan1 += 1
    elif sector == "B":
        fan2 += 1
    elif sector == "V":
        fan3 += 1
    elif sector == "G":
        fan4 += 1
prc1 = fan1 / fans * 100
prc2 = fan2 / fans * 100
prc3 = fan3 / fans * 100
prc4 = fan4 / fans * 100
prc5 = fans / capacity * 100
print(f"{prc1:.2f}%")
print(f"{prc2:.2f}%")
print(f"{prc3:.2f}%")
print(f"{prc4:.2f}%")
print(f"{prc5:.2f}%")
