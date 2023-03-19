beginning = int(input())
end = int(input())

for num1 in range(beginning, end + 1):
    for num2 in range(beginning, end + 1):
        for num3 in range(beginning, end + 1):
            for num4 in range(beginning, end + 1):
                if (num1 % 2 == 0 and num4 % 2 != 0) or (num1 % 2 != 0 and num4 % 2 == 0):
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(num1, end="")
                            print(num2, end="")
                            print(num3, end="")
                            print(num4, end="")
                            print(end=" ")