import sys
max_number = -sys.maxsize

while True:
    number = input()
    if number != "Stop":
        number = int(number)
        if number > max_number:
            max_number = number
    else:
        break

print(max_number)
