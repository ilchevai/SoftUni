border_first = int(input())
border_second = int(input())
border_third = int(input())

for first in range(1, border_first + 1):
    for second in range(2, border_second + 1):
        second_is_simple = True
        for number in range(2, second):
            if second % number == 0:
                second_is_simple = False
        for third in range(1, border_third + 1):
            if first % 2 == 0 and second_is_simple and third % 2 == 0:
                print(first, second, third)
