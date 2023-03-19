hundred = int(input())
ten = int(input())
one = int(input())

for h in range(1, hundred + 1):
    if h % 2 == 0:
        for t in range(2, ten + 1):
            if t == 2 or t == 3 or t == 5 or t == 7:
                for o in range(1, one + 1):
                    if o % 2 == 0:
                        print(h,t,o)

