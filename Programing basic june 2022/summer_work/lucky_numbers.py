n = int(input())
count_1 = 0
count_2 = 0
for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                count_1 = num1 + num2
                count_2 = num3 + num4
                if count_1 == count_2 and n % count_1 == 0:
                    print(num1, end="")
                    print(num2, end="")
                    print(num3, end="")
                    print(num4, end="")
                    print(end=" ")



