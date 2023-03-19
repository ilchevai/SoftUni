man = int(input())
woman = int(input())
table = int(input())
couple = 0
for m in range(1, man + 1):
    for w in range(1, woman + 1):
        if couple == table:
            break
        print(f"({m} <-> {w})", end=" ")
        couple += 1






